a,b,c = map(int,input().split())

maior_ab = (a + b + abs(a - b)) / 2

if c > maior_ab:
    print(f"{c:.0f} eh o maior")

else:
    print(f"{maior_ab:.0f} eh o maior")