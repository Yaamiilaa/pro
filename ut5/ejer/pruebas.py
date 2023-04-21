class Droid:
    def __init__(self, name: str):
        self.name = name
        matraca = 0


class ProtocolDroid(Droid):
    def __init__(self, name: str, languages: list[str]):
        super().__init__(name)  # llamada al constructor de la clase base
        self.languages = languages
