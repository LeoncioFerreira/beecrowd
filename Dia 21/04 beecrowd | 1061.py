dia_inicial = input().split()
dia_inicial = int(dia_inicial[1])

tempo_inicial = input().split()

hora_inicial = int(tempo_inicial[0])
minuto_inicial = int(tempo_inicial[2])
segundo_inicial = int(tempo_inicial[4])

dia_final = input().split()
dia_final = int(dia_final[1])

tempo_final = input().split()

hora_final = int(tempo_final[0])
minuto_final = int(tempo_final[2])
segundo_final = int(tempo_final[4])

segundos_por_dia = (24 * 60 * 60)

inicio_em_segundos = ( dia_inicial * segundos_por_dia + hora_inicial * 3600 + minuto_inicial * 60 + segundo_inicial)

fim_em_segundos = ( dia_final * segundos_por_dia + hora_final * 3600 + minuto_final * 60 + segundo_final)

duracao = fim_em_segundos - inicio_em_segundos

dias = duracao // segundos_por_dia
duracao %= segundos_por_dia

horas = duracao // 3600
duracao %= 3600

minutos = duracao // 60
segundos = duracao % 60

print(f"{dias} dia(s)")
print(f"{horas} hora(s)")
print(f"{minutos} minuto(s)")
print(f"{segundos} segundo(s)")