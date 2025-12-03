peso = float(input("Digite qual é o peso dos seus peixes: "))
limite = 50
multaPorQuilo = 4.00

if peso > limite:
    excesso = peso - limite
    multa = excesso * multaPorQuilo

    print(f"Peso de peixes: {peso:.2f} kg")
    print(f"Excesso de peso: {excesso:.2f} kg")
    print(f"Valor da multa a pagar: R$ {multa:.2f}")

else:
    print("Parebéns por respeitar o reulamento!!")
