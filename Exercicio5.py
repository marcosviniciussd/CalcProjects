numero = int(input("Digite um numero inteiro: "))

div1 = numero % 5
div2 = numero % 3

if(div1 == 0 and div2 == 0):
    print("FizzBuzz")

else:
    print(numero)