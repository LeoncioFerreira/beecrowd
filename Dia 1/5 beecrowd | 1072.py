# Intervalo 2

valores_in = 0
valores_out = 0

n = int(input())

for i in range(n):
    valor = int(input())
    
    if valor>=10 and valor<=20:
        valores_in+=1
    else:
        valores_out+=1

print(f"{valores_in} in")
print(f"{valores_out} out")