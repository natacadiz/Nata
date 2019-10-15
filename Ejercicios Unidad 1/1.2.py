#Escribe un programa para pedirle al usuario las horas de trabajo y el precio por hora y calcule el importe total del servicio. 
# Horas de trabajo: 6 
# Coste por hora: 10 
# Importe total: 60
 
horas=int(input("Cuantas horas ha trabajado?: "))
coste=int(input("Cual es el precio de la hora?: "))
total=horas*coste
print ("El importe total es",total,"euros")