from abc import ABC, abstractmethod
from google import genai

class AbstractLLM(ABC):
    def __init__(self, api_key: str):
        self.api_key = api_key

    @abstractmethod
    def query(self, prompt: str, **kwargs) -> str:
        """
        Envía un prompt al modelo y retorna la respuesta generada.
        kwargs puede incluir parámetros específicos de la API.
        """
        pass

    def set_api_key(self, api_key: str):
        self.api_key = api_key


class GeminiLLM(AbstractLLM):
    def __init__(self, api_key: str):
        super().__init__(api_key)
        self.client = genai.Client(api_key=self.api_key)

    def query(self, prompt: str, **kwargs) -> str:
        try:
            response = self.client.models.generate_content(
                model="gemini-2.0-flash",
                contents=prompt,
                **kwargs
            )
            return response.text
        except Exception as e:
            print("Error en la llamada a la API:", e)
        
    
    def GenerateManimCode(self, text, context):
        escenes = self.query(context + text)
        print("Creacion de las escenas \n" + escenes)
        code = self.query("Dada la siguiente informacion y distribucion de las escenas, generame un codigo en manim" + escenes)
        print("Codigo generado de manim: " + code)
        return escenes, code

    # Es necesairio especificarle al llm que debe dividir las escenas con &&&
    def GenerateManimCodeForEscenes(self, text, context, manim_specifications, code_specifications):
        # Obtener la descripción completa de las escenas
        scenes_description = self.query(context + text)
        print("Creación de las escenas:\n" + scenes_description)
        
        scenes = self.query(manim_specifications + scenes_description)
        print("Especificaciones para las escenas: \n" + scenes)
        
        # Dividir la descripción en escenas individuales usando split_text (que divide por $$$)
        individual_scenes = self.split_text(scenes_description)
        
        # Generar código Manim para cada escena por separado
        manim_codes = []
        for i, scene_text in enumerate(individual_scenes, start=1):
            prompt_code = code_specifications + scene_text
            code = self.query(prompt_code)
            print(f"Código generado para la escena {i}:\n{code}\n")
            manim_codes.append(code)
        return scenes_description, scenes, manim_codes

    def split_text(self, text: str, delimiter: str = "&&&") -> list[str]:
        parts = text.split(delimiter)
        trimmed_parts = [part.strip() for part in parts]
        return trimmed_parts

