# ENUNCIADO
# Crea un programa que simule el comportamiento del sombrero seleccionador del
# universo mágico de Harry Potter.
# - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
# - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
# - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
#   coloque al alumno en una de las 4 casas de Hogwarts (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
# - Ten en cuenta los rasgos de cada casa para hacer las preguntas y crear el algoritmo seleccionador.
#   Por ejemplo, en Slytherin se premia la ambición y la astucia.

gryffindor = 0
slytherin = 0
hufflepuff = 0
ravenclaw = 0

print("Pregunta 1: ¿Cual es su mayor virtud?")
print("\t1) Ambicion")
print("\t2) Lealtad")
print("\t3) Valentia")
print("\t4) Sabiduria")

opcion = input("Opcion ? ")
if int(opcion) == 1:
    slytherin += 1
elif int(opcion) == 2:
    hufflepuff  += 1
elif int(opcion) == 3:
    gryffindor += 1
elif int(opcion) == 4:
    ravenclaw  += 1

print("Pregunta 2: ¿Que mascota elegirias?")
print("\t1) Buho")
print("\t2) Serpiente")
print("\t3) Leon")
print("\t4) Lobo")

opcion = input("Opcion ? ")
if int(opcion) == 1:
    ravenclaw += 1
elif int(opcion) == 2:
    slytherin  += 1
elif int(opcion) == 3:
    gryffindor += 1
elif int(opcion) == 4:
    hufflepuff  += 1

print("Pregunta 3: ¿Que asignatura magica te atrae mas?")
print("\t1) Adivinacion")
print("\t2) Pociones")
print("\t3) Cuidado de criaturas magicas")
print("\t4) Defensa contra las artes oscuras")

opcion = input("Opcion ? ")
if int(opcion) == 1:
    ravenclaw += 1
elif int(opcion) == 2:
    slytherin  += 1
elif int(opcion) == 3:
    hufflepuff += 1
elif int(opcion) == 4:
    gryffindor  += 1

print("Pregunta 4: ¿En que lugar pasaras tu tiempo libre en Howards?")
print("\t1) El bosque prohibido")
print("\t2) La biblioteca")
print("\t3) Las mazmorras")
print("\t4) El campo de Quidditch")

opcion = input("Opcion ? ")
if int(opcion) == 1:
    hufflepuff += 1
elif int(opcion) == 2:
    ravenclaw  += 1
elif int(opcion) == 3:
    slytherin += 1
elif int(opcion) == 4:
    gryffindor  += 1

print("Pregunta 5: ¿Que cualidad valoras mas en un amigo?")
print("\t1) Inteligencia")
print("\t2) Coraje")
print("\t3) Lealtad")
print("\t4) Ambicion")

opcion = input("Opcion ? ")
if int(opcion) == 1:
    ravenclaw += 1
elif int(opcion) == 2:
    gryffindor  += 1
elif int(opcion) == 3:
    hufflepuff += 1
elif int(opcion) == 4:
    slytherin  += 1

if gryffindor > slytherin and gryffindor > hufflepuff and gryffindor > ravenclaw:
    print("Vas a pertenecer a la casa Gryffindor")
elif slytherin > hufflepuff and slytherin > ravenclaw:
    print("Vas a pertenecer a la casa Slytherin")
elif hufflepuff > ravenclaw:
    print("Vas a pertenecer a la casa Hufflepuff")
else:
    print("Vas a pertenecer a la casa Ravenclaw")