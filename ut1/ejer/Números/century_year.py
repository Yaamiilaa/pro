# **************************
# BUSCANDO EL SIGLO ADECUADO
# **************************


def run(year: int) -> int:
    if year % 100 == 0:
        century = round(year // 100)
    else:
        century = round(year // 100) + 1
    return century


if __name__ == '__main__':
    run(1705)