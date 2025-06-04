from google import genai
text = "hola, como estas"

def GenerateManimCode(text):
    client = genai.Client()
    initialContext = "Dado el siguiente texto necesito que me hagas una planificacion de escenas para luego dado un codigo en manim generar un video con fines educacionales representando lo que explica el texto"
    prompt = initialContext + text
    response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=prompt)
    print(response.text)

GenerateManimCode(text)