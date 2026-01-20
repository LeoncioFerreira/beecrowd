n = int(input())

horas_por_presente = {
    "bonecos": 8,
    "arquitetos": 4,
    "musicos": 6,
    "desenhistas": 12}

horas_acumuladas = {
    "bonecos": 0,
    "arquitetos": 0,
    "musicos": 0,
    "desenhistas": 0}

total_presentes = 0

for _ in range(n):
    linha = input().split()
    grupo = linha[1]
    horas = int(linha[2])

    horas_acumuladas[grupo] += horas

for grupo, horas in horas_acumuladas.items():
    total_presentes += horas // horas_por_presente[grupo]

print(total_presentes)