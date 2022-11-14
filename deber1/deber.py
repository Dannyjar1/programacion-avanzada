

print("ejercicio 1")
a= int (input("Ingrese el primer numero: "))
b= int (input("Ingrese el segundo numero: "))
producto = 0 

for c in range(1,b+1,1):
    producto = producto + a
    print("El valor es: ",producto)



print("ejercicio 2")
palabra=input("Escribe tus nombres :")
 
for i in range(len(palabra),0,-1):
    print (palabra[i-1])


print("ejercicio 3 ")
lista = []
cantidad = int(input("cantidad: "))
mayor = 0
menor = 0
i = 1
while (cantidad > 0):
    numero = float(input("numero #" + str(i)+ ":"))
    lista.append(numero)
    i = i + 1
    cantidad = cantidad -1
mayor = max(lista)
menor = min(lista)

print("lista: ", lista)
print("mayor: ", mayor)
print("menor: ", menor)


print("ejercicio 4")
import math
from sys import prefix
print("Ingrese el radio del circulo: ")
r = float(input())
a = math.pi * (r * r)
print( "El area del circulo con radio ",r,"Es: ",round(a, 2))


print("ejercicio 5")
print("ingrese la edad de la persona")
edad = int(input())
if edad >= 18:
    print("la persona es mayor de edad")
else:
    print("la persona es menor de edad")


print("ejercicio 6")

numero = int(input("Ingresa un número: "))
if numero % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")



print("ejercicio 7")
def contar_vocales(cadena):
	contador = 0
	for letra in cadena:
		if letra.lower() in "aeiou":
			contador += 1
	return contador

cadena = "estas no son horas de llamar"
cantidad = contar_vocales(cadena)
print(f"En la cadena '{cadena}'' hay {cantidad} vocales")


print("ejercicio 8")
print("Ingrese la cantidad de numeros que desea sumar: ")
a = int(input())
b =0
for i in range(1, a+1):
    print(i)
    b=b+i
print("la suma es: ",b)



print("ejercicio 9")
def calificacion(nota):
    if(nota==10 or nota>=9):
        valor = "A"
    elif(nota<9 and nota>=8):
        valor = "B"
    elif(nota<8 and nota>=7):
        valor = "C"
    elif(nota<7 and nota>=6):
        valor = "D"
    elif(nota<6 and nota>=0):
        valor= "F"
    else:
        valor = "valor desconocido"
    return valor

print(calificacion(5))




print("ejercicio 10")

num=5
for i in range(1,num+1):
    print(num-i)



print("ejercicio 11")
suma = 0
i = 0

while i< 10: 
       i = i+1
       print(i)
   


print("ejercicio 12")

class Recatangulo:
    def __init__(self,ancho,alto):
        self.ancho=ancho
        self.alto=alto
    def area(self):
        area=self.alto*self.ancho
        return area
    def perimetro(self):
        perimetro=(self.alto*2)+(self.ancho*2)
        return perimetro
r1=Recatangulo(6,2)
area=r1.area()
perimetro=r1.perimetro()
print("El area es:",area)
print("El perimetro es:",perimetro)



print("ejercicio 13")
for n in range(10):
    if n % 3 ==0: 
        print(n)



print("ejercicio 14")

titulo = "La emancipada"
autor = "Miguel Rifrio"
print("El titulo es: ", titulo)
print("El autor es: ",autor)


print("ejercicio 15")

num1 = int(input("Ingresa el primer numero: ")) 
num2 = int(input("Ingresa el segundo numero: "))
if num1>num2:
  print('El primer número es mayor.')
elif num1<num2:
  print('El primer número es menor.')
else:
  print('Es el mismo número.')


print("ejercicio 16")
tupla = [13,1,8,3,2,5,8]
for tupla in tupla: 
    if tupla < 5: 
       print(tupla)


print("ejercicio 17")
def potencia(base, exponente):
    contador = 1  
    elevado = 1  
    while contador <= exponente:
        elevado = elevado * base
        contador = contador + 1
    return elevado
print(potencia(2, 3))


print("ejercicico 18")
numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))
print("la suma es ",numero1 + numero2)



print("ejercicio 19")

numero = int(input("Ingrese el valor de 5 cifras: "))

c5 = numero % 10
c4 = int((numero % 100)/10)
c3 = int((numero % 1000)/100)
c2 = int((numero % 10000)/1000)
c1 = ((numero - (numero % 10000)) /10000)


print(str(c5)+str(c4)+str(c3)+str(c2)+str(c1))



print("ejercicio 20")
nombre = input("Cuál es tu nombre: ")
print("Hola soy Danny, que tengas un buen dia ")

