valor = list(map(int, input().split()))
a = valor[0]
n = 0
soma = 0

for i in range(1, len(valor)):
    if valor[i] > 0:
        n = valor[i]
        break

for i in range(n):
    soma += a + i

print(soma)