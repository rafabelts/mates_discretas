def factores(n):
    for i in range(2, n + 1):
        while n % i == 0:
            print(i)
            n //= i


try:
    num = int(input("Ingresa un número: "))
    factores(num)
except Exception:
    print("Ingresa un número entero")
