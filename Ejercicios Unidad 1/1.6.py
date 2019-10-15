# Escribe un programa que pida el importe final de un artículo y calcule e imprima por pantalla el IVA que se ha pagado y el importe sin IVA 
# (suponiendo que se ha aplicado un tipo de IVA del 10%). 
 
precioconiva = float(input("Cuanto ha pagado usted por ese articulo?"))
ivapagado = (0.10*precioconiva)
print ("Usted ha pagado",ivapagado ,"euros de IVA")
preciosiniva = (precioconiva-ivapagado)
print ("El precio del articulo sin IVA es de" ,preciosiniva ,"euros")