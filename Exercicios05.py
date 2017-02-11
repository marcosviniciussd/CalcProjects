def main():
    letra = input("Digite uma letra: ")
    mensagem = vogal(letra)
    print(mensagem)

def vogal(let):
    verdadeiro = True
    falso = False

    if(let == 'a' or let == "A" 
    or let == "e" or let == "E" 
    or let == "i" or let == "I"
    or let == "o" or let == "O" 
    or let == "u" or let == "U"):
        return verdadeiro

    else:
        return falso

main()
