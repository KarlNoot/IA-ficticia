"""Crearemos exceptions para esta IA definiendolas como clases"""

class ParanoiaError(Exception):
    """Excepción personalizada para palabras prohibidas en el prompt."""
    
    def __init__(self, palabra_prohibida, mensaje="Palabra prohibida detectada"):
        self.palabra_prohibida = palabra_prohibida
        self.mensaje = f"{mensaje}: '{palabra_prohibida}'"
        super().__init__(self.mensaje)



