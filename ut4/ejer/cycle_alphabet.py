# *****************
# ALFABETO CIRCULAR
# *****************


def run(max_letters: int) -> str:
    cycle_alphabet = []
    ALPHA = list("abcdefghijklmnopqrstuvwxyz")
    for i in range(max_letters):   
        if ALPHA[i] == 'z':
            ALPHA[-1] = ALPHA[0]
            cycle_alphabet.append(ALPHA[i])
            
            
 
    text = "".join(cycle_alphabet)
    print(text)
    return text


if __name__ == "__main__":
    run(0)
