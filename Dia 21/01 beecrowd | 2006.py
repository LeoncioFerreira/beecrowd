total = 0

resultado = int(input())

letras = list(map(int,input().split()))

for letra in letras:

    if letra == resultado:
        total += 1

print(total)