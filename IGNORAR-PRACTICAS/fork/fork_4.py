import os
import time
import sys

def main():
    
    fd = open("./archivo.txt", "w+")
    
    pid = os.fork()
    
    if (pid):
        print("Soy el proceso padre (PID: %d)" % os.getpid())
        time.sleep(1)
        fd.seek(0)
        print(fd.read())
        
        
    else:
        print("Soy el proceso hijo (PID: %d)" % os.getpid())
        fd.write("ESTA ES UNA LINEA DEL HIJO")
        fd.flush()
        
        time.sleep(3)
        sys.exit(0)

if __name__ == "__main__":
    main()