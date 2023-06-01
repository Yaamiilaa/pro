# Escriba un programa en Python que encuentre
# todas las palabras que comiencen por vocal en un texto dado.

import re


def found_words(text: str) -> list[str]:
    regex = r"\b[aeiou][\w-]+"
    result = re.findall(regex, text, re.I)
    return result


print(found_words("Esto,     es  uN_a pru_eba"))
