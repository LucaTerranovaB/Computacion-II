#1- Escribir un programa en Python que acepte un número de argumento entero positivo n y genere una lista de los n primeros números impares. El programa debe imprimir la lista resultante en la salida estandar.


def odd_numbers(n):
    """Generates a list of the first n odd numbers"""
    return [i for i in range(n*2) if i % 2 != 0]

print(odd_numbers(5))

