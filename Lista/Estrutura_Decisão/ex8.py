pd1 = float(input("Digite o  preço do primeiro produto: "))
pd2 = float(input("Digite o  preço do segundo produto: "))
pd3 = float(input("Digite o  preço do terceiro produto: "))

if pd1 < pd2 and pd1 < pd3:
    print("Primeiro produto é mais barato")
elif pd2 < pd1 and pd2 < pd3:
    print("Segundo produto é mais barato")
else:
    print("Terceiro produto é o mais barato")

    
