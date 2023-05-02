import argparse
import os
import sys
from multiprocessing import Process, Pipe
import multiprocessing
import subprocess

parser = argparse.ArgumentParser(description='Invierte el orden de las letras de cada linea de un archivo de texto')
parser.add_argument('-f',dest="/tmp/texto.txt" , required=True, help='Archivo de texto a invertir')
archivo= "/tmp/texto.txt"
args = parser.parse_args()




#Abrir el archivo

try:
    with open(archivo, 'r') as f:
        lineas = f.readlines()
        #Invertir el orden de las letras de cada linea
        
        for linea in lineas:
            linea = linea[::-1]
            print(linea)
        
except FileNotFoundError:
    print('El archivo no existe')
    sys.exit(1)



def invertir_linea(linea):
    """Invierte el orden de las letras de una línea."""
    return linea.strip()[::-1]

def procesar_archivo(archivo):
    """Procesa el archivo de texto y envía cada línea a un proceso hijo para invertirla."""
    with open(archivo) as f:
        lineas = f.readlines()
    
    # Crear un pipe para cada proceso hijo.
    pipes = [os.pipe() for _ in range(len(lineas))]
    
    # Crear un proceso hijo por cada línea del archivo.
    hijos = []
    for i, linea in enumerate(lineas):
        hijo = os.fork()
        if hijo == 0:  # Proceso hijo.
            # Cerrar los pipes que no va a usar este hijo.
            for j, (r, w) in enumerate(pipes):
                if j != i:
                    os.close(r)
                    os.close(w)
            
            # Invertir la línea y enviarla al padre.
            linea_invertida = invertir_linea(linea)
            os.close(pipes[i][0])
            os.write(pipes[i][1], linea_invertida.encode())
            os.close(pipes[i][1])
            
            sys.exit(0)
        else:  # Proceso padre.
            hijos.append(hijo)
    
    # Cerrar los pipes que no va a usar el padre.
    for r, w in pipes:
        os.close(w)
    
    # Leer las líneas invertidas de los pipes y mostrarlas por pantalla.
    for i, (r, w) in enumerate(pipes):
        os.close(w)
        linea_invertida = os.read(r, 1024).decode()
        os.close(r)
        print(f"Línea {i+1}: {linea_invertida}", end="")
    
    # Esperar a que terminen todos los procesos hijos.
    for hijo in hijos:
        os.waitpid(hijo, 0)
        
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", dest="/tmp/texto.txt", required=True,
                        help="archivo de texto a procesar")
    args = parser.parse_args()
    
    try:
        procesar_archivo(args("/tmp/texto.txt"))
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)



