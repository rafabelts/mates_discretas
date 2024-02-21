def sumar_divisores(n):
    suma = 1
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            suma += i
    return suma


def comprobar_si_son_amigos(n1, n2):
    suma_divisores_n1 = sumar_divisores(n1)
    suma_divisores_n2 = sumar_divisores(n2)
    return suma_divisores_n1 == n2 and suma_divisores_n2 == n1


try:
    num_1 = int(input("Ingresa el primer número: "))
    num_2 = int(input("Ingresa el segundo número: "))

    if comprobar_si_son_amigos(num_1, num_2):
        print(f"{num_1} y {num_2} son números amigos")
    else:
        print(f"{num_1} y {num_2} no son números amigos")
except Exception:
    print("Error, recuerda ingresar enteros")
