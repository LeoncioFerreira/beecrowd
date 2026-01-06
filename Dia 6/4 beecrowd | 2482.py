saudacoes = {}

quantidade = int(input())
for _ in range(quantidade):
    idioma = input().strip()
    saudacao = input()
    saudacoes[idioma] = saudacao

pessoas = int(input())
for _ in range(pessoas):
    nome = input().strip()
    idioma = input().strip()
    print(nome)
    print(saudacoes[idioma])
    print()