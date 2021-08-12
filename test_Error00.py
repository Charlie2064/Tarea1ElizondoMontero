#Un caso negativo donde se verifica el punto "a" del método multiple_op

import pytest #Librerías
import numpy as np


n = "A" #Parámetro que no es un número para fallar el test
f = 1 #Valor donde debe empezar para calcular el factorial
array = []

a = np.random.randint (1, 11) #Números random para el arreglo de entrada
b = np.random.randint (1, 11)
c = np.random.randint (1, 11)
d = np.random.randint (1, 11)

rand = [a, b, c, d] #Se crea el arreglo random

def multiple_op (n, f, array): 
    for i in range (1, n+1): #Función facotrial
        f = f * i #empezando en 1, multiplico por el valor anterior y sumo

    x = n * n #Multiplicación
    y = 2 ** n #Potencia

    array = [x, y, f] #Arreglo de salida

    return ("Dado el Parámetro n =", n, ":")                        
    return (array)


def verify_array_op (rand): #Función para el arreglo de entrada
    r = 1 #Valores iniciales para cálculo de factoriales
    s = 1
    t = 1
    u = 1

    for i in range (1, a + 1): #Mismo razonamiendo para factoriales
        r = r * i

    for i in range (1, b + 1):
        s = s * i
        
    for i in range (1, c + 1):
        t = t * i
        
    for i in range (1, d + 1):
        u = u * i
    
    z = [[a * a, 2 * a, r], [b * b, 2 * b, s], [c * c, 2 * c, t], [d * d, 2 * d, u]] #Array de arrays
    return ("Dado el arreglo: ")
    return (rand)
    return (z)


def test ():
    assert type (n) == int, "ERROR #00" #Error para cuando parámetro inicial no es un número
    
    assert type (a) == int, "ERROR #01" #Errores para cuando algún parámetro dentro del arreglo no es un número
    assert type (b) == int, "ERROR #01"
    assert type (c) == int, "ERROR #01"
    assert type (d) == int, "ERROR #01"

    multiple_op (n, f, array) #Llama a las funciones
    verify_array_op (rand)
