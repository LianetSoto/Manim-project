from google import genai
prompt = "Dado el siguiente texto como crees que deberia representarse en video mostrando lo que esta sugiriendo, solo has eso no me digas nada mas :Definición: Se denomina sección cónica degenerada a la intersección de un cono circular recto de dos hojas con un plano que pasa por su vértice. Se clasifican en tres tipos: punto, recta y par de rectas.Definición: Se denomina traslación de un sistema de coordenadas 𝑂𝑋𝑌 en el plano, a otro sistema de coordenadas 𝑂′𝑋′𝑌′ tal que los ejes 𝑂′𝑋′ y 𝑂′𝑌′ son paralelos a los ejes 𝑂𝑋 y 𝑂𝑌, respectivamente, y además, tienen el mismo sentido. El vector 𝑂𝑂′ se denomina vector de traslación"
client = genai.Client(api_key= "...")
response = client.models.generate_content(
    model = "gemini-2.0-flash", contents = prompt)
answer = "Generame un codigo en manim dada la siguiente descripcion que se vea claramente el texto que se debe escribir y no se solape con otras animaciones:" + response.text
secresponse = client.models.generate_content(
    model = "gemini-2.0-flash", contents = answer)


# answer2 = "Revisa que todos los metodos y funciones esten bien definidos de no ser asi dame la correccion de codigo sin decirme nada mas :" + secresponse.text
# thirdresponse = client.models.generate_content(
#     model = "gemini-2.0-flash", contents = answer2)
print(secresponse.text)