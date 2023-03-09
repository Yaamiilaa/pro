# ******************
# MÁQUINA DE VENDING
# ******************
import filecmp
from pathlib import Path


def read_operations(operations_path: Path) -> bool:
    with open(operations_path, "r") as f:
        for line in f:
            tokens = line.strip().split()
            op = tokens[0]
    return tokens, op


def order(op: str, tokens: list, products: dict, balance: int):
    balance = 0
    products = {}
    if op == "O":
        # Hacer un pedido
        code = tokens[1]
        quantity = int(tokens[2])
        price = products.get(code, (0, 0))[1]
        total_price = quantity * price
        if code in products:
            # Operación exitosa
            products[code] = (
                products[code][0] - quantity,
                products[code][1],
            )
            balance += total_price
        return balance, products


def restock(op: str, tokens: list, products: dict):
    if op == "R":
        # Reponer un producto
        code = tokens[1]
        quantity = int(tokens[2])
        if code not in products:
            # Producto no existe, crear uno nuevo
            products[code] = (quantity, 0)
        else:
            # Actualizar stock
            products[code] = (
                products[code][0] + quantity,
                products[code][1],
            )
    return products


def change_price(op: str, tokens: list, products: dict):
    if op == "P":
        # Cambiar el precio de un producto
        code = tokens[1]
        price = int(tokens[2])
        if code in products:
            # Actualizar precio
            products[code] = (products[code][0], price)
    return products


def restock_money(op: str, balance: int, tokens: list):
    if op == "M":
        # Reponer dinero
        amount = int(tokens[1])
        balance += amount
    return balance


def run(operations_path: Path) -> bool:
    status_path = "data/vending/status.dat"
    # Escribe el estado final de la máquina en el archivo de salida.
    def write_data(status_path: Path, balance: int, products: dict) -> bool:
        with open(status_path, "w") as f:
            f.write(f"{balance}\n")
            for code in sorted(products):
                quantity, price = products[code]
        return f.write(f"{code} {quantity} {price}\n")
    return filecmp.cmp(status_path, "data/vending/.expected", shallow=False)


if __name__ == "__main__":
    run("data/vending/operations.dat")
