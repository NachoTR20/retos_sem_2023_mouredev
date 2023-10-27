# ENUNCIADO
# Escribe un programa que reciba un texto y transforme lenguaje natural a
# "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
#  se caracteriza por sustituir caracteres alfanuméricos.
# - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
#   con el alfabeto y los números en "leet".
#   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")

leet_alphabet = ['4', 'I3', '[', ')', '3', '|=', '&', '#', '1', ',_|', '>|', '1', '/\/\\', '^/', '0', '|*', '(_,)', 'I2', '5', '7', '(_)', '\\/', '\/\/', '><', 'j', '2']

normal_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

leet_numbers = ['o', 'L', 'R', 'E', 'A', 'S', 'b', 'T', 'B', 'g']

text = input('Escribe el texto:\n').upper()

result = ''
for i in range(0, len(text)):
    char = text[i]
    
    if char.isalpha():
        idx = normal_alphabet.index(char)
        result += leet_alphabet[idx]
    if char.isdigit():
        result += leet_numbers[int(char)]

print(result)