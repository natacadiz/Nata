# Reescribe el programa del cálculo del coste de un servicio, para darle 1.5 veces la tarifa horaria para todas las horas trabajadas que 
# excedan de 40. 
# Horas de trabajo: 45 
# Coste por hora: 10 
# Importe total: 475.0 

costehora = 10
horastrabajo = int(input("Cuantas horas ha trabajado?: "))
recargo = 0 #Cuando introducimos 0, cuando no se cumpla la condicion, en la operacion se coloca 0.
diferenciatrabajo = 0 #Cuando introducimos 0, cuando no se cumpla la condicion, en la operacion se coloca 0.
if horastrabajo > 40:
    diferenciatrabajo = horastrabajo-40
    recargo = 1.5*(costehora)*diferenciatrabajo
print (costehora*(horastrabajo-diferenciatrabajo)+recargo)