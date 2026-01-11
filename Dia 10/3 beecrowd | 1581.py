n = int(input())

for _ in range(n):
    pessoas = int(input())
    mesmo_indioma = True
    lista = []

    for i in range(pessoas):
        lingua = input()
        lista.append(lingua)

    for j in range(len(lista)):
        if lingua != lista[j]:
            mesmo_indioma = False
            break
    
    if mesmo_indioma:
        print(lingua)
    else:
        print("ingles")