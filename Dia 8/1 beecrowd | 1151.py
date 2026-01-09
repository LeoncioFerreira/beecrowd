lista = []

def fibonnaci(n):
    if n>=0:
        lista.append(0)
    if n>=1:
        lista.append(1)

    for i in range(2, n):
        print(i)
        lista.append(lista[i-1] + lista[i-2])

n =int(input())
fibonnaci(n)
print(*lista)