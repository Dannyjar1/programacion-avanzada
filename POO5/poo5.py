class Juego:
    def __init__(self, nombre, alto, ancho, color, vidas, municion):
        self.nombre = nombre
        self.alto = alto
        self.ancho = ancho
        self.color = color
        self.vidas = vidas
        self.municion = municion

    
    def saltar(self):
        print (f"{self.nobre} salta 2 metros ")

    def girar(self, sentidoGiro):
        print (f"{self.nombre}gira a la {sentidoGiro}")

    def esconderse(self):
        lugaresEsconder = ["Piedra", "Rio", "calaboso", "casa"]
        lugaresEsconder2 = ["abajo", "sobre", "a un lado", "no se escondio"]
        for lugar in range (lugaresEsconder):
             print(f"{self.nombre} se esconde",lugar)
        for lugar2 in range(lugaresEsconder):
            print(f"directamente se esconde",lugar)

juego1 = Juego("Free Fire","10 cm", "8 cm", "azul ", 3, 120)
print(juego1.girar())
       



        

        