# *****************
# SUMA DE COCIENTES
# *****************


def sum_quot(n: int) -> float:
    if n < 0:
        return 0
    return (1 / sum_quot(n)) + (1 / sum_quot(n - 1))
