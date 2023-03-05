# ***
# XOR
# ***


def run(v1: bool, v2: bool) -> bool:
    if (v1 and not v2) or (not v1 and v2):
        xor = True
    else:
        xor = False
    
    return xor


if __name__ == '__main__':
    run(False, False)