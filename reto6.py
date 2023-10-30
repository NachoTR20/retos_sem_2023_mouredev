# ENUNCIADO
# Crea un programa que calcule quien gana más partidas al piedra,
# papel, tijera, lagarto, spock.
# - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
# - La función recibe un listado que contiene pares, representando cada jugada.
# - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
#   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
# - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
# - Debes buscar información sobre cómo se juega con estas 5 posibilidades.

posibilidades = [["piedra", "tijera"],
                 ["piedra", "lagarto"],
                 ["tijera", "papel"],
                 ["tijera", "lagarto"],
                 ["papel", "piedra"],
                 ["papel", "spock"],
                 ["spock", "tijera"],
                 ["spock", "piedra"],
                 ["lagarto", "spock"],
                 ["lagarto", "papel"]]

player1 = 0
player2 = 0

entrada = input("ENTRADA ? ")

entrada = entrada.split(", ")
for i in range(0, len(entrada)):
    entrada[i] = entrada[i].split("-")

    if posibilidades.count([entrada[i][0], entrada[i][1]]):
        player1 += 1
        print("\t-" + str(entrada[i][0]) + " gana a " + str(entrada[i][1]))
    elif posibilidades.count([entrada[i][1], entrada[i][0]]):
        player2 += 1
        print("\t-" + str(entrada[i][0]) + " pierde con " + str(entrada[i][1]))

print("\nRESULTADO")
if player1 > player2:
    print("Player1 Gana")
elif player1 < player2:
    print("Player2 Gana")
else:
    print("Empate")