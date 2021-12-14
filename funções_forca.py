from principal_forca_multiplayer import main
from time import sleep
from termcolor import cprint

lista_erros_jogador1 = []
lista_erros_jogador2 = []
lista_com_tema_escolhido = []

def dicionario_comidas():
    comidas = {1: 'abacate',
               2: 'banana', 3: 'morango',
               4: 'tabasco', 5: 'abobrinha',
               6: 'lentilhas', 7: 'damasco',
               8: 'aveia', 9: 'aspargos', 10: 'tomate'
               }
    return comidas


def dicionario_paises():
    paises = {1: 'lesoto', 2: 'eswatini',
              3: 'mianmar', 4: 'filipinas',
              5: 'letonia', 6: 'letonia',
              7: 'madagascar', 8: 'lituania',
              9: 'laos', 10: 'botsuana'
              }
    return paises


def dicionario_palavras():
    palavras = {1: 'anticonstitucionalissimamente',
                2: 'paraclorobenzilpirrolidinonetilbenzimidazol',
                3: 'xaropear', 4: 'quintessencia', 5: 'vicissitude',
                6: 'tergiversar', 7: 'putrefato', 8: 'verossimilhança',
                9: 'zaragatoa', 10: 'hipopotomonstrosesquipedaliofobia'
                }
    return palavras


def pergunta_escolha_tema_j1():
    dicionario_atual = {}
    escolha_tema = int(input('Escolha um nível de dificuldade, Jogador1 \n[1] Fácil [2] Médio [3] Difícil:'))
    if escolha_tema == 1:
        print('\nJOGADOR 1, você escolheu o nível fácil com o tema Frutas!')
        dicionario_atual = dicionario_comidas()

    if escolha_tema == 2:
        print('\nJOGADOR 1, você escolheu o nível médio com o tema Países!')
        dicionario_atual = dicionario_paises()

    if escolha_tema == 3:
        print('\nJOGADOR 1, você escolheu o nível difícil com o tema Palavras!')
        dicionario_atual = dicionario_palavras()

    palavra_escolhida = int(input('\nDigite um nº de 1 a 10 e sortearemos uma palavra, JOGADOR 1:\n'))
    print('-='* 35)
    palavra_escolhida = dicionario_atual[palavra_escolhida]
    return palavra_escolhida


def pergunta_escolha_tema_j2():
    cprint('JOGADOR 2\n', 'red')
    dicionario_atual = {}
    escolha_tema = int(input('Escolha um nível de dificuldade, JOGADOR 2 \n[1] Fácil [2] Médio [3] Difícil:'))
    if escolha_tema == 1:
        print('\nJOGADOR 2, você escolheu o nível fácil com o tema Frutas!')
        dicionario_atual = dicionario_comidas()

    if escolha_tema == 2:
        print('\nJOGADOR 2, você escolheu o nível médio com o tema Países!')
        dicionario_atual = dicionario_paises()

    if escolha_tema == 3:
        print('\nJOGADOR 2, você escolheu o nível difícil com o tema Palavras!')
        dicionario_atual = dicionario_palavras()

    palavra_escolhida = int(input('\nDigite um nº de 1 a 10 e sortearemos uma palavra, JOGADOR 2:\n'))
    print('-='* 35)
    palavra_escolhida = dicionario_atual[palavra_escolhida]
    return palavra_escolhida


def jogar():
    abertura()
    imprimir_msg_abertura()
    global palavra_secreta_jogador1
    global palavra_secreta_jogador2
    global letras_acertadas_jogador1
    global letras_acertadas_jogador2

    palavra_secreta_jogador1 = pergunta_escolha_tema_j1()
    palavra_secreta_jogador2 = pergunta_escolha_tema_j2()
    letras_acertadas_jogador1 = ['_' for letra in palavra_secreta_jogador1]
    letras_acertadas_jogador2 = ['_' for letra in palavra_secreta_jogador2]


def abertura():
    cprint('███████╗ ██████╗ ██████╗  ██████╗ █████╗ ', 'blue')
    cprint('██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔══██╗', 'blue')
    cprint('█████╗  ██║   ██║██████╔╝██║     ███████║', 'blue')
    cprint('██╔══╝  ██║   ██║██╔══██╗██║     ██╔══██║', 'blue')
    cprint('██║     ╚██████╔╝██║  ██║╚██████╗██║  ██║', 'blue')
    cprint('╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝', 'blue')


def imprimir_msg_abertura():
    print('*****************************************')
    print('****** Bem-vindo ao jogo da Forca *******')
    print('*****************************************')
    sleep(2)

    print('\nNinguém tem a menor ideia de quem inventou esse jogo simples,')
    sleep(1)
    print('dizem que ele surgiu na Inglaterra, mas seu primeiro registro oficial')
    sleep(1)
    print('data de 1894 no livro “Traditional Games”')
    sleep(1)

    print('\nEste é um jogo para dois jogadores, chame seu adversário e que vença o melhor!')
    sleep(1)

    print('\nVocê começa JOGADOR 1\n')
    sleep(1)


def contador_lista_erros_jogador1(chute, lista_erros_jogador1):
    if chute not in palavra_secreta_jogador1:
        lista_erros_jogador1.append(chute)
        while (len(lista_erros_jogador1) <= 7):
            print('Ops, você errou! Faltam {} tentativas'.format(
                7 - len(lista_erros_jogador1)))
            sleep(1)
            desenha_forca_j1(len(lista_erros_jogador1))

            print('\nVez do JOGADOR 2:\n')
            p2jogando()


def contador_lista_erros_jogador2(chute, lista_erros_jogador2):
    if chute not in palavra_secreta_jogador2:
        lista_erros_jogador2.append(chute)
        while (len(lista_erros_jogador2) <= 7):
            print('Ops, você errou! Faltam {} tentativas'.format(
                7 - len(lista_erros_jogador2)))
            sleep(1)
            desenha_forca_j2(len(lista_erros_jogador2))

            print('\nVez do JOGADOR 1:\n')
            p1jogando()


def desenha_forca_j1(lista_erros_jogador1):
    print("  _______     ")
    print(" |/      |    ")

    if lista_erros_jogador1 == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if lista_erros_jogador1 == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if lista_erros_jogador1 == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if lista_erros_jogador1 == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if lista_erros_jogador1 == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if lista_erros_jogador1 == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if lista_erros_jogador1 == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")
        print('ENFORCADO JOGADOR 1')
        mensagem_enforcou_j1(palavra_secreta_jogador1)

    print(" |            ")
    print("_|___         ")
    sleep(0.5)


def desenha_forca_j2(lista_erros_jogador2):
    print("  _______     ")
    print(" |/      |    ")

    if lista_erros_jogador2 == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if lista_erros_jogador2 == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if lista_erros_jogador2 == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if lista_erros_jogador2 == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if lista_erros_jogador2 == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if lista_erros_jogador2 == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if lista_erros_jogador2 == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")
        print('ENFORCADO JOGADOR 2')
        mensagem_enforcou_j2(palavra_secreta_jogador2)

    print(" |            ")
    print("_|___         ")
    sleep(0.5)


def p1jogando():
    enforcou_jogador1 = False
    acertou_jogador1 = False

    while not acertou_jogador1 and not enforcou_jogador1:
        p1jogando = True

        while p1jogando:
            cprint('\nJOGADOR 1\n', 'blue')
            cprint(letras_acertadas_jogador1, 'blue')
            cprint(f'\nLista de chutes errados, JOGADOR 1:{lista_erros_jogador1}','yellow')
            chute = str(input('\nQual letra:')).lower().strip()

            if chute in palavra_secreta_jogador1:
                indice = 0
                for letra in palavra_secreta_jogador1:
                    if chute == letra:
                        letras_acertadas_jogador1[indice] = letra
                    indice += 1

            if (len(lista_erros_jogador1) == 7):
                enforcou_jogador1 = True
                mensagem_enforcou_j1()

            if '_' not in letras_acertadas_jogador1:
                acertou_jogador1 = True
                mensagem_acertou_j1()

            else:
                contador_lista_erros_jogador1(chute, lista_erros_jogador1)

    p1jogando = False


def p2jogando():
    enforcou_jogador2 = False
    acertou_jogador2 = False

    while not acertou_jogador2 and not enforcou_jogador2:
        p2jogando = True

        while p2jogando:
            cprint('\nJOGADOR 2\n', 'red')
            cprint(letras_acertadas_jogador2, 'red')
            cprint(f'\nLista de chutes errados, JOGADOR 2:{lista_erros_jogador2}','yellow')
            chute = str(input('\nQual letra:')).lower().strip()

            if chute in palavra_secreta_jogador2:
                indice = 0
                for letra in palavra_secreta_jogador2:
                    if chute == letra:
                        letras_acertadas_jogador2[indice] = letra
                    indice += 1

            if (len(lista_erros_jogador2) == 7):
                enforcou_jogador2 = True
                mensagem_enforcou_j2()

            if '_' not in letras_acertadas_jogador2:
                acertou_jogador2 = True
                mensagem_acertou_j2()

            else:
                contador_lista_erros_jogador2(chute, lista_erros_jogador2)

    p2jogando = False


def jogar_novamente():
    resposta_jogarnovamente = input('Deseja jogar novamente? [S/N]')
    if (resposta_jogarnovamente).upper() == 'S':
        lista_erros_jogador1.clear()
        lista_erros_jogador2.clear()
        main()

    elif (resposta_jogarnovamente).upper() == 'N':
        print('Até a próxima!')
        exit()

    else:
        print('Digite uma resposta válida!')
        jogar_novamente()


def mensagem_enforcou_j1(palavra_secreta_jogador1):
    print('\nPoxa vida, você perdeu JOGADOR 1!')
    sleep(0.5)
    print(f'A palavra era: {palavra_secreta_jogador1.upper()}')
    sleep(0.5)
    cprint("\n       @@@@@@@@@@@@@@@@@@", 'red')
    cprint("     @@@@@@@@@@@@@@@@@@@@@@@", 'red')
    cprint("   @@@@@@@@@@@@@@@@@@@@@@@@@@@", 'red')
    cprint("  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@", 'red')
    cprint(" @@@@@@@@@@@@@@@/      \@@@/   @", 'red')
    cprint("@@@@@@@@@@@@@@@@\      @@  @___@", 'red')
    cprint("@@@@@@@@@@@@@ @@@@@@@@@@  | \@@@@@", 'red')
    cprint("@@@@@@@@@@@@@ @@@@@@@@@\__@_/@@@@@", 'red')
    cprint(" @@@@@@@@@@@@@@@/,/,/./'/_|.\\,\'", 'red')
    cprint("   @@@@@@@@@@@@@|  | | | | | | | |", 'red')
    cprint("                 \_|_|_|_|_|_|_|_|", 'red')


def mensagem_enforcou_j2(palavra_secreta_jogador2):
    print('\nPoxa vida, você perdeu JOGADOR 2!')
    sleep(0.5)
    print(f'A palavra era {palavra_secreta_jogador2.upper()}')
    sleep(0.5)
    cprint("\n       @@@@@@@@@@@@@@@@@@", 'red')
    cprint("     @@@@@@@@@@@@@@@@@@@@@@@", 'red')
    cprint("   @@@@@@@@@@@@@@@@@@@@@@@@@@@", 'red')
    cprint("  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@", 'red')
    cprint(" @@@@@@@@@@@@@@@/      \@@@/   @", 'red')
    cprint("@@@@@@@@@@@@@@@@\      @@  @___@", 'red')
    cprint("@@@@@@@@@@@@@ @@@@@@@@@@  | \@@@@@", 'red')
    cprint("@@@@@@@@@@@@@ @@@@@@@@@\__@_/@@@@@", 'red')
    cprint(" @@@@@@@@@@@@@@@/,/,/./'/_|.\\,\'", 'red')
    cprint("   @@@@@@@@@@@@@|  | | | | | | | |", 'red')
    cprint("                 \_|_|_|_|_|_|_|_|", 'red')
    
    jogar_novamente()


def mensagem_acertou_j1():
    print("\nParabéns, você ganhou JOGADOR 1!")
    sleep(1)
    cprint(" _______________", 'yellow')
    cprint("|@@@@|     |####|", 'yellow')
    cprint("|@@@@|     |####|", 'yellow')
    cprint("|@@@@|     |####|", 'yellow')
    cprint("\@@@@|     |####/", 'yellow')
    cprint(" \@@@|     |###/", 'yellow')
    cprint("  `@@|_____|##'", 'yellow')
    cprint("       (O)", 'yellow')
    cprint("    .-'''''-.", 'yellow')
    cprint("  .'  * * *  `.", 'yellow')
    cprint(" :  *       *  :", 'yellow')
    cprint(": ~  PARABÉNS ~ :", 'yellow')
    cprint(": ~ JOGADOR 1 ~ :", 'yellow')
    cprint(" :  *       *  :", 'yellow')
    cprint("  `.  * * *  .'", 'yellow')
    cprint("    `-.....-'", 'yellow')
    sleep(1)
    print('\n*** FIM DE JOGO! ****')
    jogar_novamente()


def mensagem_acertou_j2():
    print("\nParabéns, você ganhou JOGADOR 2!")
    sleep(1)
    cprint(" _______________", 'yellow')
    cprint("|@@@@|     |####|", 'yellow')
    cprint("|@@@@|     |####|", 'yellow')
    cprint("|@@@@|     |####|", 'yellow')
    cprint("\@@@@|     |####/", 'yellow')
    cprint(" \@@@|     |###/", 'yellow')
    cprint("  `@@|_____|##'", 'yellow')
    cprint("       (O)", 'yellow')
    cprint("    .-'''''-.", 'yellow')
    cprint("  .'  * * *  `.", 'yellow')
    cprint(" :  *       *  :", 'yellow')
    cprint(": ~  PARABÉNS ~ :", 'yellow')
    cprint(": ~ JOGADOR 2 ~ :", 'yellow')
    cprint(" :  *       *  :", 'yellow')
    cprint("  `.  * * *  .'", 'yellow')
    cprint("    `-.....-'", 'yellow')
    sleep(1)
    print('\n*** FIM DE JOGO! ****')
    jogar_novamente()


if (__name__ == '__main__'):
    jogar()
