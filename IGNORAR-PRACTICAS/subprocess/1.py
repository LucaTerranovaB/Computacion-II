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
    
    # Abrir el archivo de texto
    with open("archivo.txt", "r") as f:
        # Leer cada línea del archivo
        for line in f:
            # Escribir la línea en el pipe
            os.write(w, line.encode())
    
    # Cerrar el extremo de escritura del pipe
    os.close(w)
