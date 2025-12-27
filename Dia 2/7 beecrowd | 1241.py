# Encaixa ou Não II

encaixa = True
n = int(input())

for i in range(n):
    a,b = map(int,input().split())
    numero_a_string = str(a)
    numero_b_string = str(b)

    comprimento_a = len(numero_a_string)
    comprimento_b = len(numero_b_string)
    if comprimento_b>comprimento_a:
        print("nao encaixa")
    else:
        for j in range(-comprimento_b,0):
            if numero_a_string[j] == numero_b_string[j]:
                encaixa = True
            else:
                encaixa = False
                break
            
        if encaixa:
            print("encaixa")

        else:
            print("nao encaixa")