# Escriba un programa en Python que determine si un email dado 
# tiene el formato correcto.

import re

def is_an_email_valid(email: str) -> bool:
    regex = r'\w@\w.\w'
    result = re.search(regex, email, re.I)
    return result is not None

print(is_an_email_valid('ram$Yamila.2003@HOTMAIL.ES'))