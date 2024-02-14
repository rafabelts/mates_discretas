'''
    escribe un programa que diga si un entero es par
'''

numero = int(input("Ingrese un número: "))

terniario = f"{numero} es un numero par" if numero % 2 == 0 else f"{numero} es un numero impar"

print(terniario)
