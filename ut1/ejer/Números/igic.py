# ***************
# PRECIO SIN IGIC
# ***************


def run(price_with_igic: float, igic: float) -> float:
    IGIC = igic / 100 + 1
    clean_price = round(price_with_igic / IGIC, 2)
    

    return clean_price


if __name__ == '__main__':
    run(120, 7)