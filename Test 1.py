from AbstracClass import GeminiLLM

llm = GeminiLLM("AIzaSyCSWVPAhOYUXhjSslvBZDWk9D7BI1tA8Bg")
# escenes = llm.query("""Analiza el siguiente texto y divídelo en escenas discretas, separando cada escena con el delimitador "=====". Para cada escena, identifica los objetos principales y sus propiedades relevantes para una visualización en video con Manim.

# Para cada objeto, especifica:

# *   **Nombre del objeto:** (Ej: Circulo, Cuadrado, Texto).
# *   **Propiedades:** (Ej: color=RED, radio=2, relleno=True, texto="Hola Mundo", font_size=48). Incluye posición inicial (coordenadas x, y, z), tamaño (alto, ancho, radio), color, transparencia, relleno (True/False), grosor de línea (stroke_width), fuente (para texto), alineación (para texto), etc. Ajusta las propiedades para que los objetos sean visualmente distintos y no se solapen.
# *   **Animación:** Describe cómo y cuándo debe aparecer y moverse el objeto en la escena. Especifica el tipo de animación (Ej: Create, FadeIn, Transform, MoveTo, Rotate, Write, DrawBorderThenFill). Incluye la duración de la animación en segundos 
# y cualquier parámetro adicional necesario (Ej: angle=PI/2, run_time=2, rate_func=linear). Asegúrate de que las animaciones 
# sean fluidas y visualmente atractivas.
# *   **Tiempo en pantalla:** Indica durante cuántos segundos debe permanecer visible el objeto en la escena después de su animación.
# *   **Transición de salida:** Describe cómo debe desaparecer el objeto de la pantalla (Ej: FadeOut, ShiftOffScreen). Incluye la duración de la transición y cualquier parámetro adicional.

# Considera la narrativa del texto al determinar la secuencia de las escenas y las animaciones de los objetos. Asegúrate de que cada escena tenga un objetivo claro y que las animaciones apoyen la comprensión del texto.

# A continuación, el texto a analizar:
#  Circunferencia Definición y Caracterización Definición: Llamaremos circunferencia al lugar geométrico de todos los puntos cuya distancia a un punto fijo del plano O(h, k)"
# "(denominado centro) es igual a una constante r (denominada radio). TEOREMA: La circunferencia con centro en O(h, k) y radio r, denotada por C(O,r) tiene por ecuación, （C ーh)^2 ＋（Y-K)^2 = r""")

# #print(escenes)

generarCodigo = """dado el siguiente texto, genera el codigo manim para realizar un video (haciendo uso de la documentacion oficial de manim como guia), ten en cuenta los detalles, incluye las importaciones necesarias, ademas, asegurate de incluir todas las escenas en el video:
Escena 1: Introducción al Concepto de Circunferencia

*   **Nombre del objeto:** Texto "Circunferencia"
    *   **Propiedades:** texto="Circunferencia", font_size=72, color=BLUE, posicion=[0, 3, 0]
    *   **Animación:** Write, run_time=2
    *   **Tiempo en pantalla:** 2
    *   **Transición de salida:** FadeOut, run_time=1

*   **Nombre del objeto:** Texto "Definición y Caracterización"
    *   **Propiedades:** texto="Definición y Caracterización", font_size=36, color=GREEN, posicion=[0, 1.5, 0]
    *   **Animación:** FadeIn, run_time=1
    *   **Tiempo en pantalla:** 2
    *   **Transición de salida:** FadeOut, run_time=1
$$$
Escena 2: Definición de Circunferencia (Parte 1)

*   **Nombre del objeto:** Texto "Definición:"
    *   **Propiedades:** texto="Definición:", font_size=48, color=YELLOW, posicion=[-4, 0, 0], anchor=LEFT
    *   **Animación:** Write, run_time=1.5
    *   **Tiempo en pantalla:** 1
    *   **Transición de salida:** FadeOut, run_time=0.5

*   **Nombre del objeto:** Texto "Llamaremos circunferencia al lugar geométrico de todos los puntos cuya distancia a un punto fijo del plano"
    *   **Propiedades:** texto="Llamaremos circunferencia al lugar geométrico de todos los puntos cuya distancia a un punto fijo del plano", font_size=24, color=WHITE, posicion=[-2, -1, 0], anchor=LEFT
    *   **Animación:** Write, run_time=3
    *   **Tiempo en pantalla:** 2
    *   **Transición de salida:** FadeOut, run_time=0.5

$$$
Escena 3: Definición de Circunferencia (Parte 2)

*   **Nombre del objeto:** Texto "O(h, k)"
    *   **Propiedades:** texto="O(h, k)", font_size=36, color=RED, posicion=[2, -1, 0], anchor=LEFT
    *   **Animación:** Write, run_time=1
    *   **Tiempo en pantalla:** 2
    *   **Transición de salida:** FadeOut, run_time=0.5

*   **Nombre del objeto:** Texto "(denominado centro) es igual a una constante r"
    *   **Propiedades:** texto="(denominado centro) es igual a una constante r", font_size=24, color=WHITE, posicion=[-2, -2, 0], anchor=LEFT
    *   **Animación:** Write, run_time=2
    *   **Tiempo en pantalla:** 2
    *   **Transición de salida:** FadeOut, run_time=0.5

$$$
Escena 4: Definición de Circunferencia (Parte 3)

*   **Nombre del objeto:** Texto "(denominada radio)."
    *   **Propiedades:** texto="(denominada radio).", font_size=24, color=WHITE, posicion=[-2, -3, 0], anchor=LEFT
    *   **Animación:** Write, run_time=1
    *   **Tiempo en pantalla:** 2
    *   **Transición de salida:** FadeOut, run_time=0.5

$$$
Escena 5: Teorema de la Ecuación de la Circunferencia

*   **Nombre del objeto:** Texto "TEOREMA:"
    *   **Propiedades:** texto="TEOREMA:", font_size=48, color=YELLOW, posicion=[-4, 1, 0], anchor=LEFT
    *   **Animación:** Write, run_time=1
    *   **Tiempo en pantalla:** 1
    *   **Transición de salida:** FadeOut, run_time=0.5

*   **Nombre del objeto:** Texto "La circunferencia con centro en O(h, k) y radio r, denotada por C(O,r)"
    *   **Propiedades:** texto="La circunferencia con centro en O(h, k) y radio r, denotada por C(O,r)", font_size=24, color=WHITE, posicion=[-2, 0, 0], anchor=LEFT
    *   **Animación:** Write, run_time=3
    *   **Tiempo en pantalla:** 2
    *   **Transición de salida:** FadeOut, run_time=0.5

$$$
Escena 6: Ecuación de la Circunferencia

*   **Nombre del objeto:** Texto "tiene por ecuación:"
    *   **Propiedades:** texto="tiene por ecuación:", font_size=24, color=WHITE, posicion=[-2, -1, 0], anchor=LEFT
    *   **Animación:** Write, run_time=1
    *   **Tiempo en pantalla:** 1
    *   **Transición de salida:** FadeOut, run_time=0.5

*   **Nombre del objeto:** Texto "(x - h)^2 + (y - k)^2 = r^2"
    *   **Propiedades:** texto="(x - h)^2 + (y - k)^2 = r^2", font_size=36, color=GREEN, posicion=[0, -2, 0]
    *   **Animación:** Write, run_time=3
    *   **Tiempo en pantalla:** 3
    *   **Transición de salida:** FadeOut, run_time=1"""

codigo = llm.query(generarCodigo)
print(codigo)
