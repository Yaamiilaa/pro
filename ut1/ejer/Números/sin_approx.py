# *******************
# APROXIMANDO EL SENO
# *******************


def run(x: float) -> float:
    PARENTESIS = 180 - x
    COCIENTE = (4 * x) * PARENTESIS
    DENOMINADOR = 40500 - (x * (PARENTESIS))
    sin = COCIENTE / DENOMINADOR
    return sin


if __name__ == '__main__':
    run(90)