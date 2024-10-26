class Perro: 

    def __init__(self, nombre):
        self.nombre = nombre

    def ladrar(self):
        print("guau")

p = Perro("Manchita")
print(p.nombre)
p.ladrar()
p2 = Perro("Wally")
p2.ladrar()
print(p2.nombre)