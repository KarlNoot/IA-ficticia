"""Definineremos la clase de este robot todo paranoicop a la bestia
aqui se definira su clase y funcionamiento"""

from entidades.paranoiaerror import ParanoiaError

class Paranoia:
    """Clase que valida prompts en busca de palabras prohibidas."""
    
    def __init__(self, prompt):
        """
        Constructor de la clase Paranoia.
        
        Args:
            prompt (str): El texto a validar
        """
        self.prompt = prompt
        # Lista de palabras prohibidas
        self.palabras_prohibidas = ["tonta", "matar", "suicidar", "odio", "violencia", "asesinar"]
    
    def responder(self):
        """
        Método que valida si el prompt contiene palabras prohibidas.
        
        Returns:
            str: Mensaje de éxito si no hay palabras prohibidas
            
        Raises:
            ParanoiaError: Si se detecta una palabra prohibida
        """
        try:
            
            prompt_minusculas = self.prompt.lower()
            
            
            for palabra in self.palabras_prohibidas:
                if palabra in prompt_minusculas:
                    
                    raise ParanoiaError(palabra)
       
            return "Prompt válido: No se detectaron palabras prohibidas."
            
        except ParanoiaError as e:
 
            print(f"  ALERTA DE PARANOIA: {e}")
            raise e  






