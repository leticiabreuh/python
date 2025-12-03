n1 = float(input("Digite sua primeira nota:"))
n2 = float(input("Digite sua segunda nota:"))

media = (n1+n2) / 2

if media >= 9.0 and  media == 10.0:
    print("A, APROVADO")
elif media >= 7.5 and  media == 9.0:
    print("B, APROVADO")
elif media >= 6.0 and  media == 7.5:
    print("C,  APROVADO")
elif media >= 4.0 and  media == 6.0:
    print("D, REPROVADO")
elif media >= 4.0 and  media == 0:
    print("E, REPROVADO")

