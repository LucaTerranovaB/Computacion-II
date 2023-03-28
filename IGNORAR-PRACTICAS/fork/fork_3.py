import os
import time
import sys

print("SOY EL PROCESO PADRE (PID: %d)" % os.getpid())
print("--------------------------------------------")

ret = os.fork()

for i in range(10):
    
    if ret > 0:
        print("Soy el proceso padre (PID: %d)" % os.getpid())
    
    elif ret == 0:
        print("Soy el proceso hijo (PID: %d)" % os.getpid())    
        sys.exit(0)
    
    
    time.sleep(1)
    print(" ")

print(os.wait())    