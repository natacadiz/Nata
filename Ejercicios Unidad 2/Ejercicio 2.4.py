# Escribe un programa que solicite un número al usuario e indique si es par o impar.

numero = int(input("Introduzca un numero: "))
if numero % 2 == 0: # El simbolo porcentaje indica el resto, los simbolos == se utiliza cuando el caracter es igual a...
    print ("Par!")
if numero % 2 == 1:
    print ("Impar!")