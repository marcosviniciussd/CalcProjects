
numero = int(input("Digite o valor de n: "))

fatorial = 1
fat = 1

while(fat <= numero):
    
    fatorial = fat * fatorial
    fat = fat + 1

'''for fat in range(1, numero + 1):
    fatorial = fat * fatorial'''

print(fatorial)
    
