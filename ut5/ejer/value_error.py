def getint():
    while True:
        try:
            value = int(input("Give me an integer number: "))
            if isinstance(value, int):
                break
        except ValueError:
            print("Not a valid integer. Try it again!")
