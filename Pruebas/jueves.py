from manim import *

class IntroduccionCircunferenciaDefinicion(Scene):
    def construct(self):
        # Configuración del fondo
        self.camera.background_color = WHITE

        # Plano Cartesiano
        plano_cartesiano = Axes(
            x_range=[-5, 5, 1],
            y_range=[-3, 3, 1],
            axis_config={"color": BLACK, "stroke_width": 2},
            tips=False
        )
        plano_cartesiano.add_coordinates()
        plano_cartesiano.x_axis.set_color(BLACK)
        plano_cartesiano.y_axis.set_color(BLACK)

        # # Grilla del plano cartesiano
        # plano_cartesiano.get_axis_lines().set_color(GRAY_D)
        # plano_cartesiano.get_axis_lines().set_stroke(width=1)

        # Título
        circunferencia_definicion_titulo = Text("Circunferencia: Definición", font="Arial", font_size=40, color=BLACK)     
        circunferencia_definicion_titulo.move_to(UP * 2.5)

        # Punto O (h, k)
        h = 1
        k = 0.5
        punto_o = Dot([h, k, 0], color=RED, radius=0.1)
        label_punto_o = Text("O(h, k)", font="Arial", font_size=25, color=RED).next_to(punto_o, UR, buff=0.1)

        # Punto P (x, y)
        x = 3
        y = 1.5
        punto_p = Dot([x, y, 0], color=BLUE, radius=0.08)
        label_punto_p = Text("P(x, y)", font="Arial", font_size=25, color=BLUE).next_to(punto_p, UR, buff=0.1)

        # Radio OP
        radio_op = Line([h, k, 0], [x, y, 0], color=GREEN, stroke_width=2)
        label_radio = Text("r", font="Arial", font_size=30, color=GREEN).move_to((punto_o.get_center() + punto_p.get_center())/2)

        # Circunferencia
        radio_value = np.sqrt((x - h)**2 + (y - k)**2)
        circunferencia = Circle(radius=radio_value, color=YELLOW, stroke_width=2, fill_opacity=0.5).move_to([h, k, 0])     

        # Definición textual
        definicion = Text("Definición: Llamaremos circunferencia al lugar geométrico de todos los puntos cuya distancia a un punto fijo del plano O(h, k)\n(denominado centro) es igual a una constante r (denominada radio).",
                         font="Arial", font_size=25, color=BLACK,  t2c={'O(h, k)': RED, 'r': GREEN}).move_to(DOWN * 1.5)   

        # Animaciones
        self.play(FadeIn(circunferencia_definicion_titulo), run_time=0.5)
        self.wait(0.5)

        self.add(plano_cartesiano)

        self.play(FadeIn(punto_o), FadeIn(label_punto_o), run_time=0.3)
        self.wait(0.7)

        self.play(FadeIn(punto_p), FadeIn(label_punto_p), run_time=0.3)
        self.wait(0.7)

        self.play(Create(radio_op), FadeIn(label_radio), run_time=0.5)
        self.wait(0.5)

        self.play(Create(circunferencia), run_time=1)
        self.wait(1)

        self.play(Write(definicion), run_time=1)
        self.wait(4)