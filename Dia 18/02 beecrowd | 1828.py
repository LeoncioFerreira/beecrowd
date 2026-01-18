n = int(input())

for i in range(1,n+1):
    caso1,caso2 = input().split()
    
    if caso1 != caso2:
        if caso1 == "tesoura" and caso2 == "papel":
            print(f"Caso #{i}: Bazinga!")
        
        elif caso1 == "papel" and caso2 == "tesoura":
            print(f"Caso #{i}: Raj trapaceou!")

        elif caso1 == "papel" and caso2 == "pedra":
            print(f"Caso #{i}: Bazinga!")

        elif caso1 == "pedra" and caso2 == "papel":
            print(f"Caso #{i}: Raj trapaceou!")

        elif caso1 == "pedra" and caso2 == "lagarto":
            print(f"Caso #{i}: Bazinga!")
        
        elif caso1 == "lagarto" and caso2 == "pedra":
            print(f"Caso #{i}: Raj trapaceou!")

        elif caso1 == "lagarto" and caso2 == "Spock":
            print(f"Caso #{i}: Bazinga!")
        
        elif caso1 == "Spock" and caso2 == "lagarto":
            print(f"Caso #{i}: Raj trapaceou!")
        
        elif caso1 == "Spock" and caso2 == "tesoura":
            print(f"Caso #{i}: Bazinga!")

        elif caso1 == "tesoura" and caso2 == "Spock":
            print(f"Caso #{i}: Raj trapaceou!")

        elif caso1 == "tesoura" and caso2 == "lagarto":
            print(f"Caso #{i}: Bazinga!")
        
        elif caso1 == "lagarto" and caso2 == "tesoura":
            print(f"Caso #{i}: Raj trapaceou!")

        elif caso1 == "lagarto" and caso2 == "papel":
            print(f"Caso #{i}: Bazinga!")

        elif caso1 == "papel" and caso2 == "lagarto":
            print(f"Caso #{i}: Raj trapaceou!")

        elif caso1 == "papel" and caso2 == "Spock":
            print(f"Caso #{i}: Bazinga!")
        
        elif caso1 == "Spock" and caso2 == "papel":
            print(f"Caso #{i}: Raj trapaceou!")

        elif caso1 == "Spock" and caso2 == "pedra":
            print(f"Caso #{i}: Bazinga!")
        
        elif caso1 == "pedra" and caso2 == "Spock":
            print(f"Caso #{i}: Raj trapaceou!")

        elif caso1 == "pedra" and caso2 == "tesoura":
            print(f"Caso #{i}: Bazinga!")

        elif caso1 == "tesoura" and caso2 == "pedra":
            print(f"Caso #{i}: Raj trapaceou!")

    else:
        print(f"Caso #{i}: De novo!")