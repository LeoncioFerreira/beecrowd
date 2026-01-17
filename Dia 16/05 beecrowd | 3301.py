h,z,l = map(int,input().split())

minimo = min(h,z,l)
maximo = max(h,z,l)

if h != minimo and h != maximo:
    print("huguinho")

elif l != minimo and l != maximo:
    print("luisinho")

elif z != minimo and z != maximo:
    print("zezinho")
