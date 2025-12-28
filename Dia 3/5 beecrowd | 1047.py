# Tempo de Jogo com Minutos

hora_inicial,minuto_inicial,hora_final,minuto_final = map(int,input().split())

inicio = (hora_inicial * 60) + minuto_inicial

fim = (hora_final * 60) + minuto_final

duracao = fim - inicio

if duracao <= 0:
    duracao += 24 * 60

horas = duracao // 60
minutos = duracao % 60

print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")
