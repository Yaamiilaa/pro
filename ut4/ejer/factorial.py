# ************************************
# CALCULANDO EL FACTORIAL DE UN NÚMERO
# ************************************


def factorial(num):
    nums = 1
    for n in range(1, num + 1):
        nums *= n
    if num < 0:
        nums = None
    return nums