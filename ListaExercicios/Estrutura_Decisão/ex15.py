l1 = int(input("Lado 1 do triangulo: "))
l2= int(input("Lado 2 do triangulo: "))
l3 = int(input("Lado 3 do triangulo: "))

if l1 == l2 and l1 == l3:
    print("Trinângulo Equilátero")
elif l1 == l2 or l1 == l3:
    print("Trinângulo Isósceles")
elif l1 != l2 and l1 != l3:
    print("Triâgulo Escaleno")
