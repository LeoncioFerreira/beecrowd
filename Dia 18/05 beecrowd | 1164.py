n = int(input())

for _ in range(n):
    soma = 0
    numero = int(input())

    for i in range(1,numero):
        if numero % i == 0:
            soma += i

    if soma == numero:
        print(f"{numero} eh perfeito")
    
    else:
        print(f"{numero} nao eh perfeito")