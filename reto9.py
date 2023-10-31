# ENUNCIADO
# Crea 3 funciones, cada una encargada de detectar si una cadena de
# texto es un heterograma, un isograma o un pangrama.
# - Debes buscar la definición de cada uno de estos términos.
import string

# Funcion para comprobar si el texto es un heterograma
def isHeterograma(text: str) -> bool:
    result = True
    for i in range(0, len(text)):
        aux = text.count(text[i])
        if aux >= 2:
            result = False
            break

    return result

# Funcion para comprobar si el texto es un heterograma
def isIsograma(text: str) -> bool:
    result = True

    count = text.count(text[0])
    for i in range(1, len(text)):
        aux = text.count(text[i])
        if aux != count:
            result = False
            break

    return result

# Funcion para comprobar si el texto es un heterograma
def isPangrama(text: str) -> bool:
    result = True

    text = text.lower()
    letters = string.ascii_lowercase
    for letter in letters:
        if text.count(letter) == 0:
            result = False
            break
    
    return result

# Casos de heterogramas
print(isHeterograma("luteranismo"))
print(isHeterograma("ana"))

# Casos de isogramas
print(isIsograma("anna"))
print(isIsograma("ana"))

# Casos de pangramas
print(isPangrama("El veloz murciélago hindú comía feliz cardillo y kiwi. La cigüeña tocaba el saxofón detrás del palenque de paja"))
print(isPangrama("La cigüeña tocaba el saxofón detrás del palenque de paja"))