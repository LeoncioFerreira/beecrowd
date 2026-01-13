valor = float(input())
sobra = 0

if (valor > 4500.00):
    sobra += (valor - 4500.00) * 0.28
    valor = 4500.00
if (valor > 3000.00):
    sobra += (valor - 3000.00) * 0.18
    valor = 3000.00
if (valor > 2000.00):
    sobra += (valor - 2000.00) * 0.08

if (sobra == 0):
    print("Isento")
else:
    print(f"R$ {sobra:.2f}")