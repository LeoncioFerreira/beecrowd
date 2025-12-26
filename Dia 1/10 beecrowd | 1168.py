# LED

n = int(input())
tabela_leds = {'1': 2, '2': 5, '3': 5, '4': 4, '5': 5,'6': 6, '7': 3, '8': 7, '9': 6, '0': 6}

vetor = []

for i in range(n):
    valor = input()
    vetor.append(valor) 

for valor in vetor:
    total_de_leds = 0
    for digito in valor:
        total_de_leds += tabela_leds[digito]
        
    print(f"{total_de_leds} leds")