# ********
# PANGRAMA
# ********


def is_pangram(text:str) -> bool:
    ALPHABET = set('abcdefghijklmnopqrstuvwxyz')
    clean_text = set(''.join(text.lower().split()))
    if clean_text == ALPHABET:
        return True
    return False
