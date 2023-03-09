# **************************************************
# IDENTIFICANDO SECUENCIAS CONSECUTIVAS DE UN TAMAÑO
# **************************************************


def consecutive_seq(items:list, target_count:int) -> int:
    if len(items) == 0:
        
        return consecutive_seq(items, target_count)