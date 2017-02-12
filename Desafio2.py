
escolha = int(input("\n\nESCOLHA ABAIXO UMA MODALIDADE: \n1 - Partida \n2 - Campeonato"))

if(escolha == 1):
    print("Você escolheu partida!!!")
    print("\n\n*****  Iniciando o Jogo  *****")

else:
    print("Você escolheu campeonato!!!")
    print("\n\n*****  Iniciando o Jogo  *****")

def partida():
    n = int(input("Quantas peças: "))
    m = int(input("limite de peças por jogada: "))

    if(n % m + 1 == 0):
        computador_escolhe_jogada(m, n)
    
    else:
        usuario_escolhe_jogada(m, n)


def computador_escolhe_jogada(m, n):
    print("n\Computador inicie o jogo!")

    computador = (m - n) + 1
    pecas = (n - m)

    print("Computador retirou ", pecas, " peças")
    print("Agora restam apenas ", pecas, " no tabuleiro!")

def usuario_escolhe_jogada(n, m):
    print("\nJogador inicie o jogo!")
    retira = int(input("Retire uma quatidade de peças: "))

    jogador = m - n
    pecas = (n - m)
    jogada1 = (n - m) + 1

    print("Jogador retirou ", jogador, "peças.")
    print("Agora restam apenas ", pecas, "no tabuleiro!")

partida()
