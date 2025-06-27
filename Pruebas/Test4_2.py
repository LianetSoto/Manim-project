from manim import *

class Circunferencia(Scene):
    def construct(self):
        # Configuración inicial
        self.camera.background_color = BLACK

        # Plano sutilmente degradado
        plane = NumberPlane(
            x_range=[-7, 7, 1],
            y_range=[-5, 5, 1],
            axis_config={"stroke_color": WHITE, "stroke_width": 1}
        ).fade(0.7)
        self.add(plane)

        # Punto rojo en el origen
        origin_point = Dot(ORIGIN, color=RED, radius=0.15)
        self.add(origin_point)

        # Número de líneas punteadas
        num_lines = 50
        radius = 3  # Radio de la circunferencia

        # Grupos para las líneas y los puntos finales
        lines_group = VGroup()
        dots_group = VGroup()

        # Creación de las líneas punteadas y los puntos finales
        for i in range(num_lines):
            angle = i * 2 * PI / num_lines
            end_point = origin_point.get_center() + radius * np.array([np.cos(angle), np.sin(angle), 0])
            dashed_line = DashedLine(origin_point.get_center(), end_point, stroke_width=2, color=WHITE)
            end_dot = Dot(end_point, color=WHITE, radius=0.03)

            lines_group.add(dashed_line)
            dots_group.add(end_dot)

        # Animación de creación de las líneas y los puntos
        self.play(
            Create(lines_group),
            Create(dots_group),
            run_time=2,
            rate_func=smooth
        )
        self.wait(0.5)

        # ******************* Escena 2 *******************

        # Creación del rastro
        tracer = TracedPath(dots_group[0].get_center, dissipating_time=1, stroke_color=BLUE, stroke_width=3)
        self.add(tracer)

        # Animación de los puntos dejando rastro y formando el círculo
        for dot in dots_group:
            tracer.add_updater(lambda mob, dt, d=dot: mob.move_to(d.get_center()))

        self.wait(2)

        # Detener el updater para evitar que el rastro siga actualizandose
        for dot in dots_group:
            tracer.clear_updaters()

        # Desvanecer los puntos
        self.play(
            FadeOut(dots_group),
            FadeOut(lines_group),
            run_time=1,
            rate_func=smooth
        )
        self.wait(0.5)

        # Acercamiento gradual a la circunferencia
        # self.play(
        #     self.camera.animate.set(width=5), # Ajustar el valor para el nivel de zoom deseado
        #     run_time=3,
        #     rate_func=smooth
        # )

        self.wait(2)