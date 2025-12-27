# Mensagem Oculta

n = int(input())

for i in range(n):
    palavra = input().split()
    tamanho = len(palavra)

    nova_palavra = ""
    inicial = [p[0] for p in palavra]    

    for i in range(tamanho):
        nova_palavra += inicial[i]

    print(nova_palavra)