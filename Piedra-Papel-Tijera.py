#Juego de piedra, papel y tijera con la variable random
from random import randrange,choice

movimiento_máquina = choice(["piedra","papel","tijera"])

print("Elige:")
print("1 - Piedra")
print("2 - Papel")
print("3 - Tijera")

movimiento_jugador = int(input())

if movimiento_máquina == "piedra":
    if movimiento_jugador == 1:
        print("Empate (Piedra - Piedra)")

    elif movimiento_jugador == 2:
        print("¡Has ganado! (Papel - Piedra)")
    
    elif movimiento_jugador == 3:
        print("Has perdido... (Tijera - Piedra)")

elif movimiento_máquina == "papel":
    if movimiento_jugador == 1:
        print("Has perdido... (Piedra - Papel)")

    elif movimiento_jugador == 2:
        print("Empate (Papel - Papel)")
    
    elif movimiento_jugador == 3:
        print("¡Has ganado! (Tijera - Papel)")

elif movimiento_máquina == "tijera":
    if movimiento_jugador == 1:
        print("¡Has ganado! (Piedra - Tijera)")

    elif movimiento_jugador == 2:
        print("Has perdido... (Papel - Tijera)")
    
    elif movimiento_jugador == 3:
        print("Empate (Tijera - Tijera)")
