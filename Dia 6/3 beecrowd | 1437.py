while True:
    direcoes = ['N', 'L', 'S', 'O']  
    direcao_atual = 0  

    tamanho = int(input())
    if tamanho == 0:
        break
    comandos = input()[:tamanho]
    
    for comando in comandos:
        if comando == 'D':  
            direcao_atual = (direcao_atual + 1) % 4
        elif comando == 'E':  
            direcao_atual = (direcao_atual - 1) % 4

    print(direcoes[direcao_atual])