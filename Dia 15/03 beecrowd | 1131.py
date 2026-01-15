inter = 0
gremio = 0 
grenais = 0
empate = 0 

while True:
    gol_inter,gol_gremio = map(int,input().split())
    print("Novo grenal (1-sim 2-nao)")
    resposta = int(input())
    grenais += 1
    if gol_inter > gol_gremio:
        inter += 1
    elif gol_inter == gol_gremio:
        empate += 1
    else:
        gremio += 1
    if resposta == 2:
          break

print(f"{grenais} grenais")
print(f"Inter:{inter}")
print(f"Gremio:{gremio}")
print(f"Empates:{empate}")
if inter > gremio:
    print("Inter venceu mais")
else:
    print("Gremio venceu mais")