"""
Haz una tabla de multiplicar utilizando el ciclo for.
"""

for num in range(1, 13):
    for num1 in range(1, 13):
        print(num*num1, end="\t")
    print("")