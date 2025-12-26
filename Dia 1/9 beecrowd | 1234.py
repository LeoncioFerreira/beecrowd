# Sentença Dançante

while True:
    try:
        linha_amtiga = input()
        nova_linha = ""
        letra_maiscula = True

        for i in linha_amtiga:
            if i == " ":
                nova_linha += " "
                continue
            if letra_maiscula:
                nova_linha+=i.upper()
                letra_maiscula = False
            else:
                nova_linha+=i.lower()
                letra_maiscula = True
        print(nova_linha)
    except:
        break