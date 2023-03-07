# ********
# PANGRAMA
# ********


def is_pangram(text: str) -> bool:
    ALPHA = set("abcdefghijklmnopqrstuvwxyz")
    text = set(''.join(text.lower().split()))
    if text == ALPHA:
        return True
    else:
        return False