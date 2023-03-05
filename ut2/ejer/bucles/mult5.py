def mult5(num = 36):
    result = [n for n in range(num + 1) if n % 5 == 0]
    return result

print(mult5())
