import numpy as np  # Librerías

n = np.random.randint(1, 11)  # Función random
f = 1  # Valor donde debe empezar para calcular el factorial
array = []

a = np.random.randint(1, 11)  # Números random para el arreglo de entrada
b = np.random.randint(1, 11)
c = np.random.randint(1, 11)
d = np.random.randint(1, 11)

rand = [a, b, c, d]  # Se crea el arreglo random


def multiple_op(n, f, array):
    for i in range(1, n+1):  # Función facotrial
        f = f * i  # Empezando en 1, multiplico por el valor anterior y sumo

    x = n * n  # Multiplicación
    y = 2 ** n  # Potencia

    array = [x, y, f]  # Arreglo de salida

    print("Dado el Parámetro n =", n, ":")
    print(array)


def verify_array_op(rand):  # Función para el arreglo de entrada
    r = 1  # Valores iniciales para cálculo de factoriales
    s = 1
    t = 1
    u = 1

    for i in range(1, a + 1):  # Mismo razonamiendo para factoriales
        r = r * i

    for i in range(1, b + 1):
        s = s * i

    for i in range(1, c + 1):
        t = t * i

    for i in range(1, d + 1):
        u = u * i

    array1 = [a * a, 2 * a, r]
    array2 = [b * b, 2 * b, s]
    array3 = [c * c, 2 * c, t]
    array4 = [d * d, 2 * d, u]

    z = [array1, array2, array3, array4]  # Array de arrays
    print("Dado el arreglo: ")
    print(rand)
    print(z)


multiple_op(n, f, array)  # Llama a las funciones
verify_array_op(rand)
