edad = int(input("Ingrese su edad para saber si puede sacar su licencia: "))

while edad < 18:
    print ('Usted no puede sacar su licencia :(')
    break

if edad >= 18:
    print('!Usted puede sacar su licencia! !FELICIDADES!')

