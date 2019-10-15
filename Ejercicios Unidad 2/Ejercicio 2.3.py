# Escribe un programa que solicite una puntuación entre 0.0 y 1.0. Si la puntuación está fuera de ese rango, muestra un mensaje de error. 
# Si la puntuación está entre 0.0 y 1.0, muestra la calificación usando la tabla siguiente (el programa debe mostrar la tabla usando tabuladores): 
# Puntuación Calificación 
# >= 0.9 Sobresaliente 
# >= 0.8 Notable 
# >= 0.7 Bien 
# >= 0.6 Suficiente 
# < 0.6  Insuficiente 
# Introduzca puntuación: 0.95 
# Sobresaliente

puntuacion = float(input("Cual es su puntuacion?: "))
if puntuacion >= 0.9: # SIEMPRE se coloca dos puntos al terminar if, elif o else.
    print ("Sobresaliente!")
if puntuacion >= 0.8 and puntuacion < 0.9: # and se utiliza para añadir otra condicion.
    print ("Notable!")
if puntuacion >= 0.7 and puntuacion < 0.8:
    print ("Bien!")
if puntuacion >= 0.6 and puntuacion < 0.7:
    print ("Suficiente!")
if puntuacion < 0.6:
    print ("Insuficiente!")