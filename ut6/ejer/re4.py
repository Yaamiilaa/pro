# Escriba un programa en Python que determine si un email dado
# tiene el formato correcto.

import re


def is_an_email_valid(email: str) -> bool:
    regex = r"^[\w\.-_]+@(gmail|hotmail)[.](es|com)"
    result = re.search(regex, email, re.I)
    return result is not None


print(is_an_email_valid("ramos.y_amila2003@gmail.es"))
