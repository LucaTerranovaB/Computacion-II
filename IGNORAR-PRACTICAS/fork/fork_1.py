import os

print("SOY EL PROCESO PADRE (PID: %d)" % os.getpid())
print("--------------------------------------------")

try:
    ret = os.fork()
except OSError:
    print("ERROR: no se ha podido crear el proceso hijo")

print(ret)

ret= os.fork()

if ret > 0:
    print("Soy el proceso padre (PID: %d)" % os.getpid())
    
elif ret == 0:
    print("Soy el proceso hijo (PID: %d)" % os.getpid())