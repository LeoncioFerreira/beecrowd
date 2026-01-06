lista = []
nova_lista = []

for _ in range(20):
    valor = int(input())
    lista.append(valor)

for i in range(20):
    nova_valor = lista[19-i]
    nova_lista.append(nova_valor)

for i in range(20):
    print(f"N[{i}] = {nova_lista[i]}")   