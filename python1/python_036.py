#pide un caracter y determina si es vocal

caracter = input("ingresa caracter: ")
vocales = ["a","e","i","o","u"]

if caracter.lower() in vocales:
    print("ingresa una vocal")
else:
    print("no es una vocal")