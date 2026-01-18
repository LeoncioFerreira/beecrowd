resposta = 0

valor_padrao_1, valor_padrao_2, valor_padrao_3 = map(int,input().split())
valor_1, valor_2, valor_3 = map(int,input().split())

calculo_1 = valor_padrao_1 - valor_1
calculo_2 = valor_padrao_2 - valor_2
calculo_3 = valor_padrao_3 - valor_3

if calculo_1 < 0:
    resposta += (calculo_1 * -1)

if calculo_2 < 0:
    resposta += (calculo_2 * -1)

if calculo_3 < 0:
    resposta += (calculo_3 * -1)

print(resposta)