'''
    El triángulo de pascal fue descubierto por Blaise Pascal en el siglo XII.

    Es simétrico en relación con el eje vertical que pasa por el centro, siendo simétrico de izquierda a derecha.
    
    En computación se utiliza en la teoría de la información para calcular la cantidad de información que se puede almacenar en un sistema.
    
    En cada fila del triángulo de pascal encontramos coeficientes binomiales, que son utilizados para expandir binomios elevados a una potencia, y son representados en el triangulo 
'''

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


def coeficiente_binomial(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))


def triangulo_pascal(n):
    for i in range(n + 1):
        for j in range(i + 1):
            print(coeficiente_binomial(i, j), end=",  ")
        print()


try:
    num_de_pisos = int(input("Ingrese el numero de piso que quiere ver: "))
    print("Su triángulo de pascal:\n")
    triangulo_pascal(num_de_pisos)
except Exception:
    print("Error, ingresa un número entero")
