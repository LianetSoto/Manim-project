from manim import *

class CircunferenciaConCentroHK(Scene):
    def construct(self):
        # Configuración de colores
        COLOR_CIRCUNFERENCIA = BLUE_A  # Celeste brillante
        COLOR_EJES = YELLOW_A  # Amarillo brillante
        COLOR_FLECHA = ORANGE  # Naranja
        COLOR_HK = WHITE  # Blanco

        # 1. Circunferencia y Ejes
        circulo = Circle(radius=2, color=COLOR_CIRCUNFERENCIA)
        ejes = VGroup(
            NumberLine(x_range=[-3, 3, 1], color=COLOR_EJES, include_numbers=True),
            NumberLine(x_range=[-3, 3, 1], color=COLOR_EJES, include_numbers=True).rotate(PI / 2)
        )

        # 2. Flecha (Radio)
        radio_vector = Vector(direction=RIGHT, buff=0).scale(2).set_color(COLOR_FLECHA)
        radio_vector.shift(circulo.get_center())
        texto_radio = MathTex("r", color=COLOR_FLECHA).next_to(radio_vector, UP, buff=0.1)

        # 3. Punto O -> (h, k)
        punto_o = Dot(point=ORIGIN, color=WHITE)
        texto_o = MathTex("O", color=WHITE).next_to(punto_o, DOWN, buff=0.1)

        self.play(Create(circulo), Create(ejes))
        self.play(Create(punto_o), Write(texto_o))
        self.play(Create(radio_vector), Write(texto_radio))
        self.wait(1)

        # 4. Transformación O -> (h, k)
        punto_hk = Dot(point=[1, 1, 0], color=COLOR_HK) # Desplazamos el punto O
        texto_hk = MathTex("(h, k)", color=COLOR_HK).next_to(punto_hk, DOWN, buff=0.1)

        # Mover y actualizar la flecha del radio
        radio_vector_nuevo = Vector(direction=RIGHT, buff=0).scale(2).set_color(COLOR_FLECHA)
        radio_vector_nuevo.shift(punto_hk.get_center())  # El radio parte del nuevo centro (h, k)

        # Animación para mover la flecha
        def update_radio(obj):
            obj.become(Vector(direction=RIGHT, buff=0).scale(2).set_color(COLOR_FLECHA).shift(punto_hk.get_center()))

        self.play(
            Transform(punto_o, punto_hk),
            Transform(texto_o, texto_hk),
            UpdateFromFunc(radio_vector, update_radio),  # Animación continua del radio
            run_time=2
        )

        self.wait(1)

        # 5. Iluminación de h y k (Desplazamiento en el eje)
        h_line = DashedLine(start=punto_hk.get_center(), end=[punto_hk.get_x(), 0, 0], color=COLOR_HK)
        k_line = DashedLine(start=punto_hk.get_center(), end=[0, punto_hk.get_y(), 0], color=COLOR_HK)

        h_text = MathTex("h", color=COLOR_HK).next_to(h_line.get_end(), DOWN, buff=0.1)
        k_text = MathTex("k", color=COLOR_HK).next_to(k_line.get_end(), LEFT, buff=0.1)

        self.play(Create(h_line), Write(h_text))
        self.wait(0.5)
        self.play(Create(k_line), Write(k_text))
        self.wait(1)

        # 6. Desaparición gradual, dejando solo la circunferencia
        self.play(
            FadeOut(ejes),
            FadeOut(punto_hk),
            FadeOut(texto_hk),
            FadeOut(radio_vector),
            FadeOut(texto_radio),
            FadeOut(h_line),
            FadeOut(k_line),
            FadeOut(h_text),
            FadeOut(k_text),
            run_time=2
        )
        self.wait(1)