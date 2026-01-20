while True:
    numero_1,numero_2 = map(int,input().split())

    if numero_1 > numero_2:
        print("Decrescente")

    elif numero_1 < numero_2:
        print("Crescente")

    else:
        break