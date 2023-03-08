# **************************************************
# IDENTIFICANDO SECUENCIAS CONSECUTIVAS DE UN TAMAÑO
# **************************************************


def consecutive_seq(items:list, target_count:int) -> int:
    new_items = []
    for item in items:
        if item not in new_items:
            new_items.append(item)
        else:
            count_items = new_items.count(item)
            if target_count == count_items:
                return item
            else:
                return False
        return consecutive_seq(items, target_count)