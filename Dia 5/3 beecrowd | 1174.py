lista = []

for _ in range(100):
    valor = float(input())
    lista.append(valor)

for i in range(100):
    if lista[i] <=10:
        print(f"A[{i}] = {lista[i]}")