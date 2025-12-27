# Criptografia

n = int(input())

for _ in range(n):
    m = input()

    novom = ""
    for letra in m:
        novom += chr(ord(letra) + 3) if letra.isalpha() else letra
    m = novom[::-1]
    m = m[:len(m)//2] + ''.join([chr(ord(letra) - 1) for letra in m[len(m)//2:]])

    print(m)