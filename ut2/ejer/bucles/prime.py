def prime(n = 11):
    for i in range(2, n // 2):
        if n % i == 0:
            result = 'No es primo'
            break
        else:
            result = 'Es primo'
    return result

print(prime())