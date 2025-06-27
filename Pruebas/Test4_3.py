from manim import *

class CircunferenciaConEjes(Scene):
    def construct(self):
        # Circunferencia celeste
        circunferencia = Circle(radius=2, color=BLUE_E, stroke_width=3)
        self.play(Create(circunferencia))
        self.wait(0.5)

        # Eliminar punto rojo anterior (si existía)
        # Aunque la escena anterior no lo muestra, se incluye para robustez
        punto_rojo = Dot(color=RED)
        self.play(FadeOut(punto_rojo))


        # Ejes perpendiculares amarillos
        eje_x = Line(start=circunferencia.get_left() + LEFT * 0.5, end=circunferencia.get_right() + RIGHT * 0.5, color=YELLOW, stroke_width=2)       
        eje_y = Line(start=circunferencia.get_bottom() + DOWN * 0.5, end=circunferencia.get_top() + UP * 0.5, color=YELLOW, stroke_width=2)   
        # Animar la aparición de los ejes
        self.play(Create(eje_x), Create(eje_y))
        self.wait(0.5)

        # Punto O en la intersección de los ejes
        punto_o = Dot(color=YELLOW, point=ORIGIN)
        # No se necesita crear el punto, ya se creó con los ejes.  Podría ser redundante.

        # Etiquetas (h) y (k)
        etiqueta_h = Tex("(h)", color=WHITE).scale(0.7).next_to(eje_x, DOWN * 0.3 + RIGHT*0.3)
        etiqueta_k = Tex("(k)", color=WHITE).scale(0.7).next_to(eje_y, LEFT * 0.3 + UP * 0.3)

        # Animar la aparición de las etiquetas
        self.play(Write(etiqueta_h), Write(etiqueta_k))
        self.wait(0.5)

        # Flecha desde el origen hasta la circunferencia
        flecha_radio = Arrow(start=ORIGIN, end=circunferencia.get_right(), color=GREEN) # Elegir un punto en la circunferencia.  Usar get_right para que sea consistente.

        # Animar la creación de la flecha
        self.play(Create(flecha_radio))
        self.wait(1)

        self.wait(2) # Mantener la escena por un momento al final
