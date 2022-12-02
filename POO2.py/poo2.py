class Carrera:

    def __init__(self, nombre, materia):
        self.nombre = nombre
        self.materia= materia



class Materia:
    def __init__(self, nombre_materia, profesor):
        self.nombre_materia = nombre_materia
        self.profesor = profesor

class Horario(Materia):
    def __init__(self, nombre_materia, profesor, dias, horas):
        super().__init__(nombre_materia, profesor)
        self.dias = dias
        self.horas = horas


    def asignarHorario(self):
        print("El profesor {}". format(self.profesor))
        print("brinda la materia de {}". format(self.nombre_materia))
        print("con una carga horaria de {} horas". format(self.horas))
        print("los dias  {}". format(self.dias))




horario1 = Horario("sistemas operativos","Diego ","lunes", 3 )
print(horario1.profesor)
horario1.asignarHorario()
 







"""
    def __init__(self, dias, horas):
        super.__init__(nombre_profesor):
       self.dias = dias
        self.nombre = nombre
        self.horas = horas
        
 """

    

