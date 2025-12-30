# A Biblioteca do Senhor Severino

while True:
    try:
        n = int(input())
        lista = []

        for _ in range(n):
            lista.append(input().strip())

        lista.sort()
        for i in range(len(lista)):
            print(lista[i])

    except EOFError:
        break