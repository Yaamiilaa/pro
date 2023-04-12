class Fraction:
    def __init__(self, numerator: int, denominator: int):
        self.greatest_common_divisor = self.gcd(numerator, denominator)
        self.numerator = numerator / self.greatest_common_divisor
        self.denominator = denominator / self.greatest_common_divisor

    @staticmethod
    def gcd(a: int, b: int) -> int:
        """Algoritmo de Euclides para el cálculo del Máximo Común Divisor."""
        while b > 0:
            a, b = b, a % b
        return a

    def __add__(self, other):
        sum_numerators = (self.numerator * other.denominator) + (
            other.numerator * self.denominator
        )
        sum_denominators = self.denominator * other.denominator
        return Fraction(sum_numerators, sum_denominators)

    def __sub__(self, other):
        sum_numerators = (self.numerator * other.denominator) - (
            other.numerator * self.denominator
        )
        sum_denominators = self.denominator * other.denominator
        return Fraction(sum_numerators, sum_denominators)

    def __mul__(self, other):
        mult_numerators = self.numerator * other.numerator
        mult_denominators = self.denominator * other.denominator
        return Fraction(mult_numerators, mult_denominators)

    def __truediv__(self, other):
        div_numerators = self.numerator * other.denominator
        div_denominators = self.denominator * other.numerator
        return Fraction(div_numerators, div_denominators)

    def __str__(self) -> str:
        return f"{self.numerator}\n-----\n{self.denominator}"


fraction1 = Fraction(25, 30)
fraction2 = Fraction(40, 45)
print(fraction1.__truediv__(fraction2))
