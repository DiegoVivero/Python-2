# Jugador de fútbol con variables
class Jugador:
    def __init__(self, nombre, equipo):
        self.nombre = nombre
        self.equipo = equipo 

def main(): 
    jugador = get_jugador()
    print(f"{jugador.nombre} es de {jugador.equipo}")

def get_jugador(): 
    nombre = input("Nombre: ")
    equipo = input("Equipo: ")
    return Jugador(nombre, equipo)

if __name__ == "__main__":
    main()
