#Juego de piedra, papel y tijera con la variable random
from random import randrange,choice

movimiento_máquina = choice(["rock","paper","scissors"])

print("Choose:")
print("1 - Rock")
print("2 - Paper")
print("3 - Scissors")

movimiento_jugador = int(input())

if movimiento_máquina == "rock":
    if movimiento_jugador == 1:
        print("Tie (Rock - Rock)")

    elif movimiento_jugador == 2:
        print("You have won! (Paper - Rock)")
    
    elif movimiento_jugador == 3:
        print("You have lost... (Scissors - Rock)")

elif movimiento_máquina == "paper":
    if movimiento_jugador == 1:
        print("You have lost... (Rock - Paper)")

    elif movimiento_jugador == 2:
        print("Tie (Paper - Paper)")
    
    elif movimiento_jugador == 3:
        print("You have won! (Scissors - Paper)")

elif movimiento_máquina == "scissors":
    if movimiento_jugador == 1:
        print("You have won! (Rock - Scissors)")

    elif movimiento_jugador == 2:
        print("You have lost... (Paper - Scissors)")
    
    elif movimiento_jugador == 3:
        print("Tie (Scissors - Scissors)")

xyz = 0

while xyz == 0:
    x = input("Press enter to exit:   ")
    xyz = 1