from manim import *

class CircunferenciaExplicacion(Scene):
    def construct(self):
        # Escena 1
        titulo = Text("Circunferencia", color=WHITE, font_size=60)
        titulo.move_to(UP * 3)
        subtitulo = Text("Definicion y Caracterizacion", color=WHITE, font_size=35)
        subtitulo.move_to(UP * 2)

        self.play(FadeIn(titulo), run_time=1)
        self.wait(0.5)
        self.play(FadeIn(subtitulo), run_time=1)
        self.wait(1)
        self.play(FadeOut(titulo, subtitulo), run_time=1)
        self.wait(0.5)

        # Escena 2
        definicion_titulo = Text("Definicion:", color=WHITE, font_size=35)
        definicion_titulo.move_to(LEFT * 4 + UP * 3)
        definicion_linea1 = Text("Llamaremos circunferencia al lugar geometrico de todos los puntos cuya", color=WHITE, font_size=25)
        definicion_linea1.move_to(LEFT * 4 + UP * 2)
        definicion_linea2 = Text("distancia a un punto fijo del plano O(h, k) (denominado centro)", color=WHITE, font_size=25)
        definicion_linea2.move_to(LEFT * 4 + UP * 1.5)
        definicion_linea3 = Text("es igual a una constante r (denominada radio).", color=WHITE, font_size=25)
        definicion_linea3.move_to(LEFT * 4 + UP * 1)

        self.play(FadeIn(definicion_titulo), run_time=0.5)
        self.wait(0.25)
        self.play(FadeIn(definicion_linea1), run_time=1)
        self.wait(0.5)
        self.play(FadeIn(definicion_linea2), run_time=1)
        self.wait(0.5)
        self.play(FadeIn(definicion_linea3), run_time=1)
        self.wait(1)
        self.play(FadeOut(definicion_titulo, definicion_linea1, definicion_linea2, definicion_linea3), run_time=1)
        self.wait(0.5)

        # Escena 3
        teorema_titulo = Text("Teorema:", color=WHITE, font_size=35)
        teorema_titulo.move_to(LEFT * 4 + UP * 3)
        teorema_linea1 = Text("La circunferencia con centro en O(h, k) y radio r, denotada por", color=WHITE, font_size=25)
        teorema_linea1.move_to(LEFT * 4 + UP * 2)
        teorema_linea2 = Text("C(O, r) tiene por ecuacion,", color=WHITE, font_size=25)
        teorema_linea2.move_to(LEFT * 4 + UP * 1.5)
        ecuacion = MathTex(r"(x - h)^2 + (y - k)^2 = r^2", color=WHITE, font_size=25)
        ecuacion.move_to(LEFT * 1.7 + DOWN * 0) # Ajuste de posición

        self.play(FadeIn(teorema_titulo), run_time=0.5)
        self.wait(0.25)
        self.play(FadeIn(teorema_linea1), run_time=1)
        self.wait(0.5)
        self.play(FadeIn(teorema_linea2), run_time=1)
        self.wait(0.5)
        self.play(FadeIn(ecuacion), run_time=2)
        self.wait(2)