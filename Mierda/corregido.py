from manim import *

class ConicasDegeneradas(Scene):
    def construct(self):
        # Título
        titulo = Text("Cónicas Degeneradas", font_size=48)
        self.play(Write(titulo))
        self.wait(2)
        self.play(FadeOut(titulo))

        # 1. Cono
        cono = Surface(
            lambda u, v: np.array([
                u * np.cos(v),
                u * np.sin(v),
                u
            ]),
            u_range=[-2, 2],
            v_range=[0, 2 * PI],
            checkerboard_colors=[BLUE_D, BLUE_E],
            resolution=(15, 32)
        )

        cono_abajo = Surface(
            lambda u, v: np.array([
                u * np.cos(v),
                u * np.sin(v),
                -u
            ]),
            u_range=[-2, 2],
            v_range=[0, 2 * PI],
            checkerboard_colors=[BLUE_D, BLUE_E],
            resolution=(15, 32)
        )

        cono_completo = VGroup(cono, cono_abajo)
        self.play(Create(cono_completo))
        self.play(Rotate(cono_completo, angle=PI/6, axis=OUT, rate_func=smooth, run_time=3)) # Rotación lenta

        # 2. Plano
        plano = Surface(
            lambda u, v: np.array([
                u,
                v,
                0
            ]),
            u_range=[-5, 5],
            v_range=[-5, 5],
            fill_opacity=0.3,
            checkerboard_colors=[GREEN_A, GREEN_B]
        )
        plano.set_fill(color=GREEN, opacity=0.3)
        plano.set_stroke(width=1)

        self.play(
            plano.animate.move_to(cono_completo.get_center()),
            run_time=2
        )

        # 3. Punto
        punto = Dot(cono_completo.get_center(), color=RED, radius=0.1)
        self.play(Create(punto), run_time=1)

        self.play(
            self.camera.frame.animate.move_to(cono_completo.get_center()).scale(0.5), # Zoom
            run_time=2
        )
        texto_punto = Text("Punto", color=RED).scale(0.7).next_to(punto, UP)
        self.play(Write(texto_punto))
        self.wait(2)
        self.play(FadeOut(texto_punto))
        self.play(
            self.camera.frame.animate.scale(2).move_to(ORIGIN),
            FadeOut(punto),
            run_time=2
        )

        # 4. Recta
        plano_recta = plano.copy()
        self.play(plano_recta.animate.rotate(PI/4, axis=RIGHT).move_to(ORIGIN)) # Ajustar la posición
        recta = Line(start=np.array([-5, -5*np.tan(PI/4), 0]), end=np.array([5, 5*np.tan(PI/4), 0]), color=YELLOW)
        recta.move_to(ORIGIN + UP*np.sqrt(2))
        self.play(Create(recta))
        texto_recta = Text("Recta", color=YELLOW).scale(0.7).next_to(recta, UP)
        self.play(Write(texto_recta))
        self.wait(2)
        self.play(FadeOut(texto_recta))

        # 5. Par de Rectas
        plano_par_rectas = plano.copy()
        self.play(plano_par_rectas.animate.rotate(PI/8, axis=RIGHT).move_to(ORIGIN)) # Ajustar la posición

        recta1 = Line(start=np.array([-5, -5*np.tan(PI/8), 0]), end=np.array([5, 5*np.tan(PI/8), 0]), color=ORANGE)
        recta2 = Line(start=np.array([-5, 5*np.tan(PI/8), 0]), end=np.array([5, -5*np.tan(PI/8), 0]), color=ORANGE)

        recta1.move_to(ORIGIN + UP*np.cos(PI/8))
        recta2.move_to(ORIGIN + UP*np.cos(PI/8))

        self.play(Create(recta1), Create(recta2))
        texto_par_rectas = Text("Par de Rectas", color=ORANGE).scale(0.7).next_to(recta1, UP)
        self.play(Write(texto_par_rectas))
        self.wait(2)
        self.play(FadeOut(texto_par_rectas))

        self.wait(2)
        self.play(FadeOut(cono_completo, plano, plano_recta, plano_par_rectas, recta, recta1, recta2))

        # Traslación de Coordenadas
        titulo_traslacion = Text("Traslación de Coordenadas", font_size=48)
        self.play(Write(titulo_traslacion))
        self.wait(2)
        self.play(FadeOut(titulo_traslacion))

        # 1. Sistema OXY
        ejes_oxy = Axes(x_range=[-5, 5, 1], y_range=[-5, 5, 1], axis_config={"include_tip": True})
        ox_label = ejes_oxy.get_x_axis_label("X")
        oy_label = ejes_oxy.get_y_axis_label("Y")
        origen_o = Dot(ejes_oxy.coords_to_point(0, 0), color=RED, radius=0.1).set_z_index(1)
        o_label = MathTex("O").next_to(origen_o, DOWN+LEFT)

        self.play(Create(ejes_oxy), Write(ox_label), Write(oy_label), Create(origen_o), Write(o_label))

        # 2. Sistema O'X'Y'
        ejes_oxyr = Axes(x_range=[-5, 5, 1], y_range=[-5, 5, 1], axis_config={"include_tip": True})
        oxr_label = ejes_oxyr.get_x_axis_label("X'")
        oyr_label = ejes_oxyr.get_y_axis_label("Y'")
        origen_or = Dot(ejes_oxyr.coords_to_point(0, 0), color=GREEN, radius=0.1).set_z_index(1)
        or_label = MathTex("O'").next_to(origen_or, UP+RIGHT)

        ejes_oxyr.move_to(np.array([3, -2, 0])) # Posición inicial aleatoria

        self.play(Create(ejes_oxyr), Write(oxr_label), Write(oyr_label), Create(origen_or), Write(or_label))

        self.play(
            ejes_oxyr.animate.move_to(np.array([1, 1, 0])),
            #origen_or.animate.move_to(ejes_oxyr.coords_to_point(0,0)),
            oxr_label.animate.next_to(ejes_oxyr.x_axis.get_end(), RIGHT),
            oyr_label.animate.next_to(ejes_oxyr.y_axis.get_end(), UP),
            or_label.animate.next_to(origen_or, UP+RIGHT),

            run_time=3,
            rate_func=smooth
        ) # Movimiento paralelo
        origen_or.move_to(ejes_oxyr.coords_to_point(0,0))

        # 3. Vector OO'
        vector_oo = Arrow(start=ejes_oxy.coords_to_point(0, 0), end=ejes_oxyr.coords_to_point(0, 0), color=YELLOW, buff=0)
        oo_label = MathTex(r"\vec{OO'}", color=YELLOW).next_to(vector_oo.get_center(), UP)

        self.play(Create(vector_oo), Write(oo_label))

        # 4. Énfasis
        # Resaltar paralelismo (usando flechas pequeñas)
        flecha_paralela_x = Arrow(start=ejes_oxy.x_axis.get_end() + DOWN * 0.3, end=ejes_oxyr.x_axis.get_end() + DOWN * 0.3, color=BLUE, buff=0, max_tip_length_to_length_ratio=0.1)
        flecha_paralela_y = Arrow(start=ejes_oxy.y_axis.get_end() + RIGHT * 0.3, end=ejes_oxyr.y_axis.get_end() + RIGHT * 0.3, color=BLUE, buff=0, max_tip_length_to_length_ratio=0.1)

        paralelo_text = Text("Paralelos", color=BLUE).scale(0.6).move_to(np.array([3,-3,0]))

        self.play(Create(flecha_paralela_x), Create(flecha_paralela_y), Write(paralelo_text))
        self.wait(3)


        self.wait(3)
        self.play(FadeOut(ejes_oxy, ox_label, oy_label, origen_o, o_label, ejes_oxyr, oxr_label, oyr_label, origen_or, or_label, vector_oo, 
oo_label, flecha_paralela_x, flecha_paralela_y, paralelo_text))
        self.wait(1)