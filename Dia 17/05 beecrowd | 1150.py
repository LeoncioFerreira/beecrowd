soma = 0
contagen = 0

x = int(input())
z = int(input())

while z <= x:
    z = int(input())

if x <= z:
    for i in range(x,z+1):
            soma += i
            contagen += 1
            if soma >= z:
                 break
    print(contagen)