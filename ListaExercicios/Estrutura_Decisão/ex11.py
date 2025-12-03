salario = float(input("Qual é seu salário? "))

if salario <=280:
     aumento = salario * 0.20
     salarioR = salario + aumento
     print(f"Sem reajuste: {salario:.2f}")
     print("Percentual de aumento aplicado 20%")
     print(f"Valor do aumento: {aumento:.2f}")
     print(f"Após aumento: {salarioR:.2f}")

elif salario == 280 and salario <= 700:
     aumento = salario * 0.15
     salarioR  = salario + aumento
     print(f"Sem reajuste: {salario:.2f}")
     print("Percentual de aumento aplicado 20%")
     print(f"Valor do aumento: {aumento:.2f}")
     print(f"Após aumento: {salarioR:.2f}")


elif salario == 700 and salario <= 1500:
     aumento = salario * 0.10
     salarioR  = salario + aumento
     print(f"Sem reajuste: {salario:.2f}")
     print("Percentual de aumento aplicado 20%")
     print(f"Valor do aumento: {aumento:.2f}")
     print(f"Após aumento: {salarioR:.2f}")


elif salario >= 1500 :
     aumento = salario * 0.05
     salarioR  = salario + aumento
     print(f"Sem reajuste: {salario:.2f}")
     print("Percentual de aumento aplicado 20%")
     print(f"Valor do aumento: {aumento:.2f}")
     print(f"Após aumento: {salarioR:.2f}")

    