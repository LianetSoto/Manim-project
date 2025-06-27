from manim import *

class Circunferencia(Scene):
    def construct(self):
        # Título
        titulo = Text("Circunferencia", font_size=48).to_edge(UP)
        self.play(Write(titulo))
        self.wait(1)

        # Definición
        definicion = Tex(
            r"Llamaremos \textbf{circunferencia} al lugar geométrico de todos los puntos",
            r" cuya distancia a un punto fijo del plano $O(h, k)$ (denominado \textbf{centro})",
            r" es igual a una constante $r$ (denominado \textbf{radio}).",
            font_size=24,
            tex_environment="flushleft"
        ).next_to(titulo, DOWN, buff=0.5).to_edge(LEFT)
        self.play(Write(definicion))
        self.wait(3)

        # Dibujar plano cartesiano
        plano = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-3, 3, 1],
            background_line_style={"stroke_opacity": 0.3},
            axis_config={"include_tip": True},
        ).scale(1.2).to_edge(DOWN, buff=1)
        self.play(Create(plano))
        self.wait(1)

        # Centro O(h,k)
        h, k = 1, 0.5
        centro = Dot(plano.coords_to_point(h, k), color=RED)
        etiqueta_centro = MathTex("O(h, k)").next_to(centro, UP + RIGHT, buff=0.1).set_color(RED)
        self.play(FadeIn(centro), Write(etiqueta_centro))
        self.wait(1)

        # Radio r
        r = 2.5
        circunferencia = Circle(radius=r * plano.x_axis.unit_size, color=BLUE)
        circunferencia.move_to(plano.coords_to_point(h, k))
        self.play(Create(circunferencia))
        self.wait(1)

        # Radio como segmento
        punto_circ = Dot(plano.coords_to_point(h + r, k), color=GREEN)
        etiqueta_radio = MathTex("r").set_color(GREEN)
        etiqueta_radio.next_to(plano.coords_to_point(h + r/2, k), UP)
        segmento_radio = Line(centro.get_center(), punto_circ.get_center(), color=GREEN)
        self.play(FadeIn(punto_circ), Create(segmento_radio), Write(etiqueta_radio))
        self.wait(2)

        # Teorema y ecuación
        teorema = Text("Teorema:", font_size=36).to_edge(LEFT).shift(3*UP)
        self.play(ReplacementTransform(definicion, teorema))
        self.wait(1)

        ecuacion = MathTex(
            r"(x - h)^2 + (y - k)^2 = r^2",
            font_size=36
        ).next_to(teorema, DOWN, buff=0.5).to_edge(LEFT)
        self.play(Write(ecuacion))
        self.wait(3)

        # Resaltar centro y radio en la ecuación
        centro_eq = MathTex(r"h, k", font_size=28).set_color(RED)
        centro_eq.move_to(ecuacion.get_part_by_tex("h").get_center())
        radio_eq = MathTex(r"r", font_size=28).set_color(GREEN)
        radio_eq.move_to(ecuacion.get_part_by_tex("r").get_center())
        self.play(
            FadeIn(centro_eq),
            FadeIn(radio_eq)
        )
        self.wait(3)