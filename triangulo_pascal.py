def factores(n):
    if n <= 1:
        return 1
    else:
        return n * factores(n - 1)

def piramide_pascal(n):
    for i in range(n):
        return factores(i) // factores(i) * factores(i - n)


print(piramide_pascal(7))

