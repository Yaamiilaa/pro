from __future__ import annotations


class Fraction:
    def __init__(self, num: int, den: int):
        self.greatest_common_diisor = self.gcd(num, den)
        self.num = num / self.greatest_common_diisor
        self.den = den / self.greatest_common_diisor

    def __add__(self, other: Fraction):
        sum_nums = (self.num * other.den) + (
            other.num * self.den)
        sum_dens = self.den * other.den
        return Fraction(sum_nums, sum_dens)

    def __sub__(self, other):
        sum_numerators = (self.num * other.den) - (
            other.num * self.den
        )
        sum_dens = self.den * other.den
        return Fraction(sum_numerators, sum_dens)

    def __mul__(self, other):
        mult_numerators = self.num * other.num
        mult_dens = self.den * other.den
        return Fraction(mult_numerators, mult_dens)

    def __truediv__(self, other):
        div_numerators = self.num * other.den
        div_dens = self.den * other.num
        return Fraction(div_numerators, div_dens)

    def __str__(self) -> str:
        return f"{self.num}\n-----\n{self.den}"

    @staticmethod
    def gcd(a: int, b: int) -> int:
        '''Euclid's Algorithm'''
        while b > 0:
            a, b = b, a % b
        return a
