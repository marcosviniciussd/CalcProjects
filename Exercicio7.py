import math

x1 = int(input("Digite o primeiro número: "))
y1 = int(input("Digite o segundo numero: "))
x2 = int(input("Digite o terceiro numero: "))
y2 = int(input("Digite o quarto numero: "))

distancia = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))

if(distancia > 10):
    print(distancia)
    print("longe")

else:
    print(distancia)
    print("perto")
    
