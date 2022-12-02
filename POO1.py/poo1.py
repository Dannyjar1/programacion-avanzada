class Cliente():

    def __init__(self, name, identificacion, email, edad):
        self.name = name
        self.identificacion = identificacion
        self.email = email
        self.edad = edad


    def __str__(self):
        return "This class is a example of client"

    def esMayor(self, edad):
        if self.edad >= 18:
            print("{} es mayor de edad ". format(self.edad))
        else:
            print("{} es menor de edad ". format(self.edad))


Danny = Cliente("Danny", 1105615536,"dannyjaramillofran@gmail.com",19)
         
print(Danny.calcularEdad())