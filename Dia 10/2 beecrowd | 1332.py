n = int(input())

for i in range(n):
    resultado = ""
    palavra = input()
    um = "one"
    dois = "two"
    tres = "three"
    one = 0
    two = 0
    three = 0


    for j in range(len(palavra)):
        if len(palavra) > 3:
               three = 3
               break
        
        if palavra[j] == um[j]:
            one += 1
        
        if palavra[j] == dois[j]:
            two += 1
    
    if one>=2:
        print("1")
    
    elif two>=2:
        print("2")
    
    elif three>=2:
        print("3")