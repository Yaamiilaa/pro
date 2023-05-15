from __future__ import annotations


def load_card_glyphs(path: str = "cards.dat") -> dict[str, str]:
    """Retorna un diccionario donde las claves serán los palos
    y los valores serán cadenas de texto con los glifos de las
    cartas sin ningún separador"""
    with open(path, "r") as f:
        cards = {}
        for lines in f:
            symbols, glyphs = lines.strip().split(":")
            cards_glyphs = glyphs.replace(",", "")
            cards[symbols] = cards_glyphs
        return cards


class Card:
    CLUBS = "♣"
    DIAMONDS = "◆"
    HEARTS = "❤"
    SPADES = "♠"
    #           1,   2,   3,   4,   5,   6,   7,   8,   9,   10,  11,  12,  13
    SYMBOLS = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
    A_VALUE = 1
    K_VALUE = 13
    GLYPHS = load_card_glyphs()

    def __init__(self, value: int | str, suit: str):
        """Notas:
        - Si el suit(palo) no es válido hay que elevar una excepción de tipo
        InvalidCardError() con el mensaje: 🃏 Invalid card: {repr(suit)} is not a supported suit
        - Si el value(como entero) no es válido (es menor que 1 o mayor que 13) hay que
        elevar una excepción de tipo InvalidCardError() con el mensaje:
        🃏 Invalid card: {repr(value)} is not a supported value
        - Si el value(como string) no es válido hay que elevar una excepción de tipo
        🃏 Invalid card: {repr(value)} is not a supported symbol

        - self.suit deberá almacenar el palo de la carta '♣◆❤♠'.
        - self.value deberá almacenar el valor de la carta (1-13)"""
        if isinstance(value, str) and value not in Card.SYMBOLS:
            raise InvalidCardError(f"{repr(value)} is not a supported symbol")
        if value > Card.K_VALUE or value < Card.A_VALUE:
            raise InvalidCardError(f"{repr(value)} is not a supported value")
        if suit not in Card.get_available_suits():
            raise InvalidCardError(f"{repr(suit)} is not a supported suit")
        self.value = value
        self.suit = suit
        
    @property
    def cmp_value(self) -> int:
        """Devuelve el valor (numérico) de la carta para comparar con otras.
        Tener en cuenta el AS."""
        return self.value if not self.is_ace() else Card.A_VALUE + Card.K_VALUE

    def __repr__(self):
        """Devuelve el glifo de la carta"""
        return Card.GLYPHS[self.suit][self.value - 1]

    def __eq__(self, other: Card | object):
        """Indica si dos cartas son iguales"""
        return self.value == other.value and self.suit == other.suit

    def __lt__(self, other: Card):
        """Indica si una carta vale menos que otra"""
        return self.cmp_value == min(self.cmp_value, other.cmp_value)

    def __gt__(self, other: Card):
        """Indica si una carta vale más que otra"""
        return self.cmp_value == max(self.cmp_value, other.cmp_value)

    def __add__(self, other: Card) -> Card:
        """Suma de dos cartas:
        1. El nuevo palo será el de la carta más alta.
        2. El nuevo valor será la suma de los valores de las cartas. Si valor pasa
        de 13 se convertirá en un AS."""
        suit = self.suit if self.cmp_value > other.cmp_value else other.suit 
        value = Card.A_VALUE if self.cmp_value + other.cmp_value > Card.K_VALUE else self.value + other.value
        return Card(value, suit)

    def is_ace(self) -> bool:
        """Indica si una carta es un AS"""
        return self.value == Card.A_VALUE

    @classmethod
    def get_available_suits(cls) -> str:
        """Devuelve todos los palos como una cadena de texto"""
        return Card.CLUBS + Card.DIAMONDS + Card.HEARTS + Card.SPADES 

    @classmethod
    def get_cards_by_suit(cls, suit: str):
        """Función generadora que devuelve los glifos de las cartas por su palo"""
        for gliphs in Card.GLYPHS[suit]:
            yield gliphs


class InvalidCardError(Exception):
    """Clase que representa un error de carta inválida.
    - El mensaje por defecto de esta excepción debe ser: 🃏 Invalid card
    - Si se añaden otros mensajes aparecerán como: 🃏 Invalid card: El mensaje que sea"""
    def __init__(self, message: str = ""):
        self.message = "🃏 Invalid card"
        if message:
            self.message += f": {message}"
        super().__init__(message)
    
    def __str__(self):
        return self.message
