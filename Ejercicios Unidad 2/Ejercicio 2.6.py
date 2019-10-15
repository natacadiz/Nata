# Escribe el programa anterior usando solamente dos variables.

numero1 = int(input("Introduce un primer numero: "))
numero2 = int(input("Introduce un segundo numero: "))
if numero1 > numero2:
    numero2 = int(input("Introduce otro numero: "))
    if numero1 > numero2:
        print (numero1)
    else:
        print (numero2)
else:
    numero1 = int(input("Introduce otro numero: "))
    if numero1 > numero2:
        print (numero1)
    else:
        print (numero2)