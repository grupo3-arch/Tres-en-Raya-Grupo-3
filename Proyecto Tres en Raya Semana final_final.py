'''
Nombres: Alejandra Cadena,Ana Espinoza, Emily Cuascota, Gerardo Freire
Fecha: 03/04/2025

Proyecto Tres en Raya / Semana final

'''
import winsound

ranking = {}


def cargar_ranking():
    try:
        with open("ranking.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                nombre, victorias = linea.strip().split(",")
                ranking[nombre] = int(victorias)
    except FileNotFoundError:
        pass  


def guardar_ranking():
    with open("ranking.txt", "w", encoding="utf-8") as archivo:
        for nombre, victorias in ranking.items():
            archivo.write(f"{nombre},{victorias}\n")

def reproducir_sonido_ganar():
    winsound.Beep(1000, 500)

def reproducir_sonido_perder():
    winsound.Beep(400, 500)

def dibujar_tablero(tablero):
    print("\n")
    print(f"  {tablero[0]}  │  {tablero[1]}  │  {tablero[2]}  ")
    print("─────┼─────┼─────")
    print(f"  {tablero[3]}  │  {tablero[4]}  │  {tablero[5]}  ")
    print("─────┼─────┼─────")
    print(f"  {tablero[6]}  │  {tablero[7]}  │  {tablero[8]}  ")
    print("\n")

def verificar_ganador(tablero, jugador):
    combinaciones = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for combo in combinaciones:
        if tablero[combo[0]] == tablero[combo[1]] == tablero[combo[2]] == jugador:
            return True
    return False

def tablero_lleno(tablero):
    return " " not in tablero

def mostrar_ranking():
    print("Ranking de los mejores jugadores:")
    jugadores_ordenados = sorted(ranking.items(), key=lambda x: x[1], reverse=True)
    for i, (jugador, victorias) in enumerate(jugadores_ordenados[:3], start=1):
        print(f"{i}. {jugador} - {victorias} victorias")

def juego():
    print("¡Bienvenidos al juego!")

    nombre1 = input("Jugador 1, ingresa tu nombre: ")
    nombre2 = input("Jugador 2, ingresa tu nombre: ")

    while nombre2 == nombre1:
        print("Ese nombre ya fue usado. Elige un nombre diferente.")
        nombre2 = input("Jugador 2, ingresa tu nombre: ")

    simbolo1 = input(f"{nombre1}, elige tu simbolo (X/O): ").upper()
    while simbolo1 not in ["X", "O"]:
        simbolo1 = input("Simbolo invalido. Elige X u O: ").upper()

    simbolo2 = "O" if simbolo1 == "X" else "X"

    jugadores = {
        simbolo1: nombre1,
        simbolo2: nombre2
    }

    tablero = [" " for _ in range(9)]
    turno = simbolo1  

    while True:
        dibujar_tablero(tablero)
        print(f"Turno de {jugadores[turno]} ({turno})")

        while True:
            try:
                pos = int(input("Elige una posicion (1-9): ")) - 1
                if pos >= 0 and pos <= 8 and tablero[pos] == " ":
                    break
                else:
                    print("Esa posicion ya esta ocupada. Intenta otra vez.")
                    reproducir_sonido_perder()
            except ValueError:
                print("Posicion invalida. Elige un numero del 1 al 9.")
                reproducir_sonido_perder()

        tablero[pos] = turno

        if verificar_ganador(tablero, turno):
            dibujar_tablero(tablero)
            print(f"¡{jugadores[turno]} ({turno}) gana la partida!")
            reproducir_sonido_ganar()

            ganador = jugadores[turno]
            ranking[ganador] = ranking.get(ganador, 0) + 1
            guardar_ranking()  
            break

        if tablero_lleno(tablero):
            dibujar_tablero(tablero)
            print("Empate")
            break

        turno = simbolo2 if turno == simbolo1 else simbolo1

    mostrar_ranking()

cargar_ranking()  

while True:
    juego()
    continuar = input("¿Quieres jugar otra partida? (s/n): ").lower()
    if continuar != "s":
        print("Gracias por jugar ¡Hasta la proxima!")
        break
