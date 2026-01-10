frase_1 = input()
frase_2 = input()
frase_3 = input()

if frase_1 == "vertebrado":
    if frase_2 == "ave":
        if frase_3 == "carnivoro":
            print("aguia")
        else:
            print("pomba")
    else:
        if frase_3 == "onivoro":
            print("homem")
        if frase_3 == "herbivoro":
            print("vaca")

elif frase_1 == "invertebrado":
    if frase_2 == "inseto":
        if frase_3 == "hematofago":
            print("pulga")
        else:
            print("lagarta")
    else:
        if frase_3 == "hematofago":
            print("sanguessuga")
        if frase_3 == "onivoro":
            print("minhoca")