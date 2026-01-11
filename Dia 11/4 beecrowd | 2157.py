n = int(input())

for i in range(n):
    numero_1,numero_2 = map(int,input().split())

    resultado = ""
    
    for numero in range(numero_1,numero_2+1):
        resultado += str(numero)
    
    espelho = resultado[::-1]

    print(resultado + espelho)