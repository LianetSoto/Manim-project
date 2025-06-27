from manim import *

class ConicSections(Scene):
    def construct(self):
        # Configuración inicial
        cone = ParametricSurface(
            lambda u, v: np.array([
                np.sqrt(u) * np.cos(v),
                np.sqrt(u) * np.sin(v),
                u
            ]),
            u_range=[0, 4],
            v_range=[0, 2 * PI],
            checkerboard_colors=[BLUE_D, BLUE_E],
            resolution=(15, 32)  # Ajustar resolución para mejor calidad
        )

        cone_down = ParametricSurface(
            lambda u, v: np.array([
                np.sqrt(u) * np.cos(v),
                np.sqrt(u) * np.sin(v),
                -u
            ]),
            u_range=[0, 4],
            v_range=[0, 2 * PI],
            checkerboard_colors=[BLUE_D, BLUE_E],
            resolution=(15, 32)  # Ajustar resolución para mejor calidad
        )

        double_cone = Group(cone, cone_down).scale(1.2)
        double_cone.shift(UP) # Mover un poco arriba para mejor visualizacion

        # Escena 1: Plano cortando en el vértice
        plane_vertex = ParametricSurface(
            lambda u, v: np.array([u, v, 0]),
            u_range=[-3, 3],
            v_range=[-3, 3],
            color=GREEN_D,
            opacity=0.5
        )

        point = Sphere(radius=0.05, color=YELLOW, shininess=50).move_to(ORIGIN + UP) # Ajustar la posicion del punto       
        text_vertex = Text("Intersección: Un punto", font_size=24).to_edge(DOWN) # Texto mas pequeño y en el borde

        self.play(Create(double_cone), run_time=2)
        self.play(Create(plane_vertex), run_time=2)
        self.play(Create(point), run_time=1)
        self.play(Write(text_vertex), run_time=1) # Animar el texto
        self.wait(2)
        self.play(FadeOut(plane_vertex, point, text_vertex))


        # Escena 2: Plano tangente al cono
        plane_tangent = ParametricSurface(
            lambda u, v: np.array([u, v, v]),
            u_range=[-3, 3],
            v_range=[-3, 3],
            color=GREEN_D,
            opacity=0.5
        ).rotate(PI/4, axis=RIGHT) # Rota el plano

        line = Line(start=(-2, -2, -2), end=(2, 2, 2), color=YELLOW, stroke_width=5).rotate(PI/4, axis=RIGHT).shift(UP) # Ajuste de la linea
        text_tangent = Text("Intersección: Una línea", font_size=24).to_edge(DOWN) # Texto mas pequeño y en el borde       
        self.play(Create(plane_tangent), run_time=2)
        self.play(Create(line), run_time=1)
        self.play(Write(text_tangent), run_time=1) # Animar el texto
        self.wait(2)
        self.play(FadeOut(plane_tangent, line, text_tangent))

        # Escena 3: Plano cortando el cono creando dos líneas
        plane_two_lines = ParametricSurface(
            lambda u, v: np.array([u, v, v*0.5]),
            u_range=[-3, 3],
            v_range=[-3, 3],
            color=GREEN_D,
            opacity=0.5
        ).rotate(PI/6, axis=RIGHT)

        line1 = Line(start=(-2, -2, -1), end=(2, 2, 1), color=YELLOW, stroke_width=5).rotate(PI/6, axis=RIGHT).shift(UP) # 

        line2 = Line(start=(-2, 2, -1), end=(2, -2, 1), color=YELLOW, stroke_width=5).rotate(PI/6, axis=RIGHT).shift(UP) # 

        text_two_lines = Text("Intersección: Dos líneas", font_size=24).to_edge(DOWN) # Texto mas pequeño y en el borde    

        self.play(Create(plane_two_lines), run_time=2)
        self.play(Create(line1), run_time=1)
        self.play(Create(line2), run_time=1)
        self.play(Write(text_two_lines), run_time=1) # Animar el texto
        self.wait(2)
        self.play(FadeOut(double_cone, plane_two_lines, line1, line2, text_two_lines))

        # Escena 4: Traslación de coordenadas
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            axis_config={"include_tip": True, "numbers_to_exclude": [0]}
        )
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")

        axes_new = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            axis_config={"include_tip": True, "numbers_to_exclude": [0]}
        ).shift([2, 1, 0])  # Desplazamiento del nuevo sistema
        axes_labels_new = axes_new.get_axis_labels(x_label="x'", y_label="y'")

        arrow = Arrow(start=axes.get_origin(), end=axes_new.get_origin(), buff=0)
        text_translation = Text("Traslación de origen", font_size=24).to_edge(DOWN) # Texto mas pequeño y en el borde      

        self.play(Create(axes), Create(axes_labels), run_time=2)
        self.play(Create(axes_new), Create(axes_labels_new), run_time=2)
        self.play(Create(arrow), run_time=1)
        self.play(Write(text_translation), run_time=1) # Animar el texto
        self.wait(3)