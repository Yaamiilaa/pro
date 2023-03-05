def num_vowels(text = 'Supercalifragilisticoespialidoso'):
    VOWLES = 'AEIOU'
    count = 0
    for letter in text.upper():
        if letter in VOWLES:
            count += 1
    return count

print(num_vowels())