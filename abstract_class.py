from abc import ABC, abstractmethod
from typing import Optional

class LLMClient(ABC):
    @abstractmethod
    def generate_content(self, prompt: str, model: str, **kwargs) -> str:
        """
        Método abstracto para generar contenido a partir de un modelo de lenguaje
        :param prompt: Texto de entrada para el modelo
        :param model: Identificador del modelo a utilizar
        :param kwargs: Parámetros adicionales específicos de cada implementación
        :return: Respuesta generada por el modelo
        """
        pass

        
class LLMError(Exception):
    """Clase base para errores de LLM"""
    pass