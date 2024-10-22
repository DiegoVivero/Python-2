# Jugador de fútbol con variables
class Jugador:
    def __init__(self, nombre, equipo):
        if not nombre:
            raise ValueError("Ingrese el nombre del jugador")
        if equipo not in ["Colo Colo", "La U", "La Catolica", "Magallanes"]:
            raise ValueError("Equipo Inválido")
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
    jugador = Jugador("Palacios", "Colo Colo")
    print(jugador.nombre, jugador.equipo)
    main()
