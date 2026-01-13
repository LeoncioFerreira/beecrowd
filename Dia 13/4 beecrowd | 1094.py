tentativas = int(input())
total = 0
coelhos = 0
ratos = 0
sapos = 0

for _ in range(tentativas):
    quantia,tipo = input().split()
    quantia = int(quantia)

    total += quantia

    if tipo == "C":
        coelhos += quantia
    elif tipo == "R":
        ratos += quantia
    elif tipo == "S":
        sapos  += quantia

print(f"Total: {total} cobaias")
print(f"Total de coelhos: {coelhos}")
print(f"Total de ratos: {ratos}")
print(f"Total de sapos: {sapos}")
print(f"Percentual de coelhos: {((coelhos / total) * 100):.2f} %")
print(f"Percentual de ratos: {((ratos / total) * 100):.2f} %")
print(f"Percentual de sapos: {((sapos / total) * 100):.2f} %")
