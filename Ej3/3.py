import sys
import argparse

# Crear el parser de argumentos
parser = argparse.ArgumentParser(description='Contar palabras y líneas en un archivo de texto.')
parser.add_argument('archivo', help='el archivo de texto a analizar')
parser.add_argument('-a', '--avg-length', action='store_true', help='imprimir la longitud promedio de las palabras')
args = parser.parse_args()

# Abrir el archivo
try:
    with open(args.archivo, 'r') as f:
        # Leer el archivo línea por línea
        num_lineas = 0
        num_palabras = 0
        longitud_total = 0
        for linea in f:
            num_lineas += 1
            # Contar las palabras en la línea
            palabras = linea.split()
            num_palabras += len(palabras)
            longitud_total += sum(len(palabra) for palabra in palabras)
        
        # Imprimir los resultados
        print(f'Número de líneas: {num_lineas}')
        print(f'Número de palabras: {num_palabras}')
        if args.avg_length:
            # Calcular la longitud promedio de las palabras
            if num_palabras > 0:
                longitud_promedio = longitud_total / num_palabras
                print(f'Longitud promedio de las palabras: {longitud_promedio:.2f}')
            else:
                print('No se encontraron palabras en el archivo.')
except FileNotFoundError:
    # Si el archivo no existe, escribir el error en el archivo de errores
    with open('errors.log', 'a') as f:
        f.write(f'No se encontró el archivo "{args.archivo}".\n')
        sys.stderr.write(f'No se encontró el archivo "{args.archivo}". Se escribió el error en "errors.log".\n')
