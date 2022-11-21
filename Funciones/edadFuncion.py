#crear una funcion que permita conocer el rango de edad de una persona 

nombre = input("ingrese su nombre: ")
#rint(type(nombre))
edad = int(input("por favor ingrese su edad : "))
#print(type(edad))


def edadCalcular(int: edad):
    global edad
    if edad >= 18 and edad<= 65:
        print("es mayor de edad")
    elif edad >= 65:
        print(nombre,"usted forma parte de la 3ra edad ")
    else: 
        print("es menor de edad ")

edadCalcular(edad)