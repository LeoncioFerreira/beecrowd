while True:

    try:
        tentativas = int(input())
        lista = []
        
        for _ in range(tentativas):
            tempo = float(input())
            lista.append(tempo)

            for i in range(0,len(lista)):
                if tempo >= lista[i]:
                    tempo = lista[i]
            
        print(f"{tempo:.2f}")


    except EOFError:
     break