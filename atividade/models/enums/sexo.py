from enum import Enum

class Sexo(Enum):
    MASCULINO = ("M", "Masculino")
    FEMININO = ("F", "Feminino")

    def __init__(self, char: str, text: str):
        self.char = char
        self.text = text