def fibonacci(num=100):
    a = 0
    print(a)
    b = 1
    print(b)

    for _ in range(num - 2):
        r = a + b
        a = b
        b = r
        print(r)
    return r


print(fibonacci())


