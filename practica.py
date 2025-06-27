# from manim import *

# # class CircunferenciaIntroduccion(Scene):
# #     def construct(self):
# #         # Escena 1: Introducción al Concepto de Circunferencia
# #         circunferencia_text = Text("Circunferencia", font_size=72, color=BLUE)
# #         circunferencia_text.move_to([0, 3, 0])
# #         self.play(Write(circunferencia_text), run_time=2)
# #         self.wait(2)
# #         self.play(FadeOut(circunferencia_text), run_time=1)

# #         definicion_text = Text("Definición y Caracterización", font_size=36, color=GREEN)
# #         definicion_text.move_to([0, 1.5, 0])
# #         self.play(FadeIn(definicion_text), run_time=1)
# #         self.wait(2)
# #         self.play(FadeOut(definicion_text), run_time=1)

# # class CircunferenciaDefinicionParte1(Scene):
# #     def construct(self):
# #         # Escena 2: Definición de Circunferencia (Parte 1)
# #         definicion_label = Text("Definición:", font_size=48, color=YELLOW)
# #         definicion_label.move_to([-4, 0, 0]).align(LEFT)
# #         self.play(Write(definicion_label), run_time=1.5)
# #         self.wait(1)
# #         self.play(FadeOut(definicion_label), run_time=0.5)

# #         definicion_text = Text("Llamaremos circunferencia al lugar geométrico de todos los puntos cuya distancia a un punto fijo del plano", font_size=24, color=WHITE)
# #         definicion_text.move_to([-2, -1, 0]).align(LEFT)
# #         self.play(Write(definicion_text), run_time=3)
# #         self.wait(2)
# #         self.play(FadeOut(definicion_text), run_time=0.5)

# # class CircunferenciaDefinicionParte2(Scene):
# #     def construct(self):
# #         # Escena 3: Definición de Circunferencia (Parte 2)
# #         o_hk_text = Text("O(h, k)", font_size=36, color=RED)
# #         o_hk_text.move_to([2, -1, 0]).align(LEFT)
# #         self.play(Write(o_hk_text), run_time=1)
# #         self.wait(2)
# #         self.play(FadeOut(o_hk_text), run_time=0.5)

# #         constante_text = Text("(denominado centro) es igual a una constante r", font_size=24, color=WHITE)
# #         constante_text.move_to([-2, -2, 0]).align(LEFT)
# #         self.play(Write(constante_text), run_time=2)
# #         self.wait(2)
# #         self.play(FadeOut(constante_text), run_time=0.5)

# # class CircunferenciaDefinicionParte3(Scene):
# #     def construct(self):
# #         # Escena 4: Definición de Circunferencia (Parte 3)
# #         radio_text = Text("(denominada radio).", font_size=24, color=WHITE)
# #         radio_text.move_to([-2, -3, 0]).align(LEFT)
# #         self.play(Write(radio_text), run_time=1)
# #         self.wait(2)
# #         self.play(FadeOut(radio_text), run_time=0.5)

# # class CircunferenciaTeorema(Scene):
# #     def construct(self):
# #         # Escena 5: Teorema de la Ecuación de la Circunferencia
# #         teorema_label = Text("TEOREMA:", font_size=48, color=YELLOW)
# #         teorema_label.move_to([-4, 1, 0])
# #         self.play(Write(teorema_label), run_time=1)
# #         self.wait(1)
# #         self.play(FadeOut(teorema_label), run_time=0.5)

# #         teorema_text = Text("La circunferencia con centro en O(h, k) y radio r, denotada por C(O,r)", font_size=24, color=WHITE)
# #         teorema_text.move_to([-2, 0, 0]).align(LEFT)
# #         self.play(Write(teorema_text), run_time=3)
# #         self.wait(2)
# #         self.play(FadeOut(teorema_text), run_time=0.5)

# class CircunferenciaEcuacion(Scene):
#     def construct(self):
#         # Escena 6: Ecuación de la Circunferencia
#         ecuacion_label = Text("tiene por ecuación:", font_size=24, color=WHITE)
#         ecuacion_label.move_to([-2, -1, 0])
#         self.play(Write(ecuacion_label), run_time=1)
#         self.wait(1)
#         self.play(FadeOut(ecuacion_label), run_time=0.5)

#         ecuacion_text = MathTex("(x - h)^2 + (y - k)^2 = r^2", font_size=36, color=GREEN)
#         ecuacion_text.move_to([0, -2, 0])
#         self.play(Write(ecuacion_text), run_time=3)
#         self.wait(3)
#         self.play(FadeOut(ecuacion_text), run_time=1)

from manim import *

class CircunferenciaIntroduccion(Scene):
    def construct(self):
        # Texto "Circunferencia"
        circunferencia_text = Text("Circunferencia", font_size=72, color=BLUE)
        circunferencia_text.move_to([0, 3, 0])
        self.play(Write(circunferencia_text), run_time=2)
        self.wait(2)
        self.play(FadeOut(circunferencia_text), run_time=1)

        # Texto "Definición y Caracterización"
        definicion_text = Text("Definición y Caracterización", font_size=36, color=GREEN)
        definicion_text.move_to([0, 1.5, 0])
        self.play(FadeIn(definicion_text), run_time=1)
        self.wait(2)
        self.play(FadeOut(definicion_text), run_time=1)

class CircunferenciaDefinicionParte1(Scene):
    def construct(self):
        # Texto "Definición:"
        definicion_label = Text("Definición:", font_size=48, color=YELLOW)
        definicion_label.move_to([-4, 0, 0])
        definicion_label.to_edge(LEFT)
        self.play(Write(definicion_label), run_time=1.5)
        self.wait(1)
        self.play(FadeOut(definicion_label), run_time=0.5)

        # Texto largo parte 1
        definicion_text = Text(
            "Llamaremos circunferencia al lugar geométrico de todos los puntos cuya distancia a un punto fijo del plano",
            font_size=24, color=WHITE
        )
        definicion_text.move_to([-2, -1, 0])
        definicion_text.to_edge(LEFT)
        self.play(Write(definicion_text), run_time=3)
        self.wait(2)
        self.play(FadeOut(definicion_text), run_time=0.5)

class CircunferenciaDefinicionParte2(Scene):
    def construct(self):
        # Texto "O(h, k)"
        o_hk_text = Text("O(h, k)", font_size=36, color=RED)
        o_hk_text.move_to([2, -1, 0])
        o_hk_text.to_edge(LEFT)
        self.play(Write(o_hk_text), run_time=1)
        self.wait(2)
        self.play(FadeOut(o_hk_text), run_time=0.5)

        # Texto parte 2
        constante_text = Text("(denominado centro) es igual a una constante r", font_size=24, color=WHITE)
        constante_text.move_to([-2, -2, 0])
        constante_text.to_edge(LEFT)
        self.play(Write(constante_text), run_time=2)
        self.wait(2)
        self.play(FadeOut(constante_text), run_time=0.5)

class CircunferenciaDefinicionParte3(Scene):
    def construct(self):
        # Texto parte 3
        radio_text = Text("(denominada radio).", font_size=24, color=WHITE)
        radio_text.move_to([-2, -3, 0])
        radio_text.to_edge(LEFT)
        self.play(Write(radio_text), run_time=1)
        self.wait(2)
        self.play(FadeOut(radio_text), run_time=0.5)

class CircunferenciaTeorema(Scene):
    def construct(self):
        # Texto "TEOREMA:"
        teorema_label = Text("TEOREMA:", font_size=48, color=YELLOW)
        teorema_label.move_to([-4, 1, 0])
        teorema_label.to_edge(LEFT)
        self.play(Write(teorema_label), run_time=1)
        self.wait(1)
        self.play(FadeOut(teorema_label), run_time=0.5)

        # Texto teorema
        teorema_text = Text(
            "La circunferencia con centro en O(h, k) y radio r, denotada por C(O,r)",
            font_size=24, color=WHITE
        )
        teorema_text.move_to([-2, 0, 0])
        teorema_text.to_edge(LEFT)
        self.play(Write(teorema_text), run_time=3)
        self.wait(2)
        self.play(FadeOut(teorema_text), run_time=0.5)

class CircunferenciaEcuacion(Scene):
    def construct(self):
        # Texto "tiene por ecuación:"
        ecuacion_intro = Text("tiene por ecuación:", font_size=24, color=WHITE)
        ecuacion_intro.move_to([-2, -1, 0])
        ecuacion_intro.to_edge(LEFT)
        self.play(Write(ecuacion_intro), run_time=1)
        self.wait(1)
        self.play(FadeOut(ecuacion_intro), run_time=0.5)

        # Ecuación matemática
        ecuacion_text = MathTex(r"(x - h)^2 + (y - k)^2 = r^2", font_size=36, color=GREEN)
        ecuacion_text.move_to([0, -2, 0])
        self.play(Write(ecuacion_text), run_time=3)
        self.wait(3)
        self.play(FadeOut(ecuacion_text), run_time=1)
