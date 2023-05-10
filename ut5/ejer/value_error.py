# Version iterativa
def getint_iterative():
    while True:
        try:
            value = int(input("Give me an integer number: "))
            if isinstance(value, int):
                break
        except ValueError:
            print("Not a valid integer. Try it again!")


# Version recursiva
def getint_recursive():
    try:
        value = int(input("Give me an integer number: "))
    except ValueError:
        print("Not a valid integer. Try it again!")
        return getint_recursive()
