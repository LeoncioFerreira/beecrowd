n = int(input())

for i in range(n):
    palavra = input().lower()
    letras_especiais = ["a", "e", "i", "o", "s"]

    resultado = 1

    for letra in palavra:
            if letra in letras_especiais:
                resultado *= 3 
            else:
                 resultado *= 2
    print(resultado)