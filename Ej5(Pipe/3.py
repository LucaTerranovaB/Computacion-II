import subprocess
import os


# Crear el pipe
r, w = os.pipe()

# Crear el proceso hijo
pid = os.fork()

if pid == 0:
    # Este es el proceso hijo
    
    # Cerrar el extremo de escritura del pipe
    os.close(w)
    
    # Leer del extremo de lectura del pipe
    r = os.fdopen(r)
    
    # Leer cada línea del pipe
    for line in r:
        # Contar las palabras en la línea
        word_count = len(line.split())
        
        # Mostrar el resultado
        print(f"La línea tiene {word_count} palabras.")
    
    # Cerrar el extremo de lectura del pipe
    r.close()
else:
    # Este es el proceso padre
    
    # Cerrar el extremo de lectura del pipe
    os.close(r)
    
    # Escribir en el extremo de escritura del pipe
    a = input("Escriba algo: ")
    w = os.fdopen(w, "w")
    w.write(a) 
    
    # Verificar la existencia del pipe
    pid_dir = f"/proc/{pid}/fd/"
    print(f"El pipe existe en el directorio {pid_dir}:")
    os.system(f"ls -l {pid_dir}")
    
    # Cerrar el extremo de escritura del pipe
    w.close()
