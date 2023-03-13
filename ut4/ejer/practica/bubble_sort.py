# **********************
# ORDENANDO CON BURBUJAS
# **********************


def bubble(items: list) -> list:
    citems = items.copy()
    change = True
    while change:
        change = False
        for i in range(len(citems) - 1):
            current = citems[i]
            next = citems[i + 1]
            if current > next:
                citems[i] = next
                citems[i + 1] = current
                change = True
    return citems 

