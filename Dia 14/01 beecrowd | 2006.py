resultado = 0

resposta = input()

tentativas = input()

for i in range(len(tentativas)):
    if resposta == tentativas[i]:
        resultado += 1

print(resultado)