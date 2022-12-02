"""
Crear un script que indique si el usuario es
 mayor de edad, menor de edad o
 es parte de la tercera edad.
  Puede utilizar la siguiente tabla.
"""

edad = int(input("¿Cuál es tu edad? "))
if edad < 18: 
    print ("Eres menor a 18.")

elif edad >=18 and edad <=49 :
    print("Mayor de edad ")

elif edad >49 and edad<=120:
    print ("Tercera edad ")

else:
    print("No existe en este rango .")