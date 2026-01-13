numero = int(input())
lista = []

for i in range(0,numero + 1):
    if i % 2 == 1:
        lista.append(i)

for j in range(len(lista)):
    print(lista[j])