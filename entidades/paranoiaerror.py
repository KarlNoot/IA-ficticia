"""Crearemos exceptions para esta IA definiendolas como clases"""

class ParanoiaError(Exception):

    def __init__(self, mensaje: str):
        self.mensaje = mensaje
        super().__init__(mensaje)
    
    def __init__(self, color: str):
        self.color = color
        super().__init__(color)

    