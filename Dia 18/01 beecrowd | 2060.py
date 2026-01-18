numero_par = 0
numero_tres = 0
numero_quatro = 0
numero_cinco = 0

n = int(input())
numero = list(map(int, input().split()))

for i in range(n):
    if numero[i] % 2 == 0:
        numero_par += 1
    
    if numero[i] % 3 == 0:
        numero_tres += 1
    
    if numero[i] % 4 == 0:
        numero_quatro += 1
    
    if numero[i] % 5 == 0:
        numero_cinco += 1

print(f"{numero_par} Multiplo(s) de 2")
print(f"{numero_tres} Multiplo(s) de 3")
print(f"{numero_quatro} Multiplo(s) de 4")
print(f"{numero_cinco} Multiplo(s) de 5")