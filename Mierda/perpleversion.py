
# from manim import *

# class SeccionConicaDegenerada(Scene):
#     def construct(self):
#         # Texto definición
#         definicion = Text(
#             "Definición: Se denomina sección cónica degenerada a la intersección\n"
#             "de un cono circular recto de dos hojas con un plano que pasa por su vértice.\n"
#             "Se clasifican en tres tipos: punto, recta y par de rectas.",
#             font_size=24,
#             line_spacing=1.2
#         ).to_edge(UP)

#         # Aparece el texto con FadeIn
#         self.play(FadeIn(definicion, shift=DOWN))
#         self.wait(2)

#         # Crear cono simplificado 2D (dos arcos simétricos)
#         cone_left = ArcBetweenPoints(start=2*UP + LEFT, end=2*DOWN + LEFT, angle=PI, color=BLUE)
#         cone_right = ArcBetweenPoints(start=2*UP + RIGHT, end=2*DOWN + RIGHT, angle=PI, color=BLUE)
#         cone = VGroup(cone_left, cone_right).shift(LEFT*2)

#         # Plano que pasa por el vértice (línea vertical roja)
#         plane = Line(3*UP + ORIGIN, 3*DOWN + ORIGIN, color=RED)

#         # Mostrar cono y plano
#         self.play(Create(cone), Create(plane))
#         self.wait(1)

#         # Caso 1: Sección puntual (punto en el vértice)
#         point = Dot(ORIGIN, color=YELLOW)
#         label_point = Text("Punto", font_size=20, color=YELLOW).next_to(point, RIGHT)
#         self.play(FadeIn(point), Write(label_point))
#         self.wait(1)

#         # Caso 2: Sección recta (línea verde)
#         line_intersection = Line(UP, DOWN, color=GREEN).shift(RIGHT*2)
#         label_line = Text("Recta", font_size=20, color=GREEN).next_to(line_intersection, RIGHT)
#         self.play(Create(line_intersection), Write(label_line))
#         self.wait(1)

#         # Caso 3: Par de rectas (dos líneas naranjas cruzadas)
#         line1 = Line(2*UP + 4*LEFT, 2*DOWN + 4*RIGHT, color=ORANGE)
#         line2 = Line(2*UP + 4*RIGHT, 2*DOWN + 4*LEFT, color=ORANGE)
#         label_pair = Text("Par de rectas", font_size=20, color=ORANGE).next_to(line2, RIGHT)
#         self.play(Create(line1), Create(line2), Write(label_pair))
#         self.wait(3)

#         # Transición suave para cerrar la escena
#         self.play(FadeOut(VGroup(definicion, cone, plane, point, label_point,
#                                  line_intersection, label_line, line1, line2, label_pair),
#                           shift=DOWN))
