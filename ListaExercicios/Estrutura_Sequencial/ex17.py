import math
#Peguntar para o usuario
areaTotal = int(input("Digite o tamanho em metros quadrados da área ser pintada: "))
#Cauculo da folga e total de metros com folga
folga = areaTotal * (10 / 100)
mtsComFolga = areaTotal + folga

litrosNece = mtsComFolga/ 6

# --- Situação 1 e 2: Cálculo de Latas e Galões Separados ---
latasNece = litrosNece / 18
galaNece = litrosNece / 3.6

#Convertendo para inteiro, arredondado para cima (para a situação 1 e 2)
latasNece = math.ceil(latasNece)
galaNece = math.ceil(galaNece)

#Calculo dos preços (para a situação 1 e 2)
precoLata = latasNece * 80.00
precoGala = galaNece * 25.00

# --- Situação 3: Cálculo da Mistura ---
#Calcular quantas latas inteiras cabem no total de litros necessários (sem arredondar para cima ainda)
latas_mistura = math.floor(litrosNece / 18)  # floor arredonda para baixo
litros_restantes = litrosNece % 18  # Usa o operador de módulo para saber o restante

#Calcular quantos galões são necessários para os litros restantes
galoes_mistura = math.ceil(litros_restantes / 3.6) # Arredonda para cima, pois só vendem galões cheios

#Calcular o preço total da mistura
preco_mistura = (latas_mistura * 80.00) + (galoes_mistura * 25.00)



print("------------------------------------")
print("Opção 1: Comprar apenas latas de 18L")
print(f"Deverá comprar {latasNece} lata(s)")
print(f"Com o preço total de R$ {precoLata:.2f}")
print("------------------------------------")
print("Opção 2: Comprar apenas galões de 3.6L")
print(f"Deverá comprar {galaNece} galão(ões)")
print(f"Com o preço total de R$ {precoGala:.2f}")
print("------------------------------------")
print("Opção 3: Mistura de latas e galões (menor desperdício)")
print(f"Deverá comprar {latas_mistura} lata(s) e {galoes_mistura} galão(ões)")
print(f"Com o preço total de R$ {preco_mistura:.2f}")
print("------------------------------------")
