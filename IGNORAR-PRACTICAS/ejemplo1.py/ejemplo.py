import os
import time
from subprocess import Popen



#for i in range(2):
#    os.system("python3 ejemplo_1.py")
    
Popen(["python3", "ejemplo_1.py"])
print("HOLA")

time.sleep(1)
print("FIN DEL PROCESO PADRE")