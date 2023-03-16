# ******************
# MÁQUINA DE VENDING
# ******************
import filecmp
from pathlib import Path


def run(operations_path: Path) -> bool:
    status_path = "data/vending/status.dat"
    products = {}
    balance = 0

    with open(operations_path, "r") as f:
        for line in f:
            tokens = line.strip().split()
            op = tokens[0]
            if op == "O":
                # Hacer un pedido
                code = tokens[1]
                quantity = int(tokens[2])
                price = products.get(code, (0, 0))[1]
                total_price = quantity * price
                user_money = int(tokens[3])
                if code not in products:
                    # Producto no existe
                    print(f"E1: PRODUCT NOT FOUND ({code})")
                elif quantity > products[code][0]:
                    # Stock insuficiente
                    print(f"E2: UNAVAILABLE STOCK ({code})")
                elif user_money < total_price:
                    # Dinero insuficiente
                    print(f"E3: NOT ENOUGH USER MONEY ({code})")
                else:
                    # Operación exitosa
                    products[code] = (products[code][0] - quantity, products[code][1])
                    balance += total_price
            elif op == "R":
                # Reponer un producto
                code = tokens[1]
                quantity = int(tokens[2])
                if code not in products:
                    # Producto no existe, crear uno nuevo
                    products[code] = (quantity, 0)
                else:
                    # Actualizar stock
                    products[code] = (products[code][0] + quantity, products[code][1])
            elif op == "P":
                # Cambiar el precio de un producto
                code = tokens[1]
                price = int(tokens[2])
                if code not in products:
                    # Producto no existe
                    print(f"E1: PRODUCT NOT FOUND ({code})")
                else:
                    # Actualizar precio
                    products[code] = (products[code][0], price)
            elif op == "M":
                # Reponer dinero
                amount = int(tokens[1])
                balance += amount

    with open(status_path, "w") as f:
        f.write(f"{balance}\n")
        for code in sorted(products):
            quantity, price = products[code]
            f.write(f"{code} {quantity} {price}\n")

    return filecmp.cmp(status_path, "data/vending/.expected", shallow=False)


if __name__ == "__main__":
    run("data/vending/operations.dat")
