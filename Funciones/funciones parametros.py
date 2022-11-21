def saludoConParametro(nombre = "Danny"):
    return "Hello world", nombre

saludar = saludoConParametro()
print(saludar)

saludar1 = saludoConParametro("juan")
print(saludar1)