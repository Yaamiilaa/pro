# ********
# PANGRAMA
# ********


def is_pangram(text: str) -> bool:
    ALPHA = set('abcdefghijklmnopqrstuvwxyzñ')
    text = text.lower()
    letters = set()
    for characters in text:
        if characters in ALPHA:
            letters.add(characters)
    return ALPHA.issubset(letters)