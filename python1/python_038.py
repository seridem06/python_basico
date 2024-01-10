#determina si un numero es divisible por 5 y 7

numero = int(input("ingresa un numero: "))

if numero % 5 == 0 and numero % 7 == 0:
    print("es divisible entre 5 y 7")
else:
    print("no es divisible entre 5 y 7")