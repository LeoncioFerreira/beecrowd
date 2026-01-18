soma = 0
valor_1 = int(input())
valor_2 = int(input())

maximo = max(valor_1,valor_2)
minimo = min(valor_1,valor_2)

for i in range(minimo,maximo+1):
    if i % 13 != 0:
        soma += i

print(soma)