tentativas = int(input())

for i in range(tentativas):
    numero = int(input())
    if numero == 0:
        print("NULL")
    else:
        if numero % 2 ==0:
            if numero > 0:
                print("EVEN POSITIVE")
            else:
                print("EVEN NEGATIVE")
        
        elif numero % 2 == 1:
             if numero > 0:
                print("ODD POSITIVE")
             else:
                print("ODD NEGATIVE")