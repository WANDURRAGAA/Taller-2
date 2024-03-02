# Escribit un porgrama que muestre la siguiente serie de números basado en un número dado por el usuario: ejemplo si el numero es 5 que sea 1, 22, 333, 4444, 55555. y si el número es 6 que sea 1, 22, 333, 4444, 55555, 666666.

def feid():
    numero = int(input("Introduce un número positivo: "))
    while numero < 0:
        numero = int(input("Introduce un número positivo: "))
    for i in range(1, numero + 1):
        print(str(i) * i, end=", ")
feid()