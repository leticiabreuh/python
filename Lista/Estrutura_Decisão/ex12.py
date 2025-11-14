ganhartHoras = float(input("Quantos você ganha por hora? "))
horasTrabalhadas = int(input("Qunatas horas trabalhadas você tem? "))

salarioBruto = horasTrabalhadas * ganhartHoras

if salarioBruto <= 900 and salarioBruto <=1500:
    descontoIr = salarioBruto * 0.05
    descontoInss = salarioBruto * 0.08
    descontoSindicato = salarioBruto * 0.03
    descontoFgts =  salarioBruto * 0.11

elif salarioBruto <= 2500 :
    descontoIr = salarioBruto * 0.010
    descontoInss = salarioBruto * 0.08
    descontoSindicato = salarioBruto * 0.03
    descontoFgts =  salarioBruto * 0.11

elif salarioBruto > 2500 :
    descontoIr = salarioBruto * 0.020
    descontoInss = salarioBruto * 0.08
    descontoSindicato = salarioBruto * 0.03
    descontoFgts =  salarioBruto * 0.11



salarioLiquido = salarioBruto - descontoInss - descontoIr - descontoSindicato - descontoFgts

print("#################### FOLHA DE PAGAMENTO ####################")
print(f"Salário Bruto: R${salarioBruto:.2f}")
print(f"IR (11%): R${descontoIr:.2f}")
print(f"INSS(8%): R${descontoInss:.2f}")
print(f"Sindicato(5%): R${descontoSindicato:.2f}")
print(f"FGTS(11%): R${descontoFgts:.2f}")
print(f"Salário líquido no final é {salarioLiquido:.2f}")
print("############################################################")
