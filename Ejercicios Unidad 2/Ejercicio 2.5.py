# Escribe un programa que solicite tres números al usuario y muestre el mayor de ellos. 

numero1 = int(input("Introduce un primer numero: "))
numero2 = int(input("Introduce un segundo numero: "))
numero3 = int(input("Introduce un tercer numero: "))
if numero1 > numero2 and numero1 > numero3:
    print (numero1) # en los print, las variables SIEMPRE van entre parentesis.
if numero2 > numero1 and numero2 > numero3:
    print (numero2)
if numero3 > numero1 and numero3 > numero2:
    print (numero3)