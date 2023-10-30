# ENUNCIADO
# Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
# El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
# gane cada punto del juego.
# 
# - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
# - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
#   15 - Love
#   30 - Love
#   30 - 15
#   30 - 30
#   40 - 30
#   Deuce
#   Ventaja P1
#   Ha ganado el P1
# - Si quieres, puedes controlar errores en la entrada de datos.   
# - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   

puntuacion = ["Love", 15, 30, 40]
deuce = False
p1, p2 = 0, 0

secuencia = input("Secuencia (-): ")
secuencia = secuencia.split("-")

for punto in secuencia:
    if punto == "P1":
        p1 += 1
    elif punto == "P2":
        p2 += 1

    if p1 <= 3 and p2 <= 3:
        if p1 == 3 and p2 == 3:
            deuce = True
            print("Deuce")
        else:
            print(str(puntuacion[p1]) + " - " + str(puntuacion[p2]))
    else:
        if deuce == False:
            if p1 > p2:
                print("Ha ganado el P1")
                break
            elif p2 < p1:
                print("Ha ganado el P2")
                break
            else:
                deuce = True
                print("Deuce")
        else:
            if p1 > p2:
                print("Ventaja P1")
            else:
                print("Ventaja P2")

            deuce = False