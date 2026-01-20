n = int(input())
lista = []
k = 0

for i in range(n):
    lista = []
    for j in range(3):
        
        k +=1
        lista.append(k)
    
    print(*lista,"PUM")
    k += 1