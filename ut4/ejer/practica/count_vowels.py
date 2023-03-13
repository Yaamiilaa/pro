# *******************************
# CONTANDO VOCALES (EN RECURSIVO)
# *******************************


def count_vowels(text:str) -> int:
    VOWELS = 'aeiou'
    if len(text) == 1:
        if text[0] in VOWELS:
            return 1
        return 0
    return count_vowels(text[0]) + count_vowels(text[1:])
