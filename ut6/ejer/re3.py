# Escriba un programa en Python que indique si un 
# determinado número es o no un flotante válido en Python.

import re

def is_a_valid_float(number: str) -> bool:
    regex = '(\d+).(\d+)'
    result = re.search(regex, number) 
    return result is not None

print(is_a_valid_float('10.8'))