import math
print("############# DOWNLOAD #############")
tamMb = float(input("Tamanho do arquivo MB: "))
valoMbps = int(input("Velocidade do link: "))


tempMinu = (tamMb* 8) / (valoMbps * 60)

tempMinu = round(tempMinu)
print("Tempo aproximado de download: ", tempMinu)