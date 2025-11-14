gigaB = float(input("Digite o tamanho do seu arquivo em Gigabytes: "))

megaB = gigaB * 1024
kiloB = (gigaB * 1024) * 1024

print(f"Seu arquivo convertido para Megabytes é {megaB:.2f}")
print(f"Seu arquivo convertido para MKilobytes é {kiloB:.2f}")