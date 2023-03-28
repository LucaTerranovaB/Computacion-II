import os
import time
import sys

print("SOY EL PROCESO PADRE (PID: %d)" % os.getpid())
print("--------------------------------------------")

try:
    ret = os.fork()
except OSError:
    print("ERROR: no se ha podido crear el proceso hijo")
    
os.fork()

while True:
    if ret > 0:
        print("Soy el proceso padre (PID: %d)" % os.getpid())
#       sys.exit(0)
#       break (DEJAMOS HUERFANO AL HIJO)

    elif ret == 0:
        print("Soy el proceso hijo (PID: %d)" % os.getpid())
#        sys.exit()
#        break

    time.sleep(1)
    print("")