def num_max_min(a, b, c):
    if a > b and a > c:
        print ("El mayor es", a, "y el menor", c) 
    elif b > a and b > c:
        print ("El mayor es", b, "y el menor", c)
    elif c > a and c > b:
        print ("El mayor es", c, "y el menor", b)
    else:
        print ("Son iguales")
num_max_min(4,2,1)