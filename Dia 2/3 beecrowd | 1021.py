# Notas e Moedas

valor = float(input())

# Notas
notas_100 = valor // 100
notas_50 = (valor%100) // 50
notas_20 = ((valor%100) % 50) // 20
notas_10 = (((valor%100)% 50) % 20) // 10
notas_5 = ((((valor%100)% 50) % 20) % 10) // 5
notas_2 = (((((valor%100)% 50) % 20) % 10) % 5) // 2

# Moedas
moedas_1 = ((((((valor%100)% 50) % 20) % 10) % 5) % 2) // 1
moedas_05 = (((((((valor%100)% 50) % 20) % 10) % 5) % 2) % 1) // 0.5
moedas_025 = ((((((((valor%100)% 50) % 20) % 10) % 5) % 2) % 1) % 0.5) // 0.25
moedas_010 = (((((((((valor%100)% 50) % 20) % 10) % 5) % 2) % 1) % 0.5) % 0.25) // 0.10
moedas_005 = ((((((((((valor%100)% 50) % 20) % 10) % 5) % 2) % 1) % 0.5) % 0.25) % 0.10) // 0.05
moedas_001 = (((((((((((valor%100)% 50) % 20) % 10) % 5) % 2) % 1) % 0.5) % 0.25) % 0.10) % 0.05) / 0.01


print("NOTAS:")
print(f"{notas_100:.0f} nota(s) de R$ 100.00")
print(f"{notas_50:.0f} nota(s) de R$ 50.00")
print(f"{notas_20:.0f} nota(s) de R$ 20.00")
print(f"{notas_10:.0f} nota(s) de R$ 10.00")
print(f"{notas_5:.0f} nota(s) de R$ 5.00")
print(f"{notas_2:.0f} nota(s) de R$ 2.00")

print("MOEDAS:")
print(f"{moedas_1:.0f} moeda(s) de R$ 1.00")
print(f"{moedas_05:.0f} moeda(s) de R$ 0.50")
print(f"{moedas_025:.0f} moeda(s) de R$ 0.25")
print(f"{moedas_010:.0f} moeda(s) de R$ 0.10")
print(f"{moedas_005:.0f} moeda(s) de R$ 0.05")
print(f"{moedas_001:.0f} moeda(s) de R$ 0.01")