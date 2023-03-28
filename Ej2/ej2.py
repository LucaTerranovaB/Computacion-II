#!/usr/bin/ python3

import sys

# Obtener los argumentos de línea de comando
args = sys.argv

# Verificar si se ingresaron los dos argumentos requeridos
if len(args) != 3:
    print("Se requieren dos argumentos: una cadena de texto y un número entero.")
    sys.exit()

# Obtener la cadena de texto y el número entero
text = args[1]
num = int(args[2])

# Imprimir la repetición de la cadena de texto
print(text * num)


'''
python3 ej2.py hola 20       ░▒▓ ✔ 
holaholaholaholaholaholaholaholaholaholaholaholaholaholaholaholaholaholaholahola

'''