"""
Fiap
1TDSA - Segundo semestre de 2024
checkpoint 4
Arquivo: jogo da velha
Kaique Richard Suzart de Freitas Rm:555607
Lucas Nicolini Martins de Sousa Rm:557613
Gustavo Lopes Santos da Silva Rm:556859 
"""

import time
import random

# Tabuleiro global
tabuleiro = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]

def inicializarTabuleiro(tabuleiro):
    #Função na qual incializa o tabuleiro, ou seja, cria as casas para que possam ser selecionadas para fazer a jogada
    print('\n   0   1   2')
    print('0  ' + tabuleiro[0][0] + ' | ' + tabuleiro[0][1] + ' | ' + tabuleiro[0][2])
    print('   ---------')
    print('1  ' + tabuleiro[1][0] + ' | ' + tabuleiro[1][1] + ' | ' + tabuleiro[1][2])
    print('   ---------')
    print('2  ' + tabuleiro[2][0] + ' | ' + tabuleiro[2][1] + ' | ' + tabuleiro[2][2])

def imprimirTabuleiro():
    #Função a qual tem literalmente a "função" de imprimir o tabuleiro ao usuário
    inicializarTabuleiro(tabuleiro)

def leiaCoordenadaLinha():
    #Função na qual verifica se o jogador está informando as coordenadas corretas para se fazer a jogada.
    while True:
        linha = int(input('Digite a linha desejada para realizar a jogada (0 a 2): '))
        if linha in [0, 1, 2]:
            return linha
        else:
            print('Por favor, informe um valor de 0 a 2.')
            time.sleep(2)
            return leiaCoordenadaLinha()

def leiaCoordenadaColuna():
    #Função na qual tem o dever de verificar se o jogador está informando uma coluna existente
    while True:
        coluna = int(input('Digite a coluna desejada para realizar a jogada (0 a 2): '))
        if coluna in [0, 1, 2]:
            return coluna
        else:
            print('Por favor, informe um valor de 0 a 2.')
            time.sleep(2)
            return leiaCoordenadaColuna()

def posicaoValida(linha, coluna):
    #Função na qual valida se a linha e a coluna estão realmente vazias para realizar a jogada
    if tabuleiro[linha][coluna] == " ":
        return True
    else:
        return False

def verificarVencedor(simbolo):
    #Função na qual verifica o vencedor da rodada

    #Laço para verificar a linha do tabuleiro
    for linha in range(3):
        if tabuleiro[linha][0] == simbolo and tabuleiro[linha][1] == simbolo and tabuleiro[linha][2] == simbolo:
            return True #Retorna verdadeiro para o programa principal verificar e ver que há um vencedor
    #Laço para verificar a coluna do tabuleiro
    for col in range(3):
        if tabuleiro[0][col] == simbolo and tabuleiro[1][col] == simbolo and tabuleiro[2][col] == simbolo:
            return True#Retorna verdadeiro para o programa principal verificar e ver que há um vencedor

    if tabuleiro[0][0] == simbolo and tabuleiro[1][1] == simbolo and tabuleiro[2][2] == simbolo:
        return True #Retorna verdadeiro para o programa principal verificar e ver que há um vencedor
    if tabuleiro[0][2] == simbolo and tabuleiro[1][1] == simbolo and tabuleiro[2][0] == simbolo:
        return True #Retorna verdadeiro para o programa principal verificar e ver que há um vencedor

    return False #Retorna falso para dar continuidade na rodada

def verificarVelha():
    for linha in tabuleiro:
        if " " in linha:
            return False
    return True

def resetarTabuleiro():
    global tabuleiro
    tabuleiro = [[" ", " ", " "],
                 [" ", " ", " "],
                 [" ", " ", " "]]

def imprimePontuacao(vitorias_jogador1, vitorias_jogador2):
    print(f'\n\nPlacar: Jogador UM : {vitorias_jogador1} - Jogador DOIS : {vitorias_jogador2}')


def finalizar_menu():
    while True:
        print("""
|=================================|
|          FINALIZAR MENU         |
|                                 |
|[1]. Jogar novamente             |
|[2]. Sair                        |
|                                 |
|=================================|
""")
        opcao = int(input('Selecione a opção: '))
        if opcao == 1:
            return True
        elif opcao == 2:
            print('Saindo do programa. Até a próxima!')
            return False
        else:
            print('Opção inválida! Por favor, selecione uma opção existente.')
            return finalizar_menu()

def jogar(linha, coluna, simbolo):
    if posicaoValida(linha, coluna):
        tabuleiro[linha][coluna] = simbolo
        return True
    else:
        print("Posição já ocupada! Tente novamente.")
        return False

def modoFacil():
    print('===========================================================================================')
    print('\nNeste modo, você será o *JOGADOR UM* e jogará contra o computador *JOGADOR DOIS* (fácil).')
    print('===========================================================================================')
    time.sleep(2)

    vitorias_jogador = 0
    vitorias_computador = 0

    simbolo_jogador = 'X'
    simbolo_computador = 'O'

    # Define o jogador inicial
    jogador_atual = simbolo_jogador

    while vitorias_jogador < 3 and vitorias_computador < 3:
        resetarTabuleiro()
        imprimePontuacao(vitorias_jogador, vitorias_computador)
        time.sleep(2)
        print(f'\nO jogador {jogador_atual} começa!')
        time.sleep(2)

        while True:
            imprimirTabuleiro()
            if jogador_atual == simbolo_jogador:
                print(f'\nSua vez [{simbolo_jogador}]')
                time.sleep(2)

                linha = leiaCoordenadaLinha()
                coluna = leiaCoordenadaColuna()

                if jogar(linha, coluna, jogador_atual):
                    if verificarVencedor(jogador_atual):
                        time.sleep(3)
                        imprimirTabuleiro()
                        print(f'\n\n➡️  O jogador [{jogador_atual}] venceu!')
                        vitorias_jogador += 1
                        time.sleep(3)
                        break
                    elif verificarVelha():
                        imprimirTabuleiro()
                        print('\nEmpate!')
                        time.sleep(3)
                        break
                    jogador_atual = simbolo_computador
            else:
                if jogadaMaquinaFacil(simbolo_computador):
                    if verificarVencedor(simbolo_computador):
                        time.sleep(3)
                        imprimirTabuleiro()
                        print(f'\n\n➡️  O computador [{simbolo_computador}] venceu!')
                        vitorias_computador += 1
                        break
                    elif verificarVelha():
                        imprimirTabuleiro()
                        print('\nEmpate!')
                        time.sleep(3)
                        break
                    jogador_atual = simbolo_jogador
                

        # Verifica se algum jogador atingiu 3 vitórias para declarar o vencedor e encerrar o jogo
        if vitorias_jogador == 3:
            print('\n🎉 O jogador venceu a partida!')
            imprimePontuacao(vitorias_jogador, vitorias_computador)
            time.sleep(3)
            imprimeMenuPrincipal()
            return
        elif vitorias_computador == 3:
            print('\n🎉 O computador venceu a partida!')
            imprimePontuacao(vitorias_jogador, vitorias_computador)
            time.sleep(3)
            imprimeMenuPrincipal()
            return
        
        # Condição para questionar o usuário se deseja continuar
        sair = input('Deseja continuar? Se sim, digite qualquer tecla, senão "N": ').upper()
        if sair == 'N':
            imprimeMenuPrincipal()
            return


def jogadaMaquinaFacil(simbolo_computador):
    jogador_atual = simbolo_computador
    print(f'Vez do computador ({simbolo_computador})')
    time.sleep(3)
    while True:
        linha = random.choice([0, 1, 2])
        coluna = random.choice([0, 1, 2])
        if jogar(linha, coluna, simbolo_computador):
            break
    return False



def modoHard():  
    print('\nNeste modo, você será o *JOGADOR 1* e jogará contra o computador (hard).')
    time.sleep(2)

    vitorias_jogador = 0
    vitorias_computador = 0

    while True:
        simbolo_jogador = input('\nQual símbolo você deseja escolher? [X] ou [O]: ').upper()
        if simbolo_jogador in ['X', 'O']:
            if simbolo_jogador == 'X':
                simbolo_computador = 'O'
            else:
                simbolo_computador = 'X'
            time.sleep(2)
            print(f'\nO computador jogará com o [ {simbolo_computador} ].')
            time.sleep(2)
            break
        else:
            print('\nEscolha inválida. Por favor, escolha [X] ou [O].')
            time.sleep(1)

    
    while vitorias_jogador < 3 or vitorias_computador < 3:
        resetarTabuleiro()
        imprimePontuacao(vitorias_jogador, vitorias_computador)
        time.sleep(2)
        jogador_atual = random.choice([simbolo_jogador, simbolo_computador])
        print(f'\nO jogador {jogador_atual} começa!')
        time.sleep(2)

        while True:
            imprimirTabuleiro()
            if jogador_atual == simbolo_jogador:
                print(f'\nSua vez [{jogador_atual}]')
                time.sleep(2)

                linha = leiaCoordenadaLinha()
                coluna = leiaCoordenadaColuna()

                if jogar(linha, coluna, jogador_atual):
                    if verificarVencedor(jogador_atual):
                        time.sleep(3)
                        imprimirTabuleiro()
                        print(f'\n\n➡️  O jogador [{jogador_atual}] venceu!')
                        vitorias_jogador += 1
                        time.sleep(3)
                        break
                    elif verificarVelha():
                        imprimirTabuleiro()
                        print('\nEmpate!')
                        break
                    jogador_atual = simbolo_computador
  
            else:
                if jogadaMaquinaHard(simbolo_computador):  
                    vitorias_computador += 1
                    break
                jogador_atual = simbolo_jogador

        if vitorias_jogador == 3:
            print('\n🎉 O jogador venceu a partida!')
            imprimePontuacao(vitorias_jogador, vitorias_computador)
            time.sleep(3)
            imprimeMenuPrincipal()
            return  
        elif vitorias_computador == 3:
            print('\n🎉 O computador venceu a partida!')
            imprimePontuacao(vitorias_jogador, vitorias_computador)
            time.sleep(3)
            imprimeMenuPrincipal()
            return  
        
        sair = input('Deseja continuar? Se sim, digite qualquer tecla, senão "N": ').upper()
        if sair == 'N':
            imprimeMenuPrincipal()
            return

    

def jogadaMaquinaHard(simbolo_computador):
    print(f'Vez do computador ({simbolo_computador})')
    time.sleep(3)

    # Tentativa de ganhar
    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] == ' ':
                tabuleiro[linha][coluna] = simbolo_computador
                if verificarVencedor(simbolo_computador):
                    imprimirTabuleiro()
                    time.sleep(2)
                    print(f'\n\n➡️  O computador ({simbolo_computador}) venceu!')
                    return True
                else:
                    tabuleiro[linha][coluna] = ' '  # desfaz o movimento

    # Tentativa de bloquear o jogador
    if simbolo_computador == 'X':
        simbolo_jogador = 'O'
    else:
        simbolo_jogador = 'X'
    
    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] == ' ':
                tabuleiro[linha][coluna] = simbolo_jogador
                if verificarVencedor(simbolo_jogador):
                    tabuleiro[linha][coluna] = simbolo_computador  # bloqueia a jogada do jogador
                    return False
                else:
                    tabuleiro[linha][coluna] = ' '  # desfaz o movimento

    # Jogada aleatória (caso não haja chances de vitória ou bloqueio)
    while True:
        linha = random.choice([0, 1, 2])
        coluna = random.choice([0, 1, 2])
        if tabuleiro[linha][coluna] == ' ':
            tabuleiro[linha][coluna] = simbolo_computador
            break

    # Verifica se o computador ganhou ou se houve empate
    if verificarVencedor(simbolo_computador):
        imprimirTabuleiro()
        time.sleep(2)
        print(f'\n\n➡️  O computador ({simbolo_computador}) venceu!')
        return True
    elif verificarVelha():
        imprimirTabuleiro()
        print('\nEmpate!')
        return True

    return False

def modoJogador():
    print('===============================================')
    print('*Neste modo, dois jogadores irão se enfrentar.*')
    print('===============================================')
    time.sleep(2)

    #Contador de vitórias
    vitorias_jogador1 = 0
    vitorias_jogador2 = 0

    #Variavel para cada jogador 
    jogador1 = 'X'
    jogador2 = 'O'

    jogador_atual = jogador1

    while vitorias_jogador1 < 3 and vitorias_jogador2 < 3:
        resetarTabuleiro()  
        imprimePontuacao(vitorias_jogador1, vitorias_jogador2)
        print(f'\nO {jogador_atual} começa!')

        while True:
            imprimirTabuleiro()
            print(f'\nVez do jogador [{jogador_atual}]')

            linha = leiaCoordenadaLinha()
            coluna = leiaCoordenadaColuna()
            
            if jogar(linha, coluna, jogador_atual):
                if verificarVencedor(jogador_atual):
                    imprimirTabuleiro()
                    if jogador_atual == jogador1:
                        print(f'\n\n➡️  O Jogador UM [{jogador_atual}] venceu!')
                        vitorias_jogador1 += 1
                    else:
                        print(f'\n\n➡️  O Jogador DOIS [{jogador_atual}] venceu!')
                        vitorias_jogador2 += 1
                    time.sleep(3)
                    break
                elif verificarVelha():
                    imprimirTabuleiro()
                    print('\nEmpate!')
                    time.sleep(3)
                    break  # Sai do loop de jogo para reiniciar com outro jogador

                
                jogador_atual = jogador2 if jogador_atual == jogador1 else jogador1

        # Verifica se algum jogador atingiu 3 vitórias para declarar o vencedor e encerrar o jogo
        if vitorias_jogador1 == 3:
            print('\n🎉 O jogador UM venceu a partida!')
            imprimePontuacao(vitorias_jogador1, vitorias_jogador2)
            time.sleep(3)
            imprimeMenuPrincipal()
            return
        elif vitorias_jogador2 == 3:
            print('\n🎉 O jogador DOIS venceu a partida!')
            imprimePontuacao(vitorias_jogador1, vitorias_jogador2)
            time.sleep(3)
            imprimeMenuPrincipal()
            return
        
        # Alterna o jogador que começará a próxima partida se houve empate
        if verificarVelha():
            if jogador_atual == jogador2:
                jogador_atual == jogador1 
            else:
                jogador_atual == jogador2

        # Condição para questionar o usuário se deseja continuar
        sair = input('Deseja continuar? Se sim, digite qualquer tecla, senão "N": ').upper()
        if sair == 'N':
            imprimeMenuPrincipal()
            return

    

def imprimeMenuPrincipal():
    print("""
|=====================================|
|             MENU                    |
|                                     |
|[1]. Jogador Vs Jogador              |
|[2]. Jogador Vs Computador (Fácil)   |
|[3]. Jogador Vs Computador (Difícil) |
|[4]. Sair                            |
|                                     |
|=====================================|
""")
    escolha = int(input('Escolha uma das opções: '))
    if escolha == 1:
        modoJogador()
    elif escolha == 2:
        modoFacil()
    elif escolha == 3:
        modoHard()
    elif escolha == 4:
        print('Saindo...')
    else:
        print('Opção inválida! Tente novamente.')
        imprimeMenuPrincipal()

# Início do programa
imprimeMenuPrincipal()
