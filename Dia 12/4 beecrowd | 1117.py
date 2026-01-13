contador = 0
valor_final = 0

while contador < 2:
    valor = float(input())
    if valor >=0 and valor <= 10:
        valor_final += valor
        
        contador += 1
    
    else:
        print("nota invalida")

media = valor_final / 2
print(f"media = {media:.2f}")