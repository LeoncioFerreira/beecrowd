n = int(input())

for _ in range(n):
    numero_1,numero_2 = map(int,input().split())
    somas_impares = 0
    impares = 0
    numero = 0
    numero = numero_1

    while True:
        if impares == numero_2:
            break
        if numero % 2 == 1:
            somas_impares += numero
            impares += 1
            numero += 1
        else:
            numero += 1
        
    print(somas_impares)