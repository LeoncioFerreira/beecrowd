
n = int(input())

for _ in range(n):
    resultado = ""
    palavra = list(input())

    numero_1 = int(str(palavra[2]) + str(palavra[3]))
    numero_2 = int(str(palavra[5]) + str(palavra[6]) + str(palavra[7]))
    numero_3 = int(str(palavra[11]) + str(palavra[12]))

    soma = numero_1 + numero_2 + numero_3

    print(soma)