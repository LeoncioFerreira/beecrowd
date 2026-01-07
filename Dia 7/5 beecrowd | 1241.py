n = int(input())
for _ in range(n):
    a,b = map(int,input().split())
    
    if b > a:
        print("nao encaixa")


    else:
        a = str(a)
        b = str(b)
        encaixa = True

        for i in range(-len(b),0):
            if a[i] == b[i]:
                encaixa = True
            else:
                encaixa = False
                break

        if encaixa:
            print("encaixa")
        else:
            print("nao encaixa")