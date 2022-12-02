class Mascota():

    enfermedades = ["anemia", "moquillo", "ninguna"]
    activo = [ "activo", "muerto"]

    def __init__(self, nombre, edad, enfermedades, activo, responsable):

        self.nombre = nombre
        self.edad = edad
        self.enfermedades = enfermedades
        self.activo = activo
        self.responsable = responsable

    def generarInforme(self):
        print("*"*50)
        print(f"el paciente {self.nombre}")
        print(f"tiene aproximadamente {self.edad}")
        print(f"tiene las siguientes enfermedades {self.enfermedades}")
        print(f"esta actualmente {self.activo}")
        print(f"el nombre de su dueño es:  {self.responsable}")


    def estadoSalud(self):
        return f"El estado de salud es el siguiente: tiene {self.enfermedades} y esta {self.activo} "



joaquin = Mascota("joaquin", 4, "anemia","vivo","Daddy")
print(joaquin.estadoSalud())

 



        
  