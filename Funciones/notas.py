"""pedir una nota al usuario 
si la nota es menor a 10 y mayor o igual a 9, imprimir exelente
si la nota es menor a 9 y mayor o igual a 8, imprimir Muy bueno
si la nota es menor a 8 y mayor o igual a 7, imprimir bueno
si la nota es menor a 7, imprimir reprobado 

"""


nota = int(input("ingrese una nota: "))

def calificacion(int:nota):
    global nota
    if(nota==10 or nota>=9):
        valor= "exelente"
    elif(nota<9 and nota>=8):
        valor = "muy buena"
    elif(nota<8 and nota >=7):
        valor = "bueno"
    elif(nota<7 and nota >=0):
        valor = "reprobado"
    else:
        valor = "es otro valor"
    return(valor)

print(calificacion(nota))