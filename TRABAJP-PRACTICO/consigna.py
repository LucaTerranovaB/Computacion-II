'''----------------------------------------------------------------------------'''

## TP1

"Fecha de entrega : 02/05/2023"

### REQUERIMIENTOS

#Escribir un programa que abra un archivo de texto pasado por un argumento utilizando el modificador -f
#El programa debera generar tanbtos procesos hijos como lineas tenga el archivo de texto
#El programa debera enviarle, via pipes (os.pipe()), cada linea del archivo a un hijo
#Cada hijo debera invertir el orde las letras de la linea recibida, y luego se lo Enviara al padre
##nuevamente usando pipes
# El proceso padre debera esperar a que terminen todos los hijos, y mostrara por pantalla las lineas invertidas
#Debe manejar los Errores


### EJEMPLO MODO DE USO
'''*----------------------------------------'''
##CONTENIDO DEL ARCHIVO DE TEXTO /tmp/texto.txt

##hola mundo
##que tal
##Este es un archivo
##De ejemplo


### EJECUCION
'''------------------------------------------'''

## python3 inversor.py -f /tmp/texto.txt
## odnum aloh
## lat euq
## oiracra nu se etsE
## ojelpmeD

'''------------------------------------------'''

###OBJETIVOS

#Manejo de Archivos
#Creacion de Procesos
#Usos de mecanismnos de IPC


#BONUS TRACK

#Realizar la misma aplicacion pero usando multiprocesiig

'''-----------------------------------------------------------------------------------------'''

#PROGRAMA------------------------------------------------------------


