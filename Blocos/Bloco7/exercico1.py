
ano_nascimento = input("Por favor, digite o seu ano de nascimento: ")

ano_nascimento2 = int(ano_nascimento)

ano_atual = 2025

idade = ano_atual - ano_nascimento2

if idade > 65:
    print("Você já pode se aposentar")
else:
    print("Não pode se aposentar ainda")
