"""
Escribir un programa que pida al usuario dos números 
enteros y muestre por pantalla la <n> entre <m> da un 
cociente <c> y un resto <r> donde <n> y <m> son los 
números introducidos por el usuario, y <c> y <r> son el 
cociente y el resto de la división entera 
respectivamente.
"""

num1 = int(input("ingrese el numero: "))
num2 = int(input("ingrese el numero: "))
resp = int(num1) // int(num2)
c = resp
resto = int(num1) % int(num2)
print(resp, c , resto)
