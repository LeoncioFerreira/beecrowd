# Revisão de Contrato

while True:
    n,m = input().split()
    nova_frase = ''  
    mais_zero = 0
    if n=="0" and m=="0":
       break
       
    for ponteiro in m:
            if ponteiro != n:
                nova_frase += ponteiro
          
    if nova_frase == "":
        print(0)
    else:
        print (int(nova_frase))