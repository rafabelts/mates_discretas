def euclides(num_1, num_2):
    if num_2 == 0:
        return num_1
    else:
        return euclides(num_2, num_1 % num_2)


num_1 = int(input("Ingresa el primer número: "))
num_2 = int(input("Ingresa el segundo número: "))

mcd = euclides(num_1, num_2)

print(f"{num_1} | {num_2}: MCD = {mcd}")
