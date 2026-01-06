while True:
    n = int(input())
    if n == 0:
        break
    lista = []
    for i in range(1,n+1):
        lista.append(i)
    print(*lista)