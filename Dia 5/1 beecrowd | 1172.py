lista = []

for _ in range(11):
    valor = int(input())
    
    if valor <=0:
        valor = 1
    lista.append(valor)

for i in range(11):
    print(f"X[{i}] = {lista[i]}")