# crea un porgrama que usando bucles nos permita pedir un número par comprendido entre 100 y 200 y nos muestre todos los números pares comprendidos entre el número ingresado y 200. Por ejemplo, si el número ingresado es 192 nos debería mostrar 192, 194, 196, 198 y 200.


def brr():
    numero = int(input("Introduce un número par entre 100 y 200: "))
    while numero < 100 or numero > 200 or numero % 2 != 0:
        numero = int(input("Introduce un número par entre 100 y 200: "))
    for i in range(numero, 201, 2):
        print(i, end=", ")
brr()