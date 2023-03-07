def recursive(names=["ana", "pepe", "maría"]):
    for i, name in enumerate(names):
        len_names = len(name)
        return recursive(len_names[i]) + recursive(len_names[i + 1])


print(recursive())
