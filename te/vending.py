
operation = '/home/yamila/pro/te/operation.dat'
status = '/home/yamila/pro/te/status.dat'
def read_vending_file(vending = '/home/yamila/pro/te/vending.dat'):
    # Lee el archivo vending.dat y devuelve un diccionario con los datos
    vending_data = {}
    with open(vending) as f:
        # Lee la primera línea y guarda los datos de las monedas
        coins = f.readline().strip().split()
        vending_data['coins'] = {'2': int(coins[0]), '1': int(coins[1]), '0.5': int(coins[2])}
        
        # Lee el resto del archivo y guarda los datos de los productos
        products = {}
        for line in f:
            code, stock, price = line.strip().split()
            products[code] = {'stock': int(stock), 'price': float(price)}
        
        vending_data['products'] = products
        
    return vending_data


def read_operations_file(operation = '/home/yamila/pro/te/operation.dat'):
    # Lee el archivo operations.dat y devuelve una lista de tuplas con las operaciones
    operations = []
    with open(operation) as f:
        for line in f:
            op = line.strip().split()
            operations.append(tuple(op))
    
    return operations




def process_order(vending_data, code, quantity, coins_2, coins_1, coins_05):
    # Procesa un pedido y devuelve el cambio (si lo hay) y un mensaje de estado
    products = vending_data['products']
    coins = vending_data['coins']
    if code not in products:
        return 0, "ERROR: Invalid product code"
    
    product = products[code]
    if product['stock'] < quantity:
        return 0, "ERROR: Insufficient stock"
    
    total_price = quantity * product['price']
    total_inserted = coins_2 * 2 + coins_1 + coins_05 * 0.5
    
    if total_inserted < total_price:
        return 0, "ERROR: Insufficient funds"
    
    # Calcula el cambio y actualiza las monedas disponibles
    change = total_inserted - total_price
    coins['2'] += coins_2
    coins['1'] += coins_1
    coins['0.5'] += coins_05
    
    # Actualiza el stock del producto
    product['stock'] -= quantity
    
    return change, f"Dispensing {quantity} {code}. Change: {change:.2f} €"


def process_restock(vending_data, code, quantity):
    # Repone el stock del producto indicado
    products = vending_data['products']
    if code not in products:
        return "ERROR: Invalid product code"
    
    product = products[code]
    product['stock'] += quantity
    
    return f"Stock of {code} replenished. Current stock: {product['stock']}"




def write_status_file(status = '/home/yamila/pro/te/status.dat', *, vending_data):
    # Escribe el diccionario vending_data en el archivo vending
    with open(status, 'w') as f:
        # Escribe los datos de las monedas
        coins = vending_data['coins']
        f.write(f"{coins['2']} {coins['1']} {coins['0.5']}\n")
        
        # Escribe los datos de los productos, ordenados por código
        products = vending_data['products']
        for code in sorted(products):
            stock = products[code]['stock']
            price = products[code]['price']
            f.write(f"{code} {stock} {price}\n")





   """
    Lee el archivo de operaciones y devuelve una lista de cadenas,
    donde cada cadena es una operación.

    Args:
        filename: el nombre del archivo de operaciones

    Returns:
        una lista de cadenas, donde cada cadena es una operación
    """
    with open(operations_path, "r") as f:
        return f.readlines()

def write_status(filename, machine_balance, products):
    """
    Escribe el estado de la máquina de vending en un archivo.

    Args:
        filename: el nombre del archivo de estado
        machine_balance: el saldo actual de la máquina de vending
        products: un diccionario que contiene los productos de la máquina y su información,
            donde las claves son los códigos de producto y los valores son otros diccionarios
            con las claves "quantity" y "price"
    """
    with open(filename, "w") as f:
        f.write(str(machine_balance) + "\n")
        for code, info in sorted(products.items()):
            quantity = info["quantity"]
            price = info["price"]
            f.write(f"{code} {quantity} {price}\n")