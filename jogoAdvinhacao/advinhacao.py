import random

tentativa = 0
continuar = True
numero_aleatorio = random.randint(1, 50)  
numero = 0  
print("Tente adivinhar o número entre 1 e 50.")
while continuar == True:
    numero = int(input("Seu palpite: "))
    print(numero_aleatorio)
    tentativa += 1

    if numero > numero_aleatorio:
        print("Muito alto! Tente um número menor.")
    elif numero < numero_aleatorio:
        print("Muito baixo! Tente um número maior.")
    else:
        print(f"Parabéns, você acertou em {tentativa} tentativas!")
        jogar = input(("Quer jogar novamente? (s/n) "))
        jogar.lower()
        if jogar == "s" :
            tentaiva = 0
            numero_aleatorio = random.randint(1, 50)

        else:
            continuar = False
            print("Obrigada por jogar!")
            break
 
       



    



