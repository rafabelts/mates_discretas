def es_num_primo(n):
    primo = True
    for i in range(2, (n//2) + 1):
        if (n % i == 0):
            primo = False
            break
    return primo


def imprimir_primos(n):
    for i in range(2, n):
        if es_num_primo(i):
            print(i)


while True:
    try:
        num = int(input("Da un número: "))
        imprimir_primos(num)
        primo = es_num_primo(num)

        if primo:
            print(f"{num} es primo")
        else:
            print(f"{num} no es primo")
        break
    except Exception:
        print("Ingresa un número entero")
