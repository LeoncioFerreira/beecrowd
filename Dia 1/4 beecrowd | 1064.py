# Positivos e Média
numeros_positivos = 0
soma = 0

for i in range(6):
    valor = float(input())
    if valor>0:
        numeros_positivos += 1
        soma += valor

media = (soma/numeros_positivos)

print(f"{numeros_positivos} valores positivos")
print(f"{media:.1f}")