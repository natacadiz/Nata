# Escribe un programa que solicite dos números al usuario y le permita decidir si sumarlos, restarlos, multiplicarlos o dividirlos. 
# El programa debe controlar todos los errores posibles. 

numero1 = int(input("Introduzca un numero: "))
numero2 = int(input("Introduzca de nuevo un numero: "))
operacion = (input("Que operacion quiere realizar?: "))
if operacion == "sumar":
    print (numero1+numero2)
if operacion == "restar":
    print (numero1-numero2)
if operacion == "multiplicar":
    print (numero1*numero2)
if operacion == "dividir":
    print (numero1/numero2)