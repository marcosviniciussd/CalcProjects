
num = int(input("Digite um número: "))

x = 0
cont = 0

while(num // 10 != 0):
    
    x = num % 10
    num = num // 10

    if(x == num % 10):
        
        cont = cont + 1

if(cont > 0):
    print("Sim")

else:
    print("Não")

        