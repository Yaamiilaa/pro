# ***************
# CUADRADO MÁGICO
# ***************

def is_magic_square(values):
    n = len(values)
    magic_sum = (n * (n ** 2 + 1)) // 2
    if any(sum(file) != magic_sum for file in values):
        return False
    if any(sum(file[i] for file in values) != magic_sum for i in range(n)):
        return False
    if sum(values[i][i] for i in range(n)) != magic_sum:
        return False
    if sum(values[i][n-1-i] for i in range(n)) != magic_sum:
        return False
    return True