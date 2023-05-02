


import argparse
import os
import sys
from multiprocessing import Process, Pipe

def invertir_linea(linea):
    """
    Invierte el orden de las letras de una línea.
    """
    return linea[::-1]

def procesar_linea(linea, pipe):
    """
    Procesa una línea del archivo. Invierte el orden de sus letras y la envía al padre a través del pipe.
    """
    linea_invertida = invertir_linea(linea)
    pipe.send(linea_invertida)


parser = argparse.ArgumentParser(description='Invierte el orden de las letras de cada linea de un archivo de texto')
parser.add_argument('-f', '--file', required=True, help='Archivo de texto a invertir')
args = parser.parse_args()
# Manejo de errores: Verificar que el archivo existe
if not os.path.exists(args.file):
    print(f'El archivo "{args.file}" no existe', file=sys.stderr)
    sys.exit(1)
# Leer las líneas del archivo
with open(args.file) as f:
    lineas = f.readlines()
# Crear un pipe por cada línea
pipes = [Pipe() for _ in range(len(lineas))]
# Crear un proceso hijo por cada línea del archivo
hijos = []
for i, linea in enumerate(lineas):
    hijo = Process(target=procesar_linea, args=(linea, pipes[i][1]))
    hijo.start()
    hijos.append(hijo)
# Leer las líneas invertidas de los pipes y mostrarlas por pantalla
for i, pipe in enumerate(pipes):
    linea_invertida = pipe[0].recv()
    print(f'{linea_invertida}', end='\n',)
    
    
# Esperar a que terminen todos los procesos hijos
for hijo in hijos:
    hijo.join()
#Mostrar las lineas sin invertir
print('\n')
print('Lineas sin invertir')
print('\n')
for linea in lineas:
    print(f'{linea}', end='')
sys.exit(0)


