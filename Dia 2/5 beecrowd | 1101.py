# Sequência de Números e Soma

vetor = []
while True:
    numero_1,numero_2 = map(int,input().split())
    if numero_1 <= 0 or numero_2 <= 0:
        break
    
    else:
        
        maior = max(numero_1,numero_2)
        menor = min(numero_1,numero_2)
        vetor = []
        
        for i in range(menor,maior+1):
            vetor.append(i)
        soma = sum(vetor)

    print(*vetor, f"Sum={soma}")