# Seleçao em Vetor I
x = 0
A = []

for i in range(100):
    valor = (float(input()))
    A.append(valor)

for i in range(100):
    if A[i]<=10:
        x = A[i]
        print(f"A[{i}] = {x:.1f}")
