# Escribe un programa en Python que genere un número aleatorio ç
# entre 1 y 100 y le pida al usuario que adivine el número generado.
# El programa deberá proporcionar pistas al usuario indicando si el 
# número que ingresó es demasiado alto o demasiado bajo. 
# El juego continuará hasta que el usuario adivine correctamente el 
# número generado. Al finalizar, el programa mostrará la cantidad de 
# intentos que le tomó al usuario adivinar el número.

# Requerimientos del programa:

# Generar un número aleatorio entre 1 y 100.
# Pedir al usuario que ingrese un número.
# Comparar el número ingresado por el usuario con el número generado y proporcionar pistas.
# Contar la cantidad de intentos que le toma al usuario adivinar el número.
# Continuar el juego hasta que el usuario adivine correctamente.
# Mostrar la cantidad de intentos al finalizar el juego.

from random import randint

def guess_number():
    random = randint(1, 100)
    counter = 0
    while True:    
        num = int(input('Dame un número del 1 al 100: '))
        if num > random:
            print('Tu numero es más grande. Pon un número más pequeño')
        elif num < random:    
            print('Tu número es más pequeño. Pon un número mas grande')
        else: 
            break
        counter += 1
    return f'''¡Correcto! Adivinaste el número
Estos han sido tus intentos {counter}'''

        
print(guess_number())
