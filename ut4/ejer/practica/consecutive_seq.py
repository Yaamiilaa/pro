# **************************************************
# IDENTIFICANDO SECUENCIAS CONSECUTIVAS DE UN TAMAÑO
# **************************************************


def consecutive_seq(items: list[int], target_count: int = 3) -> int:
    def helper(items: list[int], last_seen: int = None, count: int = 0):
        if len(items) == 0:
            return False
        current_item = items[0]
        if current_item == last_seen:
            count += 1
        else:
            count = 1
        if count == target_count:
            return current_item
        return helper(items[1:], current_item, count)

    return helper(items)