class Droid:
    def __init__(self, name: str):
        self.name = name


class ProtocolDroid(Droid):
    def __init__(self, name: str, languages: list[str]):
        super().__init__(name)  # llamada al constructor de la clase base
        self.languages = languages
