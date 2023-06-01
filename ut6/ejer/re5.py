# Escriba un programa en Python que obtenga el
# resultado de una operación entre números enteros
# positivos. Las operación puede ser suma, resta,
# multiplicación o división, y puede haber espacios
# (o no) entre los operandos y el operador.

import re


def get_result(numbers: str) -> int | float:
    regex = r"(?P<num1>\d+)\s*(?P<operator>[\+\-\*\/])\s*(?P<num2>\d+)"
    groups = re.search(regex, numbers)
    num1 = int(groups["num1"])
    num2 = int(groups["num2"])
    operator = groups["operator"]
    match operator:
        case "+":
            result = num1 + num2
        case "-":
            result = num1 - num2
        case "*":
            result = num1 * num2
        case "/":
            result = num1 / num2
    return result


print(
    get_result(
        """      2                         
                  /          2"""
    )
)
