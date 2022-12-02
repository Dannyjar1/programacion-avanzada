class Empleado:
    def __init__(self, nombre, edad, horas_trabajadas, costo_hora, descuentos, bonos):
        self.nombre = nombre
        self.edad = edad
        self.descuentos = descuentos
        self.bonos = bonos
        self.horas_trabajadas = horas_trabajadas
        self.costo_hora = costo_hora

    def calcularSueldo(self):
        sueldo = (self.horas_trabajadas * self.costo_hora  )
        sueldo_total = sueldo + self.bonos - self.descuentos
        print("El sueldo de {} es de {}".format(self.nombre, sueldo_total))
        
    


class Tripulante(Empleado):
    def __init__(self, tipoTrabajo, nombre, edad, horas_trabajadas, costo_hora, descuentos, bonos):
        super().__init__(nombre, edad, horas_trabajadas, costo_hora, descuentos, bonos)
        self.tipoTrabajo = tipoTrabajo


    def presentar(self):
        print("Bienvenidos a esta aerolinea, mi nombre es {}". format(self.nombre))
 
    


class AgenteVentas(Empleado):
    def __init__(self, tipoTrabajo,  nombre, edad, sueldo, horas_trabajadas, costo_hora, descuentos, bonos):
        super().__init__(nombre, edad, sueldo, horas_trabajadas, costo_hora, descuentos, bonos)
        self.tipoTrabajo = tipoTrabajo


    def vender(self):
        print("El costo de los boletos es de $6,00")


Juan = Tripulante("piloto","Danny",19,250,12,20,100)
Juan.calcularSueldo()