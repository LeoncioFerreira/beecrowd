# Menor e Posição

N = int(input(""))
x = list(map(int, input().split()))

menor_valor = x[0]
posicao = 0

for i in range(N):

    if x[i] < menor_valor:
        menor_valor = x[i]
        posicao = i

print(f"Menor valor: {menor_valor}")
print(f"Posicao: {posicao}")