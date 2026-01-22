abas,numero_acoes = map(int,input().split())

for _ in range(numero_acoes):
    acao = input()
    if acao == "fechou":
        abas += 1
    if acao == "clicou":
        abas -= 1

print(abas)