'''
1-Escribir un programa que ralice una multiplicacion de 2 matrices de 2x2. Cada elemento debera 
calcularse en un proceso distinto devolviendo el resultado en una fifo indicando el indice del elemento
El padre debera leer en la fifo y mostrar el resultado final

'''

import os
import sys
import multiprocessing

def trabajador(row, col, a, b, resultado_pipe):
    
    #Calcula el elemento de la matriz den la fila "row",columna "col"
    result= a[row][0]*b[0][col] + a[row][1]*b[1][col]
    resultado_pipe.send([row,col,result])
    

def matriz():
    
    a= [[1,2],[2,1]]
    b= [[5,5],[5,5]]
    
    #Crea procesos de los trabajadores
    
    resultado_pipes=[]
    
    for i in range(2):
        
        for j in range(2):
            
            resultado_pip = multiprocessing.Pipe()
            process = multiprocessing.Process(target=trabajador, args=(i,j,a,b,resultado_pipes[1]))
            process.start()
            resultado_pipes.append(resultado_pip[0])
            
   #Leer resultados de los procesos y contruir la matriz
   
    result = [[0,0],[0,0]]
    
    for i in range (4):
        
        row,col,value = resultado_pipes[i].recv()
        result[row][col] = value
          
    print(result)
    
if __name__ == '__main__':
    
    matriz()
      