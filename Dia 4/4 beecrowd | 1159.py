# Soma de Pares Consecutivos

while True:
    
    x = int(input())
    
    if x==0:
        break
    else:
            soma_dos_pares = 0
            
            indicador = 0
            
            atual = x
            
            while indicador<5:
                 if atual % 2 ==0:
                      soma_dos_pares += atual
                      atual+=1
                      indicador+=1
                 else:
                    atual +=1

            print(soma_dos_pares)
                 