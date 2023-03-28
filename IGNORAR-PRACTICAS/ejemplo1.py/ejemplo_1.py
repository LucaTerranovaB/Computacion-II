'''
Ejemplo de codigo secuencial
Las instrucciones se van ejecutando una detras de la otra

NOTAS: mientras se ejecuta el codigo correr "ps fax|grep python" en otra terminal

'''

import time
import os

print("INICIO")
print("PID: %d -- PPID: %d" % (os.getpid(), os.getppid()))

for i in range(5,0,-1):
    print(i)
    time.sleep(1)
    

print("\nFIN")
print("PID: %d -- PPID: %d" % (os.getpid(), os.getppid()))


