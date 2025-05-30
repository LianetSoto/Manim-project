from manim import *

class DegenerateConics(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)

        # Parte 1: Secciones Cónicas Degeneradas

        # Introducción Visual
        cone = Cone(direction=UP, base_radius=2, height=4, resolution=24)  # Reducir la resolución para velocidad
        cone.rotate(PI / 2, axis=RIGHT)
        cone.rotate(PI, axis=UP)
        cone.set_color(BLUE_E)
        cone.set_opacity(0.7)

        degenerate_conics_text = Tex("Secciones Cónicas Degeneradas").to_edge(UP)
        self.play(Create(cone), Write(degenerate_conics_text))
        self.wait(2)

        # Punto
        point_plane = Surface(
            lambda u, v: np.array([u, v, 2]),
            u_range=[-3, 3],
            v_range=[-3, 3],
            resolution=(10, 10),  # Reducir la resolución para velocidad
        )
        point_plane.set_color(GREEN)
        point_plane.set_opacity(0.5)
        point_plane.move_to(UP * 4)

        point_text1 = Tex("Un plano que pasa por el vértice del cono").next_to(degenerate_conics_text, DOWN, buff=0.5)
        point_text2 = Tex("Intersección: Un Punto").next_to(point_text1, DOWN, buff=0.5)

        point = Dot3D(ORIGIN, color=YELLOW)
        self.play(
            AnimationGroup(
                Create(point_plane),
                Write(point_text1),
                lag_ratio=0.2
            )
        )
        self.play(point_plane.animate.move_to(ORIGIN))
        self.play(Create(point), Write(point_text2))
        self.wait(2)
        self.play(FadeOut(point_plane, point, point_text1, point_text2))



        # Recta
        line_plane = Surface(
            lambda u, v: np.array([u, v, v]),
            u_range=[-3, 3],
            v_range=[-3, 3],
            resolution=(10, 10),  # Reducir la resolución para velocidad
        )
        line_plane.set_color(GREEN)
        line_plane.set_opacity(0.5)
        line_plane.move_to(LEFT * 4)

        line_text1 = Tex("Un plano tangente al cono, pasando por el vértice").next_to(degenerate_conics_text, DOWN, buff=0.5)
        line_text2 = Tex("Intersección: Una Recta").next_to(line_text1, DOWN, buff=0.5)

        line = Line3D(start=-3 * UP, end=3 * UP, color=YELLOW)

        self.play(
             AnimationGroup(
                Create(line_plane),
                Write(line_text1),
                lag_ratio=0.2
            )
        )
        self.play(line_plane.animate.move_to(ORIGIN))
        self.play(Create(line), Write(line_text2))
        self.wait(2)
        self.play(FadeOut(line_plane, line, line_text1, line_text2))

        # Par de Rectas
        pair_plane = Surface(
            lambda u, v: np.array([u, v, u]),
            u_range=[-3, 3],
            v_range=[-3, 3],
            resolution=(10, 10),  # Reducir la resolución para velocidad
        )
        pair_plane.set_color(GREEN)
        pair_plane.set_opacity(0.5)
        pair_plane.move_to(RIGHT * 4)

        pair_text1 = Tex("Un plano que intersecta ambas hojas del cono, pasando por el vértice").next_to(degenerate_conics_text, DOWN, buff=0.5)
        pair_text2 = Tex("Intersección: Un Par de Rectas").next_to(pair_text1, DOWN, buff=0.5)

        line1 = Line3D(start=-3 * LEFT + -3 * UP, end=3 * RIGHT + 3 * UP, color=YELLOW)
        line2 = Line3D(start=-3 * RIGHT + -3 * UP, end=3 * LEFT + 3 * UP, color=YELLOW)

        self.play(
            AnimationGroup(
                Create(pair_plane),
                Write(pair_text1),
                lag_ratio=0.2
            )
        )
        self.play(pair_plane.animate.move_to(ORIGIN))
        self.play(Create(line1), Create(line2), Write(pair_text2))
        self.wait(2)
        self.play(FadeOut(pair_plane, line1, line2, pair_text1, pair_text2))

        # Resumen
        summary_text = Tex("Secciones Cónicas Degeneradas: Punto, Recta, Par de Rectas").to_edge(DOWN)
        point = Dot3D(ORIGIN, color=YELLOW)
        line = Line3D(start=-3 * UP, end=3 * UP, color=YELLOW)
        line1 = Line3D(start=-3 * LEFT + -3 * UP, end=3 * RIGHT + 3 * UP, color=YELLOW)
        line2 = Line3D(start=-3 * RIGHT + -3 * UP, end=3 * LEFT + 3 * UP, color=YELLOW)

        self.play(
            AnimationGroup(
                Create(point),
                Create(line),
                Create(line1),
                Create(line2),
                Write(summary_text),
                lag_ratio=0.2
            )
        )
        self.wait(3)
        self.play(FadeOut(cone, point, line, line1, line2, degenerate_conics_text, summary_text))
        self.wait(1)



class CoordinateTranslation(Scene):
    def construct(self):
        # Parte 2: Traslación de un Sistema de Coordenadas

        # Introducción Visual
        oxy_axes = Axes(x_range=[-5, 5, 1], y_range=[-5, 5, 1], axis_config={"include_numbers": True, "numbers_to_exclude": [0]})
        square = Square(side_length=2).move_to([2, 2, 0])
        circle = Circle(radius=1).move_to([-2, -2, 0])

        translation_text = Tex("Traslación de un Sistema de Coordenadas").to_edge(UP)

        self.play(
            AnimationGroup(
                Create(oxy_axes),
                Create(square),
                Create(circle),
                Write(translation_text),
                lag_ratio=0.2
            )
        )
        self.wait(2)

        # Explicación de la Traslación
        oxprimeyprime_axes = Axes(x_range=[-5, 5, 1], y_range=[-5, 5, 1], axis_config={"include_numbers": True, "numbers_to_exclude": [0]}) 
        oxprimeyprime_axes.move_to([3, 2, 0])

        translation_vector = Vector([3, 2])
        translation_vector_label = Tex("Vector de Traslación: $\\vec{OO'}$").next_to(translation_vector, UP)

        new_system_text = Tex("Nuevo sistema de coordenadas $O'X'Y'$").next_to(translation_text, DOWN, buff=0.5)
        parallel_text = Tex("Ejes paralelos: $O'X' || OX, O'Y' || OY$").next_to(new_system_text, DOWN, buff=0.5)

        self.play(
            AnimationGroup(
                Create(oxprimeyprime_axes),
                Write(new_system_text),
                lag_ratio=0.2
            )
        )
        self.play(Write(parallel_text))
        self.play(Create(translation_vector), Write(translation_vector_label))

        self.wait(3)

        # Impacto en las Figuras
        square_translated = Square(side_length=2).move_to([2 + 3, 2 + 2, 0])  # Translate square
        circle_translated = Circle(radius=1).move_to([-2 + 3, -2 + 2, 0])  # Translate circle

        shape_preserved_text = Tex("La forma y el tamaño se conservan").to_edge(DOWN)

        self.play(
            AnimationGroup(
                square.animate.move_to(square_translated.get_center()),
                circle.animate.move_to(circle_translated.get_center()),
                Write(shape_preserved_text),
                lag_ratio=0.2
            )
        )


        self.wait(3)
        self.play(FadeOut(oxy_axes, oxprimeyprime_axes, square, circle, translation_vector, translation_vector_label, translation_text, new_system_text, parallel_text, shape_preserved_text))
        self.wait(1)