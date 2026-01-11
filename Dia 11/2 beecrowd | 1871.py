while True:
    x,y = map(int,input().split())
    if x == 0 and y ==0:
        break
    else:
        soma = x + y
        resultado = ''

        soma = str(soma)

        for numero in soma:
         
         if numero != "0" :
                resultado += numero
        print(resultado)