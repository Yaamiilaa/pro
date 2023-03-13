# *****************
# NÚMEROS PERFECTOS
# *****************


def divisors(n: int) -> int:
    for divisors in range(1, n):
        if n % divisors == 0:
            yield divisors


def is_perfect(n: int) -> bool:
    if sum(divisors(n)) == n:
        return True
    return False

