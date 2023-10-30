# ENUNCIADO
# Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
# Ejemplos:
#   - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
#   - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"

numero = int(input("Introduce un numero ? "))

primo = True
par = False
fibonacci = False

for i in range(1, numero):
    if numero % i == 0 and i != 1:
        primo = False
        break

if numero % 2 == 0:
    par = True

n1 = 0
n2 = 1

while n2 < numero:
    aux = n1 + n2
    n1 = n2
    n2 = aux

if n2 == numero:
    fibonacci = True

resultado = str(numero) + " "
if primo != True:
    resultado += "no "
resultado += "es primo, "
if par != True:
    resultado += "es impar y "
resultado += "es par y "
if fibonacci != True:
    resultado += "no "
resultado += "es fibonacci"

print(resultado)