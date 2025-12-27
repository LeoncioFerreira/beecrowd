# Frase Completa

n = int(input())

for i in range(n):
    frase = input().strip()
    nova_frase = set(frase)
    
    valor = 0
    
    for caractere in nova_frase:
        if caractere.isalpha():
            valor+=1

    if valor == 26:
        print("frase completa")

    if valor >= 12 and valor < 26:
        print ("frase quase completa")

    if valor < 12:
        print("frase mal elaborada")