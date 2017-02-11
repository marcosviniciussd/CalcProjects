def main():
    letra = input("Digite uma letra: ")
    mensagem = vogal(letra)
    print(mensagem)

def vogal(letra):
    verdadeiro = True
    falso = False

    if(letra == 'a' or letra == "A" 
    or letra == "e" or letra == "E" 
    or letra == "i" or letra == "I"
    or letra == "o" or letra == "O" 
    or letra == "u" or letra == "U"):
        return verdadeiro

    else:
        return falso

main()
