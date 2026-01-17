numero_1,numero_2 = map(int,input().split())

if numero_1 == numero_2:
    print("O JOGO DUROU 24 HORA(S)")

elif numero_2 > numero_1:
    duracao = numero_2 - numero_1
    print(f"O JOGO DUROU {duracao} HORA(S)")
else:
    duracao = 24 - numero_1 + numero_2
    print(f"O JOGO DUROU {duracao} HORA(S)")