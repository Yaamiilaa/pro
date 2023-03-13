# *****************
# ALFABETO CIRCULAR
# *****************

def gen_alphabet(max_letters: int) -> str:
    ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
    for index_letters in range(max_letters):
        index_letter = index_letters % len(ALPHABET)
        yield ALPHABET[index_letter]
def run(max_letters: int) -> str:
    return ''.join(gen_alphabet(max_letters))


if __name__ == '__main__':
    run(0)