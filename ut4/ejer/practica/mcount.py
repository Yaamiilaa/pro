# *******************
# CONTANDO SIN CONTAR
# *******************


def mcount(items: set[int], target: int) -> int:
    count_item = 0
    for item in items:
        if item == target:
            count_item += 1
    return count_item
