
#1 calcular los primeros 50 numeros impares 
print("ejercicio 1")

i= 1
while i <50: 
    print (i)
    i+=2


# calcular los primeros 20 numeros pares, pero retirar el 10

print("ejercicio 2")

i= 0
while i <20: 
    i+=2
    if i == 10:
        continue
    print(i)

#calcular los multiplos de 5 pero detener en el 3ro

print("ejercicio 3")

i=5
while i <= 50:
    print (i)
    if i== 20: 
        break
    i+=5
