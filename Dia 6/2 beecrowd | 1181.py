matriz = []

linha_entrada = int(input())
operacao = input().upper()

for l in range(12):
    linha = []
    for c in range(12):
        linha.append(float(input()))
    matriz.append(linha)

valores_da_linha = matriz[linha_entrada]
soma = sum(valores_da_linha)

if operacao == "S":
    print(f"{soma:.1f}")

elif operacao == "M":
    media = soma / 12
    print(f"{media:.1f}")

