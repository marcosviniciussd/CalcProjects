num = int(input("Digite um número: "))

i = 1
cont = 0

for i in range(1, 9):

    if(num % i == 0):
        cont = cont + 1

if(cont > 2):
    print("Não primo")

else:
    print("Primo")