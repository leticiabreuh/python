import math

a  = int(input("Digite o valor de A: "))
b  = int(input("Digite o valor de B: "))
c  = int(input("Digite o valor de C: "))

delta = (b**2) - (4 * a * c)
x1 = (-b - math.sqrt(delta)) / (2*a)
x2 = (-b + math.sqrt(delta)) / (2*a)
