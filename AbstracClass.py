from abc import ABC, abstractmethod

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


from google import genai

class GeminiLLM(AbstractLLM):
    def __init__(self, api_key: str):
        super().__init__(api_key)
        self.client = genai.Client(api_key=self.api_key)

    def query(self, prompt: str, **kwargs) -> str:
        response = self.client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt,
            **kwargs
        )
        return response.text
    
    # def GenerateManimCode(self, text, context):
    #     escenes = self.query(prompt + text)
    #     print("Creacion de las escenas \n" + escenes)
    #     code = self.query("Dada la siguiente informacion y distribucion de las escenas, generame un codigo en manim" + escenes)
    #     print("Codigo generado de manim: " + code)
    #     return escenes, code
    
    
    #que es el prompt? cuando me lo pasas
    #arreglar el prompt para generar el codigo de manim
    #asegurarse de que los codigos no tengan comentarios al final
    def GenerateManimCode(self, text, context):
        # Obtener la descripción completa de las escenas
        scenes_description = self.query(prompt + text)
        print("Creación de las escenas:\n" + scenes_description)
        
        # Dividir la descripción en escenas individuales usando split_text (que divide por $$$)
        individual_scenes = split_text(scenes_description)
        
        # Generar código Manim para cada escena por separado
        manim_codes = []
        for i, scene_text in enumerate(individual_scenes, start=1):
            prompt_code = (
                f"Dada la siguiente información y distribución de la escena {i}, "
                f"generame un código en Manim:\n{scene_text}"
            )
            code = self.query(prompt_code)
            print(f"Código generado para la escena {i}:\n{code}\n")
            manim_codes.append(code)
        return scenes_description, manim_codes

def split_text(text: str, delimiter: str = "$$$") -> list[str]:
    parts = text.split(delimiter)
    trimmed_parts = [part.strip() for part in parts]
    return trimmed_parts


