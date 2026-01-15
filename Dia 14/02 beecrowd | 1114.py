senha = 2002

while True:
    nova_senha = int(input())

    if nova_senha == senha:
        print("Acesso Permitido")
        break
    else:
        print("Senha Invalida")