#Dio error 

from manim import *

class Escena4(Scene):
    def construct(self):
        # Definición de colores
        COLOR_CIRCUNFERENCIA = BLUE_A  # Cambiado a BLUE_A para consistencia
        COLOR_EJES = YELLOW_A
        COLOR_RADIO = ORANGE
        COLOR_ETIQUETA_RADIO = WHITE

        # Creación de la circunferencia
        circunferencia = Circle(radius=2, color=COLOR_CIRCUNFERENCIA)
        centro = Dot(color=WHITE)

        # Creación de los ejes
        eje_x = Line(start=5 * LEFT, end=5 * RIGHT, color=COLOR_EJES)
        eje_y = Line(start=5 * DOWN, end=5 * UP, color=COLOR_EJES)

        # Creación inicial de la flecha (radio)
        radio = Line(start=centro.get_center(), end=circunferencia.get_center(), color=COLOR_RADIO, stroke_width=3)
        flecha = Arrow(start=centro.get_center(), end=radio.get_end(), buff=0, color=COLOR_RADIO, stroke_width=3)
        label_r = Tex("r", color=COLOR_ETIQUETA_RADIO).next_to(flecha, UP, buff=0.1)

        # Animación de la flecha
        self.play(Create(circunferencia), Create(centro), Create(eje_x), Create(eje_y))
        self.play(Create(flecha), Write(label_r))
        self.wait(0.5)

        # Animación de "rebote" de la flecha y engrosamiento
        original_end = flecha.get_end()
        new_end = original_end + 0.2 * normalize(original_end - centro.get_center()) # Extender ligeramente

        self.play(
            flecha.animate.become(Arrow(start=centro.get_center(), end=new_end, buff=0, color=COLOR_RADIO, stroke_width=6)),
            label_r.animate.next_to(Arrow(start=centro.get_center(), end=new_end, buff=0, color=COLOR_RADIO), UP, buff=0.1),
            rate_func=rate_functions.ease_in_out_sine
        )
        self.wait(0.3)

        self.play(
            flecha.animate.become(Arrow(start=centro.get_center(), end=original_end, buff=0, color=COLOR_RADIO, stroke_width=3)),
            label_r.animate.next_to(Arrow(start=centro.get_center(), end=original_end, buff=0, color=COLOR_RADIO), UP, buff=0.1),
            rate_func=rate_functions.ease_in_out_sine
        )

        self.wait(1)

        # Alejar la cámara
        self.play(
            self.camera_frame.animate.scale(1.2)
        )

        self.wait(2)