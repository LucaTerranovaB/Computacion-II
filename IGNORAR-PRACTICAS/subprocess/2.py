'''En general, no es posible que dos procesos hijos o nietos lean el mismo pipe del proceso padre
simultáneamente, ya que el pipe solo puede tener un extremo de escritura y un extremo de lectura.
Sin embargo, existen técnicas para permitir que varios procesos lean del mismo pipe, como por ejemplo, 
utilizando múltiples pipes o compartiendo un descriptor de archivo entre los procesos.

Una posible solución es crear múltiples pipes para cada proceso hijo y el padre escribirá en cada uno de ellos.
Los procesos hijos leerán cada uno su propio pipe y procesarán la información de manera independiente.'''






import os

# Crear los pipes
pipes = []
for i in range(2):
    r, w = os.pipe()
    pipes.append((r, w))

# Crear los procesos hijos
for i in range(2):
    pid = os.fork()

    if pid == 0:
        # Este es el proceso hijo

        # Cerrar los extremos de escritura de los otros pipes
        for j in range(2):
            if j != i:
                os.close(pipes[j][1])

        # Leer del extremo de lectura del pipe
        r = os.fdopen(pipes[i][0])

        # Leer cada línea del pipe
        for line in r:
            # Contar las palabras en la línea
            word_count = len(line.split())

            # Mostrar el resultado
            print(f"Hijo {i+1}: La línea tiene {word_count} palabras.")

        # Cerrar el extremo de lectura del pipe
        r.close()

        # Salir del proceso hijo
        os._exit(0)

# Este es el proceso padre

# Cerrar los extremos de lectura de los pipes
for i in range(2):
    os.close(pipes[i][0])

# Abrir el archivo de texto
with open("./archivo.txt", "w+") as f:
    # Leer cada línea del archivo
    for line in f:
        # Escribir la línea en cada pipe
        for i in range(2):
            os.write(pipes[i][1], line.encode())

# Cerrar los extremos de escritura de los pipes
for i in range(2):
    os.close(pipes[i][1])
