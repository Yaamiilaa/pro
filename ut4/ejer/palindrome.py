# **********
# PALÍNDROMO
# **********


def is_palindrome(text: str) -> bool:
    clean_text = ''.join(text.split())
    if clean_text.upper() == clean_text[::-1].upper():
        return True
    else:
        return False

