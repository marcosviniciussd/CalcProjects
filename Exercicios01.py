def main():
    numero = int(input("Digite um numero inteiro: "))
    mensagem = fizzbuzz(numero)
    print(mensagem)

def fizzbuzz(a):
    div1 = a % 5
    div2 = a % 3

    if(div1 == 0 and div2 == 0):
        return("FizzBuzz")
    
    elif (div1 == 0):
        return("Buzz")
    
    elif(div2 == 0):
        return("Fizz")

    else:
        return a

main()
