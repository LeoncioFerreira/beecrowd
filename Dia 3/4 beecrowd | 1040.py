# Média 3
em_analise = False
nota_1,nota_2,nota_3,nota_4 = map(float,input().split())
media_inicial = ((nota_1 * 2) + (nota_2 * 3) + (nota_3 *4) + (nota_4*1)) / 10

if media_inicial >= 5.0 and  media_inicial <=6.9:
    em_analise = True
    nota_exame = float(input(""))


print(f"Media: {media_inicial:.1f}")

if em_analise:
    print("Aluno em exame.")
    print(f"Nota do exame: {nota_exame:.1f}")
    media_final = (media_inicial + nota_exame) / 2
    
    if media_final >=5:
        print("Aluno aprovado.")
        print(f"Media final: {media_final:.1f}")

elif media_inicial>= 7:
    print("Aluno aprovado.")

elif media_inicial<5:
    print("Aluno reprovado.")