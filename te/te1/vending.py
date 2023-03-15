# ******************
# MÁQUINA DE VENDING
# ******************
import filecmp
from pathlib import Path
    
products = {}
balance = 0

def read_data(operations_path: Path):
    with open(operations_path, "r") as f:
        ops = []
        for line in f:
            tokens = line.strip().split()
            op = tokens[0]
            ops.append(op)
        return ops, tokens


def order(ops: int, tokens: int, balance: int, products: dict):

    for op in ops:
        if op == "O":
            # Hacer un pedido
            code = tokens[1]
            quantity = int(tokens[2])
            price = products.get(code, (0, 0))[1]
            total_price = quantity * price
            if code in products:
                products[code] = (products[code][0] - quantity, products[code][1])
                balance += total_price
        return products, balance


def restok_product(ops: str, tokens: int, products: dict):
    if ops == "R":
        # Reponer un producto
        code = tokens[1]
        quantity = int(tokens[2])
        if code not in products:
            # Producto no existe, crear uno nuevo
            products[code] = (quantity, 0)
        else:
            # Actualizar stock
            products[code] = (products[code][0] + quantity, products[code][1])
    return products


def change_price(ops: str, tokens: int, products: dict):
    for op in ops:
        if op == "P":
            # Cambiar el precio de un producto
            code = tokens[1]
            price = int(tokens[2])
            if code not in products:
                # Producto no existe
                print(f"E1: PRODUCT NOT FOUND ({code})")
            else:
                # Actualizar precio
                products[code] = (products[code][0], price)
        return products


def restock_money(ops: str, tokens: int, products: dict, balance: int):
    for op in ops:
        if op == "M":
            # Reponer dinero
            amount = int(tokens[1])
            balance += amount
        return balance, products


def write_data(status_path: Path, balance: int, products: dict):
    with open(status_path, "w") as f:
        f.write(f"{balance}\n")
        for code in sorted(products):
            quantity, price = products[code]
            result = f.write(f"{code} {quantity} {price}\n")
            return result

def run(operations_path: Path) -> bool:
    global balance
    balance = 0
    global products 
    products = {}
    status_path = "data/vending/status.dat"
    ops, tokens = read_data(operations_path)
    products, balance = order(ops, tokens, balance, products)
    restok_product(ops, tokens,products)
    change_price(ops, tokens, products)
    restock_money(ops, tokens, products, balance)
    write_data(status_path, balance, products)
    return filecmp.cmp(status_path, "data/vending/.expected", shallow=False)


if __name__ == "__main__":
    run("data/vending/operations.dat")
