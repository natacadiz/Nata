#Reescribe el programa del ejercicio 2.1 usando try y except, de modo que el programa sea capaz de gestionar entradas no numéricas mostrando un mensaje y saliendo del programa. 
# A continuación se muestran dos ejecuciones del programa: 
# Horas de trabajo: 20 
# Coste por hora: nueve 
# Error, por favor introduzca un número 
# Horas de trabajo: cuarenta 
# Error, por favor introduzca un número 

try:
    costehora = 10
    horastrabajo = int(input("Cuantas horas ha trabajado?: "))
    recargo = 0 #Cuando introducimos 0, cuando no se cumpla la condicion, en la operacion se coloca 0.
    diferenciatrabajo = 0 #Cuando introducimos 0, cuando no se cumpla la condicion, en la operacion se coloca 0.
    if horastrabajo > 40:
        diferenciatrabajo = horastrabajo-40
        recargo = 1.5*(costehora)*diferenciatrabajo
    print (costehora*(horastrabajo-diferenciatrabajo)+recargo)
except:
    print ("Introduzca un numero!")
finally:
    print ("El control de errores termino")