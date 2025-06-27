from manim import *

class Circunferencia(Scene):
    def construct(self):
        # Escena 1: Punto central y líneas radiales
        self.play_initial_scene()

    def play_initial_scene(self):
        """
        Crea un plano, un punto central y emite líneas punteadas desde el punto.
        """

        # 1. Plano bidimensional blanco
        plano = NumberPlane()
        self.add(plano)  # No animamos la aparición del plano para simplificar.  Podríamos usar Create(plano) si fuera necesario.

        # 2. Punto rojo brillante en el centro
        punto_rojo = Dot(ORIGIN, color=RED, radius=0.08)  # Radio ajustado para mejor visualización
        self.play(Create(punto_rojo), run_time=1)

        # 3. Líneas punteadas emergiendo del punto rojo
        num_lineas = 20
        lineas = VGroup()
        for i in range(num_lineas):
            angulo = i * 2 * PI / num_lineas
            direccion = np.array([np.cos(angulo), np.sin(angulo), 0])
            linea = DashedLine(start=ORIGIN, end=5 * direccion, color=GRAY, dash_length=0.2) # Longitud y espaciado ajustados
            lineas.add(linea)

        self.play(Create(lineas, lag_ratio=0.1), run_time=2) # Animación escalonada para la creación de las líneas
        self.wait(0.5)

        # 4. Pulsación suave del punto rojo
        self.play(
            punto_rojo.animate.scale(1.2).set_opacity(0.8),  # Aumenta tamaño y transparencia para efecto de brillo
            run_time=0.7,
            rate_func=there_and_back
        )

        # 5. Oscurecimiento ligero alrededor de las líneas
        self.play(plano.animate.set_opacity(0.5), run_time=1)

        self.wait(1) # Pausa final para visualizar la escena
