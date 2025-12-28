# LED

tabela_leds = {'1': 2, '2': 5, '3': 5, '4': 4, '5': 5,'6': 6, '7': 3, '8': 7, '9': 6, '0': 6}

n = int(input())
novo_valor = 0

for _ in range(n):
    valor = input()
    
    for digito in valor:
        novo_valor += tabela_leds[digito]
    
    print(f"{novo_valor} leds")
    novo_valor = 0
