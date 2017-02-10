def main():
    numero = int(input("Digite um numero inteiro: "))
    numero_divisivel()

def numero_divisivel(a):
    div1 = numero % 5
    div2 = numero % 3
    return div1, div2

    if(div1 == 0 and div2 == 0):
        print("FizzBuzz")
    
    elif (div1 == 0):
        print("Buzz")
    
    elif(div2 == 0):
        print("Fizz")

    else:
        return a

main()