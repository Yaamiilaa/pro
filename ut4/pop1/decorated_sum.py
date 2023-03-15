# ****************************
# DECORANDO LA SUMA DE VALORES
# ****************************

def result_as_status(func):
    def wrapper(*args, **kwargs):
        convert = func(*args, **kwargs)
        value1, value2 = convert
        return {'status': value1, 'result': value2}
    return wrapper


@result_as_status
def run(values: list[int|str]) -> dict[str, bool|int|str]:
    result = 0
    for value in values:
        if isinstance(value, int):
            status = True
            result += value
        else:
            status = False
            result = 'Not int value found'
            break
    return status, result

