from manim import *

class SeccionConicaDegenerada3D(ThreeDScene):
    def construct(self):
        # Texto definición
        definicion = Text(
            "Definición:\nSe denomina sección cónica degenerada a la intersección\n"
            "de un cono circular recto de dos hojas con un plano que pasa por su vértice.\n"
            "Se clasifican en tres tipos: punto, recta y par de rectas.",
            font_size=24,
            line_spacing=1.2
        ).to_edge(UP)
        self.play(Write(definicion))
        self.wait(2)

        # Configurar ejes 3D
        axes = ThreeDAxes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            z_range=[-3, 3, 1],
            x_length=6,
            y_length=6,
            z_length=6,
        )
        self.add(axes)

        # Crear cono circular recto de dos hojas (dos conos invertidos)
        cone_up = Cone(
            base_radius=1.5,
            height=3,
            direction=UP,
            fill_opacity=0.5,
            checkerboard_colors=False,
            color=BLUE,
        ).move_to(ORIGIN)

        cone_down = Cone(
            base_radius=1.5,
            height=3,
            direction=DOWN,
            fill_opacity=0.5,
            checkerboard_colors=False,
            color=BLUE,
        ).move_to(ORIGIN)

        self.play(FadeIn(cone_up), FadeIn(cone_down))
        self.wait(1)

        # Plano que pasa por el vértice (un plano XY en z=0)
        plane = Surface(
            lambda u, v: np.array([u, v, 0]),
            u_range=[-3, 3],
            v_range=[-3, 3],
            fill_opacity=0.5,
            checkerboard_colors=[RED_D, RED_E],
            stroke_color=RED,
        )
        self.play(FadeIn(plane))
        self.wait(1)

        # Mostrar intersección - Caso 1: Punto (vértice)
        punto = Dot3D(point=ORIGIN, color=YELLOW, radius=0.1)
        label_punto = Text("Punto", font_size=20, color=YELLOW).to_corner(UL)
        self.play(FadeIn(punto), Write(label_punto))
        self.wait(1)

        # Caso 2: Recta (línea intersección)
        linea = Line3D(start=np.array([-1.5, 0, 0]), end=np.array([1.5, 0, 0]), color=GREEN, stroke_width=4)
        label_linea = Text("Recta", font_size=20, color=GREEN).next_to(linea.get_center(), DOWN)
        self.play(Create(linea), Write(label_linea))
        self.wait(1)

        # Caso 3: Par de rectas (dos líneas que se cruzan)
        linea1 = Line3D(start=np.array([-1.5, -1.5, 0]), end=np.array([1.5, 1.5, 0]), color=ORANGE, stroke_width=4)
        linea2 = Line3D(start=np.array([-1.5, 1.5, 0]), end=np.array([1.5, -1.5, 0]), color=ORANGE, stroke_width=4)
        label_par = Text("Par de rectas", font_size=20, color=ORANGE).next_to(linea2.get_center(), UP)
        self.play(Create(linea1), Create(linea2), Write(label_par))
        self.wait(3)

        # Transición para cerrar escena
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=2
        )
