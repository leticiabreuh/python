areaTotal = int(input("Digite o tamanho em metros quadrados da área ser pintada: "))

litrosNece = areaTotal /3

latasNece = litrosNece / 18

latasNece = round(latasNece)

preco = latasNece * 80.00


print("Deverá comprar ",latasNece ,"lata(s)")
print(f"Com o preço total de R$ {preco:.2f}")
