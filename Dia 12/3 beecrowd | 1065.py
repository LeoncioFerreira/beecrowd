valor_final = 0

for i in range(5):
    
    valor = int(input())
    resultado = valor % 2
    
    if resultado == 0:
        valor_final += 1

print(f"{valor_final} valores pares")