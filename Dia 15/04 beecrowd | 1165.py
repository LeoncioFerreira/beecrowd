import math

tentativas = int(input())

for _ in range(tentativas):
    numero = int(input())
    Primo = True

    if numero < 2:
        Primo = False
    if numero == 2:
        Primo = True
    if numero> 2 and numero % 2 == 0:
        Primo = False

    maximo = int(math.sqrt(numero)) + 1
    for i in range(3,maximo,2):
        if numero % i == 0:
            Primo = False
            break
        
    if Primo:
        print(f"{numero} eh primo")
    else:
        print(f"{numero} nao eh primo")