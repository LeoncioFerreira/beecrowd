n = int(input())

for i in range(n):
    dieta = input()
    cafe = input()   
    almoco = input()

    consumido = cafe + almoco
    trapaca = False

    for alimento in consumido:
        if alimento not in dieta:
            trapaca = True
            break
        else:
            dieta = dieta.replace(alimento, '', 1)

    if trapaca:
        print("CHEATER")
    else:
        jantar = sorted(dieta)
        print(''.join(jantar))