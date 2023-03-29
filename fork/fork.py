import argparse
import math
import os
import sys
import time


#Parser: Biblioteca que define y analiza argumentos en la linea de comandos
#Se crea un objeto de tipo parser
#Con parser.add()_argument() se definen los argumentos que se van a recibi.remove()

parser = argparse.ArgumentParser()
parser.add_argument("-f", action="store_true", help="Fork the process")
parser.add_argument("number", type=float, help="Number to calculate the square root")
archivo = "/home/b/Documentos/GitHub/Computacion-II/fork/archivo"

print("---------------------------------------------------------------------")

args = parser.parse_args()

archivo = archivo + ".txt"

#Se crea un try-except para que si el numero es negativo, no se muestre el error en la terminal
try:
    if args.number:
        
        
        
        
        #Fork: Crea un proceso hijo que es una copia del proceso padre
        ret = os.fork()
         
        
        if ret > 0:
            # Proceso padre
            print("Soy el proceso padre (PID: %d)" % os.getpid(), " y mi hijo es: ", ret)
            result = -math.sqrt(args.number)
            print(f"Raiz cuadrada negativa {args.number} es {result:.2f}")
        elif ret == 0:
            # Processo hijo
            time.sleep(1)
            print("Soy el proceso hijo (PID: %d)" % os.getpid(), " y mi padre es: ", os.getppid())
            result = math.sqrt(args.number)
            print(f"Raiz cuadrada positiva {args.number} es {result:.2f}")
    
        time.sleep(1)

#Si el numero es negativo, se imprime el error en el archivo de errores
# Y NO MUESTRA VALUEERROR EN LA TERMINAL
except ValueError:
    with open(archivo, 'a') as e:
        e.write(f'No se puede calcular la raíz cuadrada de un número negativo: {args.number}.\n')
        sys.stderr.write(f'No se puede calcular la raíz cuadrada de un número negativo: {args.number}. Se escribió el error en "archivo".\n')
    





time.sleep(1)

print("---------------------------------------------------------------------")    
