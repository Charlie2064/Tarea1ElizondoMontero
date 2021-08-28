#Importar Librerias
from threading import Thread
from time import time
import numpy as np
import argparse

#Arrays vacios
array=[]
cuadrado=[]
cuadrado2=[]

#Descripción de lo que hace el programa
parser = argparse.ArgumentParser(description="second power of elements in an array")

#Argumentos que recibe el programa
parser.add_argument("Elementos", metavar="Elementos", type=str, help="Enter Number of Elements or C to clear .txt file")
parser.add_argument("txt", nargs="?", metavar="txt", type=str, help="Enter T if you want a .txt file")
args = parser.parse_args()

#Q guarda el parametro opcional introducido
Q = args.txt
#se decide el valor de P de acuerdo con el parametro (str) fijo
if args.Elementos == "C":
    P = 0
#cambia el tipo de variable a int
else: 
    P = int(args.Elementos)

#Llena el array con valores de 0 a P
for i in range (0,P):
    array.append(i)
    i=i+1

#Marca el tiempo de inicio para un hilo
t1i = time()
#calculo potencia de cada elemento del array
for j in range (0,P):
    cuadrado.append(np.power(array[j],2))
    j=j+1

#Marca el tiempo donde termina para un hilo
t1f = time()
#Resta los valores de tiempo y calcula cuanto tiempo dura el proceso de un hilo
thilo1 = t1f - t1i


#Marca el tiempo de inicio para cuatro hilos
t4i = time()

#Divisiones para cada hilo
a = 0
b = (P//4)
c = (P//4)*2
d = (P//4)*3
e = P

#Numero de hilos
n = 4
hilos = list()

#Funcion de segmentacion a llamar en el ciclo de los cuatro hilos
def seg(vi, vf):
    for k in range (vi,vf):
        cuadrado2.append(np.power(array[k],2))
        k = k+1
        
#Ciclo de los cuatro hilos
#Los llama con thread para iniciar operacion en paralelo
for i in range(n-1):
    if i == 0:
        h = Thread(target=seg, args=(a,b))
    if i == 1:
        h = Thread(target=seg, args=(b,c))
    if i == 2:
        h = Thread(target=seg, args=(c,d))
    if i == 3:
        h = Thread(target=seg, args=(d,e))
  
#Union de los resultados de los hilos despues de correr la funcion target
    hilos.append(h)
  
#Comienza el thread llamando a la funcion target
    h.start()

#Los hilos que terminan antes, esperan a que los demas finalicen la tarea
for h in hilos:
    h.join()

#Marca el tiempo donde termina para cuatro hilos
t4f = time()
#Resta los valores de tiempo y calcula cuanto tiempo dura el proceso para cuatro hilos
thilo4 = t4f - t4i

#como el parametro fijo es "C" se limpia el .txt
if P == 0:
    f = open ("TextFile.txt", "w")
    f.truncate(0) 
    f.close()
    print(".txt file has been cleared")
else:
    print('Tiempo calculo con un hilo:',thilo1)
    print('Tiempo calculo con cuatro hilos:',thilo4)

#se escriben los datos en el .txt
if Q=="T":
    f = open ("TextFile.txt", "w")
    f.write('Tiempo calculo con un hilo: %s \nTiempo calculo con cuatro hilos: %s' % (thilo1,thilo4)) 
    f.close()


