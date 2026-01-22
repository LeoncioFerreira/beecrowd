a,b,c = map(float,input().split())
lados = sorted([a, b, c], reverse=True)
a,b,c = lados

if(a >= b + c):
    print('NAO FORMA TRIANGULO')
else:
    if(a * a == b * b + c * c):
        print('TRIANGULO RETANGULO')
    elif(a * a > b * b + c * c):
        print('TRIANGULO OBTUSANGULO')
    else:
        print('TRIANGULO ACUTANGULO')

    if(a == b == c):
        print('TRIANGULO EQUILATERO')
    elif(a == b or a == c or b == c):
        print('TRIANGULO ISOSCELES')