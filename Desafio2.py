
escolha = int(input("\n\nESCOLHA ABAIXO UMA MODALIDADE: \n1 - Partida \n2 - Campeonato: \n"))

if(escolha == 1):
    print("Você escolheu partida!!!")
    print("\n\n*****  Iniciando o Jogo  *****")

else:
    print("Você escolheu campeonato!!!")
    print("\n\n*****  Iniciando o Jogo  *****")

# *** Função iniciar partida ***
def partida():
    n = int(input("Quantas peças: "))
    m = int(input("limite de peças por jogada: "))

    while(n != 0):
        if(n % (m + 1) == 0):
            computador_escolhe_jogada(m, n)
    
        else:
            usuario_escolhe_jogada(m, n)
    
    

# *** Função computador joga ***
def computador_escolhe_jogada(limite, pecas):
    print("n\Computador inicie o jogo!")

    retira = limite - 1
    restante = pecas - retira

    if(restante % (limite+1) != 0):
        retira =  limite
        n = pecas - limite
    n = pecas - retira

    

    print("Computador retirou ", retira, " peças")
    print("Agora restam apenas ", n, " no tabuleiro!")

# *** Função usuario joga ***
def usuario_escolhe_jogada(limite, pecas):
    print("\nJogador inicie o jogo!")
    retira = int(input("Retire uma quatidade de peças: "))

    if(retira > limite):
        print("Quantidade Invalida!!! Tente Novamente")
        usuario_escolhe_jogada(limite, pecas)

    n = pecas - retira

    print("Jogador retirou ", retira, "peças.")
    print("Agora restam apenas ", n, "no tabuleiro!")

# *** Chamando as funções ***
partida()
