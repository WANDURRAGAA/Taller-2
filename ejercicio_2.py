# Escribir un programa que pida al usuario un n1úmero entero positivo y muestre por pantalla la cuenta hacia atrás desde ese número hasta cero.

def brr():
    numero = int(input("Introduce un número entero positivo: "))
    while numero < 0:
        numero = int(input("Introduce un número entero positivo: "))
    for i in range(numero, -1, -1):
        print(i, end=", ")
brr()