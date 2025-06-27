from manim import *

class CircleExplainer(Scene):
    def construct(self):
        # Configuración general
        self.camera.background_color = BLACK
        dot_color = YELLOW
        radius_color = GREEN
        circle_color = BLUE
        axes_color = WHITE

        # Escena 1: Origen del Concepto
        self.play_scene_1(dot_color)
        self.wait(1)

        # Escena 2: El Rastro de la Distancia Constante
        self.play_scene_2(dot_color, radius_color, circle_color)
        self.wait(1)

        # Escena 3: Llenado y Definición de la Circunferencia
        self.play_scene_3(circle_color)
        self.wait(1)

        # Escena 4: Representación Gráfica del Radio y Centro
        self.play_scene_4(dot_color, radius_color, axes_color)
        self.wait(1)

        # Escena 5: Visualización Dinámica de la Ecuación
        self.play_scene_5(radius_color)
        self.wait(2)


    def play_scene_1(self, dot_color):
        # Espacio vacío
        self.camera.background_color = BLACK
        # Punto O(h,k)
        origin_point = Dot(ORIGIN, color=dot_color)
        origin_point.set_z_index(1)  # Asegura que el punto esté al frente
        aura = Circle(radius=0.5, color=dot_color, fill_opacity=0.1).move_to(ORIGIN) #Aura sutil
        self.play(Create(origin_point), Create(aura))
        self.play(origin_point.animate.scale(1.5).set_color(RED), run_time=0.5)
        self.play(origin_point.animate.scale(2/3).set_color(dot_color), run_time=0.5)
        self.add(origin_point) # Asegura que el punto permanece en la escena
        self.origin_point = origin_point #Guardamos el punto para usarlo en otras escenas
        self.aura = aura

        # Label O(h,k)
        origin_label = MathTex("O(h, k)", color=dot_color).next_to(origin_point, DR, buff=0.1)
        self.play(Write(origin_label))
        self.origin_label = origin_label


    def play_scene_2(self, dot_color, radius_color, circle_color):
        # Radio 'r' extendiéndose
        radius = Line(self.origin_point.get_center(), self.origin_point.get_center() + RIGHT*3, color=radius_color)
        self.radius = radius
        self.play(Create(radius))

        # Huella del círculo
        circle = Circle(radius=3, color=circle_color, stroke_width=2).move_to(self.origin_point.get_center())

        self.play(
            Rotate(
                radius,
                angle=2*PI,
                about_point=self.origin_point.get_center(),
                run_time=4,
                rate_func=linear
            )
        )
        self.play(Create(circle), run_time=1)
        self.circle = circle

    def play_scene_3(self, circle_color):
        # Llenado y definición de la circunferencia
        num_points = 200
        points = []
        for i in range(num_points):
            angle = i * 2 * PI / num_points
            x = 3 * np.cos(angle)
            y = 3 * np.sin(angle)
            points.append([x, y, 0])

        dots = VGroup(*[Dot(point, color=circle_color, radius=0.02) for point in points])
        dots.move_to(self.origin_point.get_center())
        self.play(Transform(self.circle, dots), run_time = 2)
        self.remove(self.circle)
        self.circle = dots #Actualizamos el círculo con los puntos
        self.add(self.circle)


    def play_scene_4(self, dot_color, radius_color, axes_color):
        # Sistema de coordenadas
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            axis_config={"color": axes_color, "stroke_width": 1}
        )
        axes.move_to(ORIGIN)

        x_label = axes.get_x_axis_label("x")
        y_label = axes.get_y_axis_label("y")

        self.play(Create(axes), Create(x_label), Create(y_label))
        self.axes = axes
        self.x_label = x_label
        self.y_label = y_label

        # Mover el círculo y el punto al centro
        self.play(
            self.circle.animate.move_to(axes.get_origin()),
            self.origin_point.animate.move_to(axes.get_origin())
        )

        #Posicionar O(h,k) en las coordenadas (h,k)
        h = 2
        k = 1
        self.play(
            self.origin_point.animate.move_to(axes.c2p(h,k))
        )
        self.h = h
        self.k = k

        # Radio 'r'
        radius_line = Line(axes.c2p(h, k), axes.c2p(h+3, k), color=radius_color)
        r_label = MathTex("r", color=radius_color).next_to(radius_line, UP, buff=0.1)

        self.play(Create(radius_line), Write(r_label))
        self.radius_line = radius_line
        self.r_label = r_label

        # Punto en la circunferencia
        circumference_point = Dot(axes.c2p(h+3, k), color=YELLOW)
        self.play(Create(circumference_point))
        self.wait(0.5)
        self.play(FadeOut(circumference_point))
        self.circumference_point = circumference_point

    def play_scene_5(self, radius_color):
        # (x - h)
        x = 4
        x_minus_h = abs(x - self.h) #Valor absoluto para evitar problemas de dirección
        x_minus_h_line = Line(self.axes.c2p(self.h, self.k), self.axes.c2p(x, self.k), color=radius_color)
        x_minus_h_label = MathTex("x - h", color=radius_color).next_to(x_minus_h_line, DOWN, buff=0.1)
        self.play(Create(x_minus_h_line), Write(x_minus_h_label))
        self.x_minus_h_line = x_minus_h_line
        self.x_minus_h_label = x_minus_h_label

        # (y - k)
        y = self.k + np.sqrt(3**2 - x_minus_h**2) #Nos aseguramos que el punto este en la circunferencia
        y_minus_k = abs(y - self.k) #Valor absoluto
        y_minus_k_line = Line(self.axes.c2p(x, self.k), self.axes.c2p(x, y), color=radius_color)
        y_minus_k_label = MathTex("y - k", color=radius_color).next_to(y_minus_k_line, RIGHT, buff=0.1)
        self.play(Create(y_minus_k_line), Write(y_minus_k_label))
        self.y_minus_k_line = y_minus_k_line
        self.y_minus_k_label = y_minus_k_label

        # Cuadrados
        x_minus_h_square = Square(side_length=x_minus_h_line.get_length(), color=BLUE, fill_opacity=0.5).move_to(self.x_minus_h_line.get_center()).shift(DOWN*(x_minus_h_line.get_length()/2)).shift(LEFT*(x_minus_h_line.get_length()/2))
        y_minus_k_square = Square(side_length=y_minus_k_line.get_length(), color=GREEN, fill_opacity=0.5).move_to(self.y_minus_k_line.get_center()).shift(RIGHT*(y_minus_k_line.get_length()/2)).shift(DOWN*(y_minus_k_line.get_length()/2))

        self.play(Create(x_minus_h_square), Create(y_minus_k_square))
        self.x_minus_h_square = x_minus_h_square
        self.y_minus_k_square = y_minus_k_square

        # Círculo de radio 'r'
        r_squared_circle = Circle(radius=self.radius_line.get_length(), color=YELLOW, fill_opacity=0.3).move_to(self.axes.get_origin()).shift(LEFT * 4)
        r_squared_label = MathTex("r^2", color=YELLOW).next_to(r_squared_circle, UP, buff=0.1)
        self.play(Create(r_squared_circle), Write(r_squared_label))
        self.r_squared_circle = r_squared_circle
        self.r_squared_label = r_squared_label

        # Suma de los cuadrados
        sum_area = x_minus_h_square.get_area() + y_minus_k_square.get_area()
        self.wait(1)

        # Mover los cuadrados
        self.play(
            x_minus_h_square.animate.move_to(r_squared_circle.get_center()).scale(np.sqrt(r_squared_circle.get_area() / (x_minus_h_square.get_area() + y_minus_k_square.get_area()))),
            y_minus_k_square.animate.move_to(r_squared_circle.get_center()).scale(np.sqrt(r_squared_circle.get_area() / (x_minus_h_square.get_area() + y_minus_k_square.get_area())))
        )

        self.wait(1)

        # Desvanecer
        self.play(FadeOut(self.x_minus_h_line, self.x_minus_h_label, self.y_minus_k_line, self.y_minus_k_label, self.x_minus_h_square, self.y_minus_k_square))

    def setup(self):
        # Este método se llama antes de construct()
        pass