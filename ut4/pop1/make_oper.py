# *******************
# CREANDO OPERACIONES
# *******************

def make_oper(oper: str) -> float:
    def operations(num1: int, num2: int) -> float:
        match oper:
            case 'add':
                op = num1 + num2
            case 'sub':
                op = num1 - num2
            case 'mul':
                op = num1 * num2
            case 'div':
                op = num1 / num2
            case _:
                op = None
        return op
    return operations



def run(oper: str, num1: int, num2: int) -> float:
    operation = make_oper(oper)
    result = operation(num1, num2)
    return result



