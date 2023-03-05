# *****************
# NÚMEROS PERFECTOS
# *****************


def is_perfect(n: int) -> bool:
    count_divisor = 0
    for divisor in range (1, n):
        if n % divisor == 0:
            count_divisor += divisor
    if count_divisor == n:
        return True
    else:
        return False

