from manim import *

class Circunferencia(Scene):
    def construct(self):
        # Configuración general
        title_font = "Arial Bold"
        subtitle_font = "Arial"
        text_font = "Arial"
        eq_font = "Arial"

        # Escena 1: Título
        title = Text("Circunferencia", color=YELLOW, font_size=60, font=title_font, stroke_width=2)
        title.move_to(UP*3.5)
        subtitle = Text("Definición y Caracterización", color=WHITE, font_size=30, font=subtitle_font, stroke_width=1)
        subtitle.move_to(UP*3)

        self.play(Write(title))
        self.play(FadeIn(subtitle))
        self.wait(3)
        self.play(FadeOut(title), FadeOut(subtitle))

        # Escena 2: Definición
        definicion_title = Text("Definición:", color=GREEN, font_size=40, font=title_font, stroke_width=1)
        definicion_title.move_to(LEFT*5 + UP*2)
        definicion_text = Text("Llamaremos circunferencia al lugar geométrico de todos los puntos cuya distancia a un punto fijo del plano O(h, k) (denominado centro) es igual a una constante r (denominada radio).",
                              color=WHITE, font_size=24, font=text_font, stroke_width=1, width=9)
        definicion_text.move_to(DOWN*0.5)
        self.play(Write(definicion_title))

        self.play(Write(definicion_text, run_time=7))
        self.wait(3)
        self.play(FadeOut(definicion_title), FadeOut(definicion_text))


        # Escena 3: Visualización del círculo
        circle = Circle(radius=1.5, color=BLUE, stroke_width=3)
        circle.move_to(DOWN*1)
        center_point = Dot(color=RED, radius=0.1)
        center_point.move_to(DOWN*1)  # Mover el centro del círculo al origen
        center_label = Text("O(h, k)", color=RED, font_size=24, font=text_font, stroke_width=1)
        center_label.move_to(RIGHT*0.5 + DOWN*0.5)
        center_label.shift(circle.get_center())  # Asegurarse de que la etiqueta se mueva con el círculo

        radius_line = Line(start=circle.get_center(), end=circle.get_center() + RIGHT*1.5, color=ORANGE, stroke_width=2)
        radius_label = Text("r", color=ORANGE, font_size=30, font=text_font, stroke_width=1)
        radius_label.move_to(circle.get_center() + RIGHT*0.75 + UP*0.1)

        self.play(Create(circle))
        self.play(Create(center_point))
        self.play(FadeIn(center_label))
        self.play(Create(radius_line))
        self.play(FadeIn(radius_label))
        self.wait(5)

        self.play(FadeOut(circle), FadeOut(center_point), FadeOut(center_label), FadeOut(radius_line), FadeOut(radius_label))

        # Escena 4: Teorema Introducción
        teorema_title = Text("Teorema:", color=GREEN, font_size=40, font=title_font, stroke_width=1)
        teorema_title.move_to(LEFT*5 + UP*2)
        teorema_text = Text("La circunferencia con centro en O(h, k) y radio r, denotada por C(O, r) tiene por ecuación:",
                               color=WHITE, font_size=24, font=text_font, stroke_width=1, width=9)
        teorema_text.move_to(DOWN * 0.5)

        self.play(Write(teorema_title))
        self.play(Write(teorema_text, run_time=7))
        self.wait(3)
        self.play(FadeOut(teorema_title), FadeOut(teorema_text))

        # Escena 5: Ecuación
        ecuacion = MathTex(r"(x - h)^2 + (y - k)^2 = r^2", color=YELLOW, font_size=40)
        ecuacion.move_to(DOWN*1)
        self.play(Write(ecuacion))
        self.wait(5)
        self.play(FadeOut(ecuacion))

        self.wait(2)