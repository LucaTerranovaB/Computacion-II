#1- Escribir un programa en Python que acepte un número de argumento entero positivo n y genere una lista de los n primeros números impares. El programa debe imprimir la lista resultante en la salida estandar.

#!/bin/bash python3 

def odd_numbers(n):
    """Generates a list of the first n odd numbers"""
    return [i for i in range(n*2) if i % 2 != 0]

print(odd_numbers(5))

'''
~/Do/G/Computacion-II/Ej1 │ main !1 ▓▒░ python3 ej1.py args 5
[1, 3, 5, 7, 9]

 ~/Do/G/Computacion-II/Ej1 │ main !1 ▓
 '''