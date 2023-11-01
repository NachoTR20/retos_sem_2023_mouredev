# ENUNCIADO
# Dada una URL con parámetros, crea una función que obtenga sus valores.
# No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
# Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
# los parámetros serían ["2023", "0"]

from urllib.parse import urlparse, parse_qs

def obtener_parametros(url):
    url = urlparse(url)
    parametros = parse_qs(url.query)
    resultado = []
    for p in parametros.values():
        for m in p:
            resultado.append(m)

    return resultado

url = "https://ejemplo.com?param1=valor1&param2=valor2&param3=valor3&param4=valor4"
parametros = obtener_parametros(url)
print(parametros)