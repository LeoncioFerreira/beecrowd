numero = int(input())
contador = 0
lista = []

while contador < 6:
    if numero % 2 == 1:
        lista.append(numero)
        contador += 1
        numero += 1

    else:
        numero += 1

for i in range(len(lista)):
    print(lista[i])