# Lanche

cardapio = {"1":4, "2":4.50, "3":5, "4":2, "5":1.50}

valor_compra = 0

codigo,quantidade = map(int,input().split())

codigo = str(codigo)

valor_compra = cardapio[codigo] * quantidade

print(f"Total: R$ {valor_compra:.2f}")