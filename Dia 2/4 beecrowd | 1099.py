# Soma de Ímpares Consecutivos II
numero_impar = 0

n = int(input())

vetor = []

for i in range(n):
    numero_1,numero_2 = map(int,input().split())
    
    menor = min(numero_1,numero_2)
    maior = max(numero_1,numero_2)

    for j in range(menor+1,maior):
        if j % 2 == 1:
            numero_impar += j
    vetor.append(numero_impar)
    numero_impar = 0

for numero in vetor:
    print(numero)