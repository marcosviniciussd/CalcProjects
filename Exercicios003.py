
num = int(input("Digite um número: "))

soma = 0
x = 0

while(num // 10 != 0):
    
    x = num % 10
    soma = soma + x
    num = num // 10

    if(num // 10 == 0):
        soma = soma + num
        
print(soma)