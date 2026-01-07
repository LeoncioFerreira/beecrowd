codigo_peça1,numero_peça1,valor_peça1 = map(float,input().split())

codigo_peça2,numero_peça2,valor_peça2 = map(float,input().split())

calculo = (numero_peça1 * valor_peça1) + (numero_peça2 * valor_peça2)

print(f"VALOR A PAGAR: R$ {calculo:.2f}")