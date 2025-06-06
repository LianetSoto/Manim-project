# from manim import *

# class IntroduccionCircunferenciaDefinicion(Scene):
#     def construct(self):
#         # Configuración del entorno
#         self.camera.background_color = WHITE

#         # Plano Cartesiano
#         plano_cartesiano = NumberPlane(
#             x_range=[-5, 5, 1],
#             y_range=[-3, 3, 1],
#             x_length=10,
#             y_length=6,
#             axis_config={"color": BLACK, "include_numbers": False, "include_ticks": False}  # Ocultar números y ticks
#         ).add_coordinates()

#         plano_cartesiano.set_axis_props({"color": BLACK})  # Color de los ejes
#         plano_cartesiano.add_updater(lambda mob, dt: mob)

#         self.add(plano_cartesiano)  # Añadir el plano aquí para que esté detrás de los ejes.

#         # Ejes X e Y
#         eje_x = Line(start=(-5, 0, 0), end=(5, 0, 0), color=BLACK, stroke_width=2)
#         eje_y = Line(start=(0, -3, 0), end=(0, 3, 0), color=BLACK, stroke_width=2)

#         self.add(eje_x, eje_y)

#         # Título
#         circunferencia_definicion_titulo = Text("Circunferencia: Definición", font="Arial", font_size=0.7, color=BLACK).move_to(UP * 2.5)
#         self.play(FadeIn(circunferencia_definicion_titulo, run_time=0.5, rate_func=linear))

#         # Punto O(h, k)
#         punto_o = Dot(point=(1, 0.5, 0), color=RED, radius=0.1)
#         label_punto_o = Text("O(h, k)", font="Arial", font_size=0.4, color=RED).next_to(punto_o, UR, buff=0.1)
#         self.play(FadeIn(punto_o, run_time=0.3, rate_func=ease_in), FadeIn(label_punto_o, run_time=0.3, rate_func=ease_in))
#         self.wait(0.7)

#         # Punto P(x, y)
#         punto_p = Dot(point=(3, 1.5, 0), color=BLUE, radius=0.08)
#         label_punto_p = Text("P(x, y)", font="Arial", font_size=0.4, color=BLUE).next_to(punto_p, UR, buff=0.1)
#         self.play(FadeIn(punto_p, run_time=0.3, rate_func=ease_in), FadeIn(label_punto_p, run_time=0.3, rate_func=ease_in))
#         self.wait(0.7)

#         # Radio OP
#         radio_op = Line(start=(1, 0.5, 0), end=(3, 1.5, 0), color=GREEN, stroke_width=2)
#         label_radio = Text("r", font="Arial", font_size=0.5, color=GREEN).move_to(radio_op.get_center() + DOWN * 0.1 + LEFT * 0.1)

#         self.play(Create(radio_op, run_time=0.5, rate_func=linear), FadeIn(label_radio, run_time=0.3, rate_func=ease_in))
#         self.wait(0.5)

#         # Circunferencia
#         radio_value = 2.236  # Distancia entre O y P (aproximada)
#         circunferencia = Circle(radius=radio_value, color=YELLOW, stroke_width=2, fill_opacity=0.5).move_to((1, 0.5, 0))
#         self.play(Create(circunferencia, run_time=1, rate_func=smooth))
#         self.wait(1)

#         # Texto de Definición
#         definicion_texto = Tex(
#             "Definición: Llamaremos circunferencia al lugar geométrico de todos los puntos cuya distancia a un punto fijo del plano O(h, k)\n(denominado centro) es igual a una constante r (denominada radio).",
#             font_size=0.5,
#             color=BLACK
#         ).move_to(DOWN * 1.5)

#         self.play(Write(definicion_texto, run_time=1, rate_func=linear))
#         self.wait(5)

# from manim import *

# class IntroduccionCircunferenciaDefinicion(Scene):
#     def construct(self):
#         # Configuración del entorno
#         self.camera.background_color = WHITE
#         plano_cartesiano = Axes(
#             x_range=[-5, 5, 1],
#             y_range=[-3, 3, 1],
#             axis_config={"color": BLACK, "stroke_width": 2},
#             tips=False
#         )
#         # #plano_cartesiano.add_coordinates()  # Eliminar si causa problemas
#         # plano_cartesiano.create_grid(color=GRAY, stroke_width=0.5)
#         # self.add(plano_cartesiano)

#         # Título
#         circunferencia_definicion_titulo = Text("Circunferencia: Definición", font="Arial", font_size=30, color=BLACK).move_to(UP * 2.5) # Ajuste tamaño y uso de UP
#         self.play(FadeIn(circunferencia_definicion_titulo, run_time=0.5, rate_func=linear))

#         # Punto O(h, k)
#         punto_o = Dot(point=[1, 0.5, 0], color=RED, radius=0.1)
#         label_punto_o = Text("O(h, k)", font="Arial", font_size=20, color=RED).next_to(punto_o, RIGHT + UP, buff=0.1) #Ajuste tamaño
#         self.play(FadeIn(punto_o, run_time=0.3, rate_func= rate_functions.ease_in), FadeIn(label_punto_o, run_time=0.3, rate_func=ease_in))        
#         self.wait(0.7)

#         # Punto P(x, y)
#         punto_p = Dot(point=[3, 1.5, 0], color=BLUE, radius=0.08)
#         label_punto_p = Text("P(x, y)", font="Arial", font_size=20, color=BLUE).next_to(punto_p, RIGHT + UP, buff=0.1) #Ajuste tamaño
#         self.play(FadeIn(punto_p, run_time=0.3, rate_func= rate_functions.ease_in), FadeIn(label_punto_p, run_time=0.3, rate_func=ease_in))        
#         self.wait(0.7)

#         # Radio OP
#         radio_op = Line(start=[1, 0.5, 0], end=[3, 1.5, 0], color=GREEN, stroke_width=2)
#         label_radio = Text("r", font="Arial", font_size=25, color=GREEN).move_to([2, 1, 0]) #Ajuste tamaño
#         self.play(Create(radio_op, run_time=0.5, rate_func=linear), FadeIn(label_radio, run_time=0.3, rate_func=ease_in))  
#         self.wait(0.5)

#         # Circunferencia
#         radio_value = np.sqrt((3-1)**2 + (1.5-0.5)**2) # Calcula el radio correcto
#         circunferencia = Circle(radius=radio_value, color=YELLOW, stroke_width=2, fill_opacity=0.5).move_to([1, 0.5, 0])   
#         self.play(Create(circunferencia, run_time=1, rate_func=smooth))
#         self.wait(1)

#         # Definición de la circunferencia (texto)
#         definicion_texto = Text("Definición: Llamaremos circunferencia al lugar geométrico de todos los puntos cuya distancia a un punto fijo del plano O(h, k)(denominado centro) es igual a una constante r (denominada radio).",
#                                 font="Arial", font_size=25, color=BLACK,  wrap_width=8).move_to(DOWN * 1.5) #Ajuste tamaño y ajuste de linea
#         self.play(Write(definicion_texto, run_time=3, rate_func=linear)) #Aumente el tiempo
#         self.wait(4)

from manim import *

class IntroduccionCircunferenciaDefinicion(Scene):
    def construct(self):
        # Configuración general
        self.camera.background_color = WHITE

        # Plano Cartesiano
        plano_cartesiano = Axes(
            x_range=[-5, 5, 1],
            y_range=[-3, 3, 1],
            axis_config={"color": BLACK, "stroke_width": 2},
            x_axis_config={"numbers_to_include": range(-5, 6, 1)},
            y_axis_config={"numbers_to_include": range(-3, 4, 1)}
        )

        # Agrega lineas de grilla
        plano_cartesiano.add_coordinates()

        # Configuración de las líneas de la grilla
        plano_cartesiano.get_axis_lines().set_color(LIGHT_GRAY).set_stroke(width=0.5)

        # Ejes X e Y
        eje_x = Line(start=[-5, 0, 0], end=[5, 0, 0], color=BLACK, stroke_width=2)
        eje_y = Line(start=[0, -3, 0], end=[0, 3, 0], color=BLACK, stroke_width=2)

        # Título
        circunferencia_definicion_titulo = Text("Circunferencia: Definición", font="Arial", font_size=36, color=BLACK).move_to([0, 2.5, 0])

        # Punto O(h, k)
        h = 1
        k = 0.5
        punto_o = Dot([h, k, 0], color=RED, radius=0.1)
        label_punto_o = Text("O(h, k)", font="Arial", font_size=24, color=RED).next_to(punto_o, RIGHT + UP, buff=0.1)      

        # Punto P(x, y)
        x = 3
        y = 1.5
        punto_p = Dot([x, y, 0], color=BLUE, radius=0.08)
        label_punto_p = Text("P(x, y)", font="Arial", font_size=24, color=BLUE).next_to(punto_p, RIGHT + UP, buff=0.1)     

        # Radio OP
        radio_op = Line(start=[h, k, 0], end=[x, y, 0], color=GREEN, stroke_width=2)
        label_radio = Text("r", font="Arial", font_size=30, color=GREEN).move_to([(h + x) / 2, (k + y) / 2, 0])

        # Circunferencia
        radio_valor = np.sqrt((x - h)**2 + (y - k)**2)
        circunferencia = Circle(radius=radio_valor, color=YELLOW, stroke_width=2, fill_opacity=0.5).move_to([h, k, 0])     

        # Definición de la circunferencia
        definicion_texto = Text(
            "Definición: Llamaremos circunferencia al lugar geométrico de todos los puntos cuya distancia a un punto fijo del plano O(h, k) \n (denominado centro) es igual a una constante r (denominada radio).",
            font="Arial",
            font_size=24,
            color=BLACK,
            justify=LEFT
        ).move_to([0, -1.5, 0])

        # Animaciones
        self.play(FadeIn(circunferencia_definicion_titulo), run_time=0.5)
        self.wait(0.5)

        self.add(plano_cartesiano)

        self.play(FadeIn(punto_o), FadeIn(label_punto_o), run_time=0.3, rate_func=ease_in)
        self.wait(0.7)

        self.play(FadeIn(punto_p), FadeIn(label_punto_p), run_time=0.3, rate_func=ease_in)
        self.wait(0.7)

        self.play(Create(radio_op), FadeIn(label_radio), run_time=0.5)
        self.wait(0.5)

        self.play(Create(circunferencia), run_time=1, rate_func=smooth)
        self.wait(1)

        self.play(Write(definicion_texto), run_time=1)
        self.wait(4)

        self.wait(1) # Tiempo extra al final
