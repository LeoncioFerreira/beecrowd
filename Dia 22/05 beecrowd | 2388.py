n = int(input())
resultado = 0

for _ in range(n):
    numero_1,numero_2 = map(int,input().split())
    resultado += (numero_1 * numero_2)

print(resultado)