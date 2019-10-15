# Escribe un programa que pida el importe sin IVA de un artículo y el tipo de IVA a aplicar y calcule e imprima por pantalla el precio final del artículo.
 
siniva=float(input("Introduca el importe del articulo sin iva: "))
iva=0.21*siniva
coniva=siniva+iva
print ("El importe del articulo con iva es de",coniva,"euros iva incluido.")