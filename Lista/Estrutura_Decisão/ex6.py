n1 = int(input("Dgite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

if n1 > n2  and n1 > n3:
    print(n1,"é maior")
elif n2 > n1 and n2 > n3:
    print(n2,"é maior")
else:
    print(n3,"é maior")