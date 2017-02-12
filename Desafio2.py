rodada = 0
vez = 0
n = 0
m = 0
escolha = int(input("\n\nESCOLHA ABAIXO UMA MODALIDADE: \n1 - Partida \n2 - Campeonato: \n"))

if(escolha == 1):
    print("Você escolheu partida!!!")
    print("\n\n*****  Iniciando o Jogo  *****")

else:
    print("Você escolheu campeonato!!!")
    print("\n\n*****  Iniciando o Jogo  *****")

# *** Função iniciar partida ***


def partida():
    global rodada
    global vez
    global n
    global m

    n = int(input("Quantas peças: "))
    m = int(input("limite de peças por jogada: "))
    
    if(rodada == 0): 
        if(n % (m + 1) == 0):
            vez = 0
            rodada = 1
            usuario_escolhe_jogada(m, n)
            
        else:
            vez = 1
            rodada = 1
            computador_escolhe_jogada(m, n)

    else:
            
        while( n != 0):
            if(vez % 2 == 0):
                computador_escolhe_jogada(m, n)
                vez = vez + 1

            else:
                usuario_escolhe_jogada(m, n)
                vez = vez + 1
        
    

# *** Função computador joga ***
def computador_escolhe_jogada(limite, pecas):
    global n
    global m
    print("n\Computador inicie o jogo!")

    retira = limite - 1
    restante = pecas - retira

    if(restante % (limite+1) != 0):
        retira =  limite
        
    n = pecas - retira

    

    print("Computador retirou ", retira, " peças")
    print("Agora restam apenas ", n, " no tabuleiro!")

# *** Função usuario joga ***
def usuario_escolhe_jogada(limite, pecas):
    global n
    global m
    
    print("\nJogador inicie o jogo!")
    retira = int(input("Retire uma quatidade de peças: "))

    if(retira > limite):
        print("Quantidade Invalida!!! Tente Novamente")
        usuario_escolhe_jogada(limite, pecas)

    n = pecas - retira

    print("Jogador retirou ", retira, "peças.")
    print("Agora restam apenas ", n, "no tabuleiro!")

# *** Chamando as funções ***
rodada = rodada + 1
partida()
