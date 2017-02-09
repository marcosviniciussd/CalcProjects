import math

def main():
    a = float(input("Digite o valor de 'a': "))
    b = float(input("Digite o valor de 'b': "))
    c = float(input("Digite o valor de 'c': "))
    imprimi(a, b, c)

def delta(a, b, c):
    return (b ** 2) - (4 * a * c)

def imprimi(a, b, c):  
    if (delta(a, b, c) < 0):
        print("esta equação não possui raízes reais")

    elif(delta(a, b, c) == 0):
        x1 = (-b + math.sqrt(delta(a, b, c))) / (2 * a)
        print("a raiz desta equação é ", x1)

    else:
        x1 = (-b + math.sqrt(delta(a, b, c))) / (2 * a)
        x2 = (-b - math.sqrt(delta(a, b, c))) / (2 * a)

        if(x1 < x2):
            print("as raízes da equação são ", x1, " e ", x2)

        else:
            print("as raízes da equação são ", x2, " e ", x1)

main()