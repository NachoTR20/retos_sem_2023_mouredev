# ENUNCIADO
# Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
# Podrás configurar generar contraseñas con los siguientes parámetros:
# - Longitud: Entre 8 y 16.
# - Con o sin letras mayúsculas.
# - Con o sin números.
# - Con o sin símbolos.
# (Pudiendo combinar todos estos parámetros entre ellos)
import string
import random

long = int(input("Longitud (entre 8 y 16) ? "))
if long >= 8 and long <= 16:
    mayus = input("Mayusculas (1-SI) ? ")
    nums = input("Numeros (1-SI) ? ")
    simb = input("Simbolos (1-SI) ? ")

    posibilidades = string.ascii_lowercase
    mayusculas = string.ascii_uppercase
    numeros = string.digits
    simbolos = string.punctuation

    if mayus == "1":
        posibilidades = posibilidades + mayusculas
    if nums == "1":
        posibilidades = posibilidades + numeros
    if simb == "1":
        posibilidades = posibilidades + simbolos

    contraseña = ""
    for i in range(0, long):
        contraseña += posibilidades[random.randint(0, len(posibilidades)-1)]

    print(contraseña)
else:
    print("Longitud no válida")