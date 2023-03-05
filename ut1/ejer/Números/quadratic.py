# *************************
# ECUACIÓN DE SEGUNDO GRADO
# *************************


def run(a: int, b: int, c: int) -> tuple:
    DISCRIMINATE = ((b ** 2) - (4 * a * c)) ** (1/2)
    DENOMINADOR = 2 * a
    x1 = (-b + DISCRIMINATE) / DENOMINADOR
    x2 = (-b - DISCRIMINATE) / DENOMINADOR

    return x1, x2


if __name__ == '__main__':
    run(4, -6, 2)