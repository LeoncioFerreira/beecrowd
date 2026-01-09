import math
a,b,c = map(float,input().split())
baskara = ((b*b) - (4*a*c))

if a <= 0 or b <= 0 or c <= 0 or baskara < 0:
    print("Impossivel calcular")
else:
    x1 = (-b + math.sqrt(baskara) )/ (2*a)
    x2 = (-b - math.sqrt(baskara)) / (2*a)

    print(f"R1 = {x1:.5f}")
    print(f"R2 = {x2:.5f}")