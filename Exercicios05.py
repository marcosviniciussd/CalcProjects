def main():
    letra = input("Digite uma letra: ")
    mensagem = vogal(letra)
    print(mensagem)

def vogal(letra):
    if(letra == 'a' or letra == "e" or letra == "i" or letra == "o" or letra == "u"):
        return "True"

    else:
        return "False"

main()
