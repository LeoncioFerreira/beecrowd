media = 0
quantidade = 0

while True:
    nota = float(input())
    
    if nota >= 0 and nota <=10:
        media += nota
        quantidade += 1
    else:
        print("nota invalida")

    if quantidade == 2: 
        resposta = media / quantidade
        
        print(f"media = {resposta:.2f}")
        
        while True:
            print("novo calculo (1-sim 2-nao)")
            resultado = int(input())
            
            if resultado == 1:
                media = 0
                quantidade = 0
                break
            elif resultado == 2:
                exit()