lista = []

valor = int(input())
lista.append(valor)

for i in range(9):
    valor *= 2
    lista.append(valor)

for i in range(10):
    print(f"N[{i}] = {lista[i]}")