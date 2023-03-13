# ************************************
# FRECUENCIA DE ELEMENTOS CONSECUTIVOS
# ************************************


def cfreq(items: list, /, as_string: bool = False) -> list:
    count_items = 0
    
    for item in items:
        for index_items in range(len(items)):
            last_seen = items[index_items]
            if item == last_seen:
                count_items += 1
            if as_string:
                return f'{item}:{count_items}'
        return item, count_items
