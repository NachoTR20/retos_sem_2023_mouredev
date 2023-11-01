# ENUNCIADO
# Llamar a una API es una de las tareas más comunes en programación.
# Implementa una llamada HTTP a una API (la que tú quieras) y muestra su
# resultado a través de la terminal. Por ejemplo: Pokémon, Marvel...
# Aquí tienes un listado de posibles APIs: 
# https://github.com/public-apis/public-apis

import requests

url = "https://pokeapi.co/api/v2/pokemon/?limit=151"
response = requests.get(url)
data = response.json()["results"]

for i in data:
    pokemon_name = i["name"]
    pokemon_url = i["url"]
    print(pokemon_name, pokemon_url)