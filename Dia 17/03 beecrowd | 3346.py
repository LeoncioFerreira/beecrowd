f1,f2 = map(float, input().split())

flutuacao_total = ((1 + f1/100) * (1 + f2/100) - 1) * 100

print(f"{flutuacao_total:.6f}")