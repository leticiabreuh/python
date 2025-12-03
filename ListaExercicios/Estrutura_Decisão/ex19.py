
numero  = int(input("Digite um número inteiro: "))

valorAbs = abs(numero)

unidades = valorAbs  % 10
dezenas = (valorAbs  // 10) % 10
centenas = valorAbs  // 100


print("-" * 20)
print(f"Número digitado: {numero}")
print(f"{centenas} centenas.")
print(f"{dezenas} dezenas.")
print(f"{unidades} unidades.")
print("-" * 20)
