# Resto da Divisão

numero_1 = int(input())
numero_2 = int(input())
vetor = []

minimo = min(numero_1,numero_2)
maximo = max(numero_1,numero_2) 


for i in range(minimo+1,maximo):
    if i%5 == 2 or i% 5 == 3:
        vetor.append(i)

vetor.sort()

for i in range(len(vetor)):
    print(vetor[i])