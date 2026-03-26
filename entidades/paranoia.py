"""Definineremos la clase de este robot todo paranoicop a la bestia
aqui se definira su clase y funcionamiento"""

from entidades.paranoiaerror import ParanoiaError

class Paranoia:

    def __init__(self, nombre: str, color: str, prompt: str):
        self.nombre = nombre
        self.color = color
        self.prompt = prompt

    def saludar(self) -> str:
        if self.prompt != 'Q royo, no soy chat gipiti':
            raise ParanoiaError("No we")
        
    
        
        return f"Hola, {self.nombre}, mucho gusto {"usuario"}"

patrones_prompt = ["tonta", "suicidar", "matar", "te odio", "odio", "te matare", "tonto"]

def responder(prompt):



