from AbstracClass import GeminiLLM

llm = GeminiLLM("AIzaSyCSWVPAhOYUXhjSslvBZDWk9D7BI1tA8Bg")
#GENERAR ESCENA

prompt1 = ("Actúa como un ingeniero de prompts especializado en la creación de prompts para modelos de lenguaje grandes (LLMs) enfocados en la generación de descripciones detalladas para la creación de animaciones en Manim. Tu objetivo es convertir un texto dado en un conjunto de escenas discretas, cada una con una "
"descripción exhaustiva de los objetos, sus propiedades y su comportamiento para facilitar la creación de la animación. \n\n"  

"**Instrucciones:**\n\n"

"1.  **Análisis del Texto:** Analiza el texto proporcionado e identifica las distintas escenas que lo componen. Una escena se define como un cambio significativo en el lugar, el tiempo, los personajes/objetos presentes o la acción principal.\n\n"    

"2.  **Delimitación de Escenas:** Separa cada escena con el delimitador especial \"###ESCENA###\"\n\n"

"3.  **Descripción Detallada de Cada Escena:** Para cada escena, proporciona la siguiente información:\n\n"

    "*   **Título de la Escena:** Un título breve y descriptivo de la escena.\n\n"
    "*   **Entorno:** Descripción detallada del lugar donde se desarrolla la escena (fondo, elementos estáticos, iluminación, etc.). Especifica colores, texturas y cualquier detalle visual relevante.\n\n"
    "*   **Objetos:** Lista de todos los objetos presentes en la escena, cada uno con la siguiente información:\n\n"
        "*   **Nombre del Objeto:** Identificador único para el objeto.\n\n"
        "*   **Tipo de Objeto:** (e.g., círculo, cuadrado, texto, imagen, vector, línea, etc.)\n\n"
        "*   **Propiedades:**\n\n"
            "*   **Posición Inicial:** Coordenadas (x, y, z) donde el objeto aparece inicialmente. \n\n"
            "*   **Tamaño/Escala:** Dimensiones iniciales del objeto (radio, longitud, altura, ancho, etc.)\n\n"
            "*   **Color:** Color del objeto en formato hexadecimal o nombre del color \n\n"
            "*   **Transparencia (Alpha):** Valor entre 0 y 1 que indica la transparencia del objeto (0 = completamente transparente, 1 = completamente opaco).\n\n"
            "*   **Borde:** Grosor y color del borde del objeto (si aplica).\n\n"
            "*   **Relleno:** Color del relleno del objeto (si aplica).\n\n"
            "*   **Texto (si aplica):** Contenido del texto, fuente, tamaño de la fuente, alineación.\n\n"
    "*   **Animaciones:** Descripción detallada de las animaciones que ocurren en la escena, incluyendo:\n\n"
        "*   **Objeto Afectado:** Nombre del objeto que se anima.\n\n"
        "*   **Tipo de Animación:** (e.g., Traslación, Rotación, Escala, FadeIn, FadeOut, Transformación, Cambio de Color, Escritura, etc.)\n\n"
        "*   **Duración:** Tiempo en segundos que dura la animación.\n\n"
        "*   **Interpolación:** Tipo de interpolación para la animación (e.g., linear, smooth, ease_in, ease_out, ease_in_out). \n\n"
        "*   **Parámetros:** Parámetros específicos para cada tipo de animación (e.g., vector de traslación, ángulo de rotación, factor de escala, nuevo color, etc.).\n\n"
        "*   **Tiempo de Inicio:** Tiempo en segundos desde el inicio de la escena cuando comienza la animación.\n\n"
        "*   **Tiempo de Finalización:** Tiempo en segundos desde el inicio de la escena cuando finaliza la animación. \n\n"    
    "*   **Texto en Pantalla:** Especifica cualquier texto que deba aparecer en la pantalla, su posición, fuente, tamaño y duración en pantalla.\n\n"
    "*   **Sonido (Opcional):** Si es relevante, indica el archivo de sonido a reproducir y el momento en que debe sonar.  \n\n"
    "*   **Cámara:** Movimientos de la cámara (si los hay) como paneos, zooms o rotaciones. Incluye duración y tipo de interpolación.\n\n"

"4.  **Consistencia:** Mantén la consistencia en la nomenclatura de los objetos y en las unidades de medida utilizadas. \n\n"   

"5.  **Claridad:** Sé lo más claro y preciso posible en las descripciones para que puedan ser fácilmente interpretadas y traducidas a código Manim.\n\n"

"**Texto de Entrada:** Circunferencia Definición y Caracterización Definición: Llamaremos circunferencia al lugar geométrico de todos los puntos cuya distancia a un punto fijo del plano O(h, k)"
"(denominado centro) es igual a una constante r (denominada radio). TEOREMA: La circunferencia con centro en O(h, k) y radio r, denotada por C(O,r) tiene por ecuación, （C ーh)^2 ＋（Y-K)^2 = r ")


#PROMPT PARA GENERAR PROMPT PARA GENERAR ESCENA
prompt = ("quiero pedirele a un llm que dado un texto me delimite las escenas y los objetos, con sus respectivas propiedades, para posteriormente hacer un video en manim, ayudame a realizar un buen prompt para eso, imagina que eres un ingeniero de prompts, delimita las escenas con un caracter especial para posteriormente separarlas, asimismo, especifica como deberian moverse los objetos en las escenas, el lugar, tiempo en pantalla de cada objeto y otras especificidades que podrian ser necesarias, asegurate de que los objetos no se solapen en las escenas, ademas, solo pasame el prompt, sin sugerencias u otro tipo de informacion")

b = llm.query(prompt)
print(b)

# UNA DE LAS RESPUESTAS DEL PROMPT DE ARRIBA
B = """Eres un ingeniero de prompts experto en generar descripciones detalladas para la creación de animaciones en Manim. Analizarás el texto proporcionado y generarás una descripción estructurada para cada escena, incluyendo objetos, propiedades, movimientos, tiempo en pantalla y ubicación, todo optimizado para la animación en Manim.

**Formato de Salida:**

Las escenas estarán separadas por el delimitador '####'. Dentro de cada escena, la información se organizará de la siguiente manera:

*   **Escena:** [Número de Escena]
*   **Descripción General:** [Breve resumen de la escena]
*   **Entorno:**
    *   **Fondo:** [Color, imagen o gradiente de fondo]
    *   **Lugar:** [Descripción detallada del lugar: interior/exterior, elementos distintivos, etc.]
    *   **Sonido:** [Descripción breve de la ambientación sonora, si es relevante]
*   **Objetos:**
    *   **Objeto 1:**
        *   **Tipo:** [Circle, Square, Text, Image, etc.]
        *   **Propiedades:**
            *   **Color:** [Hexadecimal o nombre de color]
            *   **Tamaño:** [Radio, lado, altura, ancho, etc. en unidades Manim]
            *   **Posición Inicial:** [Coordenadas (x, y, z) en el plano cartesiano de Manim]
            *   **Texto (si aplica):** [Contenido del texto, fuente, tamaño de fuente]
            *   **Imagen (si aplica):** [Ruta de la imagen]
        *   **Animación:**
            *   **Aparición:** [Create, FadeIn, Write, DrawBorderThenFill, etc.]
            *   **Movimiento:** [Transform, MoveTo, Shift, Rotate, GrowFromCenter, etc.]
            *   **Posición Final:** [Coordenadas (x, y, z) si hay movimiento]
            *   **Duración:** [Tiempo en segundos de la animación]
            *   **Easing Function:** [linear, ease_in, ease_out, ease_in_out, etc.]
        *   **Tiempo en Pantalla:** [Tiempo total en segundos que el objeto permanece visible]
    *   **Objeto 2:** (Repetir la estructura anterior para cada objeto en la escena)
*   **Cámara:**
    *   **Zoom:** [Nivel de zoom inicial]
    *   **Movimiento de Cámara:** [Si la cámara se mueve, descripción del movimiento y duración]
*   **Notas Adicionales:** [Cualquier instrucción o detalle adicional relevante para la implementación en Manim, por ejemplo, prevenir solapamientos, jerarquía visual, énfasis en ciertos elementos, etc.]

**Instrucciones:**

1.  **Análisis del Texto:** Lee cuidadosamente el texto proporcionado e identifica las escenas clave.
2.  **Delimitación de Escenas:** Separa cada escena con el delimitador '####'.
3.  **Descripción Detallada:** Para cada escena, completa la información en el formato especificado.  Sé preciso y conciso 
en las descripciones.
4.  **Animaciones Realistas:** Diseña animaciones fluidas y coherentes con la narrativa del texto. Considera la física básica y la percepción visual.
5.  **Optimización Manim:**  Asegúrate de que las propiedades y animaciones sean compatibles con las funciones de Manim.   
6.  **Prevención de Solapamientos:**  Considera las posiciones y tamaños de los objetos para evitar que se solapen visualmente. Ajusta las posiciones si es necesario.
7.  **Claridad Visual:** Prioriza la claridad visual y la jerarquía de la información. Utiliza colores, tamaños y animaciones para guiar la atención del espectador.
8.  **Estructura Coherente:** Mantén una estructura coherente en todas las escenas para facilitar la posterior implementación en Manim.

**Entrada:**

[Aquí se insertará el texto que describe las escenas a animar]"
"""

#UN CASO DE GENERAR CODIGO

# prompt = ("""Dado el siguiente texto, teniendo en cuenta las especificidades que destaca, generame el codigo en manim, asegurate de que solo sea codigo y comentarios, nada mas: ###ESCENA###
# **Título de la Escena:** Introducción a la Circunferencia - Definición
# **Entorno:**
# *   Fondo: Color blanco (#FFFFFF)
# *   Plano Cartesiano: Visible, con ejes X e Y etiquetados. Las líneas de la grilla son de color gris claro (#DDDDDD) y tienen un grosor fino.   
# *   Iluminación: Luz ambiental uniforme.

# **Objetos:**

# *   **eje_x:**
#     *   Tipo de Objeto: Línea
#     *   Propiedades:
#         *   Posición Inicial: (-5, 0, 0)
#         *   Posición Final: (5, 0, 0)
#         *   Color: Negro (#000000)
#         *   Grosor: 2
#     *   Animaciones: Ninguna
# *   **eje_y:**
#     *   Tipo de Objeto: Línea
#     *   Propiedades:
#         *   Posición Inicial: (0, -3, 0)
#         *   Posición Final: (0, 3, 0)
#         *   Color: Negro (#000000)
#         *   Grosor: 2
#     *   Animaciones: Ninguna

# *   **circunferencia_definicion_titulo:**
#     *   Tipo de Objeto: Texton
#     *   Propiedades:
#         *   Posición Inicial: (0, 2.5, 0)
#         *   Texto: Circunferencia: Definición
#         *   Fuente: Arial
#         *   Tamaño de la Fuente: 0.7
#         *   Color: Negro (#000000)
#         *   Alineación: Centrado
#     *   Animaciones: FadeIn (Duración: 0.5 segundos, Interpolación: linear, Tiempo de Inicio: 0, Tiempo de Finalización: 0.5)

# *   **punto_o:**
#     *   Tipo de Objeto: Punto
#     *   Propiedades:
#         *   Posición Inicial: (1, 0.5, 0)  (Coordenadas (h, k), h=1, k=0.5)
#         *   Color: Rojo (#FF0000)
#         *   Tamaño: 0.1
#     *   Animaciones: FadeIn (Duración: 0.3 segundos, Interpolación: ease_in, Tiempo de Inicio: 1, Tiempo de Finalización: 1.3)

# *   **label_punto_o:**
#     *   Tipo de Objeto: Texto
#     *   Propiedades:
#         *   Posición Inicial: (1.3, 0.8, 0)
#         *   Texto: O(h, k)
#         *   Fuente: Arial
#         *   Tamaño de la Fuente: 0.4
#         *   Color: Rojo (#FF0000)
#         *   Alineación: Izquierda
#     *   Animaciones: FadeIn (Duración: 0.3 segundos, Interpolación: ease_in, Tiempo de Inicio: 1, Tiempo de Finalización: 1.3)

# *   **punto_p:**
#     *   Tipo de Objeto: Punto
#     *   Propiedades:
#         *   Posición Inicial: (3, 1.5, 0) (Punto genérico P(x,y) en la circunferencia)
#         *   Color: Azul (#0000FF)
#         *   Tamaño: 0.08
#     *   Animaciones: FadeIn (Duración: 0.3 segundos, Interpolación: ease_in, Tiempo de Inicio: 2, Tiempo de Finalización: 2.3)

# *   **label_punto_p:**
#     *   Tipo de Objeto: Texto
#     *   Propiedades:
#         *   Posición Inicial: (3.3, 1.8, 0)
#         *   Texto: P(x, y)
#         *   Fuente: Arial
#         *   Tamaño de la Fuente: 0.4
#         *   Color: Azul (#0000FF)
#         *   Alineación: Izquierda
#     *   Animaciones: FadeIn (Duración: 0.3 segundos, Interpolación: ease_in, Tiempo de Inicio: 2, Tiempo de Finalización: 2.3)

# *   **radio_op:**
#     *   Tipo de Objeto: Línea
#     *   Propiedades:
#         *   Posición Inicial: (1, 0.5, 0)
#         *   Posición Final: (3, 1.5, 0)
#         *   Color: Verde (#00FF00)
#         *   Grosor: 2
#     *   Animaciones: Create (Duración: 0.5 segundos, Interpolación: linear, Tiempo de Inicio: 3, Tiempo de Finalización: 3.5)
# *   **label_radio:**
#     *   Tipo de Objeto: Texto
#     *   Propiedades:
#         *   Posición Inicial: (2, 1, 0)
#         *   Texto: r
#         *   Fuente: Arial
#         *   Tamaño de la Fuente: 0.5
#         *   Color: Verde (#00FF00)
#         *   Alineación: Centrado
#     *   Animaciones: FadeIn (Duración: 0.3 segundos, Interpolación: ease_in, Tiempo de Inicio: 3, Tiempo de Finalización: 3.3)

# *   **circunferencia:**
#     *   Tipo de Objeto: Círculo
#     *   Propiedades:
#         *   Posición Inicial: (1, 0.5, 0) (Centro en O(h, k))
#         *   Radio: 2.236 (Distancia entre O y P, calculado con sqrt((3-1)^2 + (1.5-0.5)^2))
#         *   Color: Amarillo (#FFFF00)
#         *   Grosor: 2
#         *   Transparencia: 0.5
#     *   Animaciones: Create (Duración: 1 segundos, Interpolación: smooth, Tiempo de Inicio: 4, Tiempo de Finalización: 5)

# **Texto en Pantalla:**

# *   "Definición: Llamaremos circunferencia al lugar geométrico de todos los puntos cuya distancia a un punto fijo del plano O(h, k)(denominado centro) es igual a una constante r (denominada radio).
#     *   Posición: (0, -1.5, 0)
#     *   Fuente: Arial
#     *   Tamaño: 0.5
#     *   Color: Negro (#000000)
#     *   Duración: 5 segundos (Aparece gradualmente desde t=1 hasta t=2, se mantiene hasta t=6)
#     *   Animaciones: Write (Duración: 1 segundos, Interpolación: linear, Tiempo de Inicio: 1, Tiempo de Finalización: 2)

# **Cámara:**
# *   Ninguna""")


#CORREGIR CODIGO


# respuesta = llm.query(prompt)
# print(respuesta)
# corregido = llm.query("corrige las posibles fallas qe pueda tener el siguiente codigo de manim " + respuesta)
# print(corregido)

# aa = """el siguiente codigo me da bateo por el ease_in que no esta definido, arreglalo
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
#         self.play(FadeIn(punto_o, run_time=0.3, rate_func="ease_in"), FadeIn(label_punto_o, run_time=0.3, rate_func=ease_in))        
#         self.wait(0.7)

#         # Punto P(x, y)
#         punto_p = Dot(point=[3, 1.5, 0], color=BLUE, radius=0.08)
#         label_punto_p = Text("P(x, y)", font="Arial", font_size=20, color=BLUE).next_to(punto_p, RIGHT + UP, buff=0.1) #Ajuste tamaño
#         self.play(FadeIn(punto_p, run_time=0.3, rate_func= "ease_in"), FadeIn(label_punto_p, run_time=0.3, rate_func=ease_in))        
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
#         self.wait(4)"""
# x = llm.query(aa)
# print(x)


#prompt generado por el llm para pedir codigo manim
a = """"Eres un experto en Manim y un ingeniero de prompts. Tu tarea es generar código Manim limpio, correcto, funcional y legible que visualice un conjunto de escenas descritas textualmente. Debes priorizar la exactitud de la sintaxis, la claridad del 
código y la fidelidad a las descripciones de las escenas.  Asegúrate de que el código compile sin errores y produzca el video deseado.

**Consideraciones Importantes:**

*   **Sintaxis Perfecta:** Presta atención extrema a la sintaxis de Python y Manim.  Revisa cada línea en busca de errores 
tipográficos, comas faltantes, paréntesis desbalanceados, indentación incorrecta, etc.
*   **Variables Bien Definidas:**  Asegúrate de que cada variable utilizada se defina antes de ser utilizada, con el tipo de dato correcto.
*   **Funciones Claramente Definidas:** Si una escena requiere una función personalizada (por ejemplo, para animaciones complejas), define la función con precisión, incluyendo argumentos y documentación.
*   **Animaciones Suaves:** Utiliza interpolaciones y funciones de animación apropiadas para crear transiciones suaves entre objetos y estados. Considera el uso de `rate_functions`.
*   **Textos Legibles:** Asegúrate de que el texto en la pantalla sea legible.  Utiliza tamaños de fuente apropiados, colores contrastantes y, si es necesario, agrega fondos o contornos al texto.
*   **Comentarios Claros:** Agrega comentarios en el código para explicar el propósito de cada sección y las decisiones de 
diseño importantes.
*   **Optimización:**  Si es posible, optimiza el código para que se ejecute de manera eficiente y reduzca el tiempo de renderizado.  Considera el uso de `Scene.wait()` para controlar la duración de las animaciones.
*   **Contexto:** Ten en cuenta la lógica global de la animación, no solo cada escena de forma aislada. Trata de reutilizar objetos y variables donde sea posible para mantener la coherencia y evitar redundancias.
*   **Estilo Manim:** Utiliza el estilo recomendado de Manim, incluyendo nombres de clases y funciones.
*   **Unidades:** Asegúrate de que todas las unidades (tamaños, posiciones) sean consistentes y lógicas dentro del contexto de Manim.  Evita valores arbitrarios sin justificación.

**Formato de Salida:**

*   El código debe estar completamente contenido dentro de una sola celda de código Python (formato adecuado para copy-paste directo).
*   Incluye las importaciones necesarias al principio del código.
*   Organiza el código en una clase que herede de `Scene`.
*   Utiliza nombres descriptivos para las funciones dentro de la clase `Scene`.
*   Después del código, incluye una breve explicación de cómo se organiza el código y las decisiones de diseño tomadas. 

**Título de la Escena:** Introducción a la Circunferencia - Definición
**Entorno:**
*   Fondo: Color blanco (#FFFFFF)
*   Plano Cartesiano: Visible, con ejes X e Y etiquetados. Las líneas de la grilla son de color gris claro (#DDDDDD) y tienen un grosor fino.   
*   Iluminación: Luz ambiental uniforme.

**Objetos:**

*   **eje_x:**
    *   Tipo de Objeto: Línea
    *   Propiedades:
        *   Posición Inicial: (-5, 0, 0)
        *   Posición Final: (5, 0, 0)
        *   Color: Negro (#000000)
        *   Grosor: 2
    *   Animaciones: Ninguna
*   **eje_y:**
    *   Tipo de Objeto: Línea
    *   Propiedades:
        *   Posición Inicial: (0, -3, 0)
        *   Posición Final: (0, 3, 0)
        *   Color: Negro (#000000)
        *   Grosor: 2
    *   Animaciones: Ninguna

*   **circunferencia_definicion_titulo:**
    *   Tipo de Objeto: Texton
    *   Propiedades:
        *   Posición Inicial: (0, 2.5, 0)
        *   Texto: Circunferencia: Definición
        *   Fuente: Arial
        *   Tamaño de la Fuente: 0.7
        *   Color: Negro (#000000)
        *   Alineación: Centrado
    *   Animaciones: FadeIn (Duración: 0.5 segundos, Interpolación: linear, Tiempo de Inicio: 0, Tiempo de Finalización: 0.5)

*   **punto_o:**
    *   Tipo de Objeto: Punto
    *   Propiedades:
        *   Posición Inicial: (1, 0.5, 0)  (Coordenadas (h, k), h=1, k=0.5)
        *   Color: Rojo (#FF0000)
        *   Tamaño: 0.1
    *   Animaciones: FadeIn (Duración: 0.3 segundos, Interpolación: ease_in, Tiempo de Inicio: 1, Tiempo de Finalización: 1.3)

*   **label_punto_o:**
    *   Tipo de Objeto: Texto
    *   Propiedades:
        *   Posición Inicial: (1.3, 0.8, 0)
        *   Texto: O(h, k)
        *   Fuente: Arial
        *   Tamaño de la Fuente: 0.4
        *   Color: Rojo (#FF0000)
        *   Alineación: Izquierda
    *   Animaciones: FadeIn (Duración: 0.3 segundos, Interpolación: ease_in, Tiempo de Inicio: 1, Tiempo de Finalización: 1.3)

*   **punto_p:**
    *   Tipo de Objeto: Punto
    *   Propiedades:
        *   Posición Inicial: (3, 1.5, 0) (Punto genérico P(x,y) en la circunferencia)
        *   Color: Azul (#0000FF)
        *   Tamaño: 0.08
    *   Animaciones: FadeIn (Duración: 0.3 segundos, Interpolación: ease_in, Tiempo de Inicio: 2, Tiempo de Finalización: 2.3)

*   **label_punto_p:**
    *   Tipo de Objeto: Texto
    *   Propiedades:
        *   Posición Inicial: (3.3, 1.8, 0)
        *   Texto: P(x, y)
        *   Fuente: Arial
        *   Tamaño de la Fuente: 0.4
        *   Color: Azul (#0000FF)
        *   Alineación: Izquierda
    *   Animaciones: FadeIn (Duración: 0.3 segundos, Interpolación: ease_in, Tiempo de Inicio: 2, Tiempo de Finalización: 2.3)

*   **radio_op:**
    *   Tipo de Objeto: Línea
    *   Propiedades:
        *   Posición Inicial: (1, 0.5, 0)
        *   Posición Final: (3, 1.5, 0)
        *   Color: Verde (#00FF00)
        *   Grosor: 2
    *   Animaciones: Create (Duración: 0.5 segundos, Interpolación: linear, Tiempo de Inicio: 3, Tiempo de Finalización: 3.5)
*   **label_radio:**
    *   Tipo de Objeto: Texto
    *   Propiedades:
        *   Posición Inicial: (2, 1, 0)
        *   Texto: r
        *   Fuente: Arial
        *   Tamaño de la Fuente: 0.5
        *   Color: Verde (#00FF00)
        *   Alineación: Centrado
    *   Animaciones: FadeIn (Duración: 0.3 segundos, Interpolación: ease_in, Tiempo de Inicio: 3, Tiempo de Finalización: 3.3)

*   **circunferencia:**
    *   Tipo de Objeto: Círculo
    *   Propiedades:
        *   Posición Inicial: (1, 0.5, 0) (Centro en O(h, k))
        *   Radio: 2.236 (Distancia entre O y P, calculado con sqrt((3-1)^2 + (1.5-0.5)^2))
        *   Color: Amarillo (#FFFF00)
        *   Grosor: 2
        *   Transparencia: 0.5
    *   Animaciones: Create (Duración: 1 segundos, Interpolación: smooth, Tiempo de Inicio: 4, Tiempo de Finalización: 5)

**Texto en Pantalla:**

*   "Definición: Llamaremos circunferencia al lugar geométrico de todos los puntos cuya distancia a un punto fijo del plano O(h, k)(denominado centro) es igual a una constante r (denominada radio).
    *   Posición: (0, -1.5, 0)
    *   Fuente: Arial
    *   Tamaño: 0.5
    *   Color: Negro (#000000)
    *   Duración: 5 segundos (Aparece gradualmente desde t=1 hasta t=2, se mantiene hasta t=6)
    *   Animaciones: Write (Duración: 1 segundos, Interpolación: linear, Tiempo de Inicio: 1, Tiempo de Finalización: 2)

**Cámara:**
*   Ninguna"""
b = llm.query(a)
#print(b)