# Primo Rápido
import math

n = int(input())

for _ in range(n):
    valor = int(input())
    
    if valor < 2:
        print("Not Prime")
        continue
    
    if valor == 2:
        print("Prime")
        continue
        
    if valor % 2 == 0:
        print("Not Prime")
        continue

    indicador = True
    limite = int(math.sqrt(valor))
    
    for i in range(3, limite + 1, 2):
        if valor % i == 0:
            indicador = False
            break

    if indicador:
        print("Prime")
    else:
        print("Not Prime")