#determina si un año es bisiesto

anio = int(input('Ingresa un año: '))

if (anio % 4 == 0 and anio % 100 != 0) or \
    (anio % 400 == 0):
    print('es un año bisiesto')
else:
    print('no es bisiesto')
