def checar_numero_perfecto(n):
    suma = 1
    for i in range(2, n):
        if n % i == 0:
            suma += i
    return suma == n


def imprimir_perfectos_hasta_n(n):
    for i in range(n+1):
        if checar_numero_perfecto(i):
            print(i)


try:
    num = int(input("Ingrese que número quiere comprobar si es perfecto: "))
    if checar_numero_perfecto(num):
        print(f"{num} es un número perfecto")
    else:
        print(f"{num} no es un número perfecto")

    num_para_serie = int(input("Ingrese hasta que numero quiere imprimir los perfectos: "))
    imprimir_perfectos_hasta_n(num_para_serie)

except Exception:
    print("Error, ingrese un numero entero")
