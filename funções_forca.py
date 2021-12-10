comidas = {1:'abacate',
    2:'banana',3:'morango',
    4:'tabasco',5:'abobrinha',
    6:'lentilhas',7:'damasco',
    8:'aveia',9: 'aspargos',10:'tomate'
    }

paises = {1:'lesoto',2:'eswatini',
          3:'mianmar',4:'filipinas',
          5:'letonia',6:'letonia',
          7:'madagascar',7:'guatemala',
          8:'lituania',9:'laos',
          10:'botsuana'
          }

palavras = {1:'anticonstitucionalissimamente',
            2:'paraclorobenzilpirrolidinonetilbenzimidazol',
            3:'xaropear', 4:'quintessencia',5:'vicissitude',
            6:'tergiversar',7:'putrefato',8:'verossimilhança',
            9:'zaragatoa',10:'hipopotomonstrosesquipedaliofobia'
}

def apresenta_níveis():
    print('[1]Fácil [Frutas]\n [2]Médio [Países]\n[3]Difícil [Palavras)')

def escolha_tema():
    escolha_palavra = int(input('Escolha um nível de dificuldade:'))
    if escolha_palavra == 1:
        print('Você escolheu o nível Fácil com o tema Frutas!')
        #importdicionário do tema
    if escolha_palavra == 2:
        print('Você escolheu o nível Médio com o tema Países!')
        # importdicionário do tema
    if escolha_palavra == 3:
        print('Você escolheu o nível Difícil com o tema Palavras!')
        # importdicionário do tema

def escolha_palavra_dicionário_1():
    escolha_palavra = int(input('Escolha um n° de 1 a 10 e sortearemos uma palavra:'))
    if escolha_palavra in comidas.items():


from principal_forca_multiplayer import main
from time import sleep
from termcolor import cprint

palavra_secreta_jogador1 = 'abacate'
palavra_secreta_jogador2 = 'morango'

letras_acertadas_jogador1 = ['_' for letra in palavra_secreta_jogador1]
letras_acertadas_jogador2 = ['_' for letra in palavra_secreta_jogador2]

lista_erros_jogador1 = []
lista_erros_jogador2 = []

def jogar():
    abertura()
    imprimir_msg_abertura()


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

    print('\nEste é um jogo para dois jogadores, chame seu adversário e que vença o melhor!')
    sleep(1)

    print('\nVocê começa jogador1\n')
    sleep(1)


def contador_lista_erros_jogador1(chute, lista_erros_jogador1):
    if chute not in palavra_secreta_jogador1:
        lista_erros_jogador1.append(chute)
        print('Ops, você errou! Faltam {} tentativas'.format(len(palavra_secreta_jogador1) - len(lista_erros_jogador1)))
        sleep(1)
        desenha_forca_j1(len(lista_erros_jogador1))

        print('\nVez do jogador 2:\n')
        p2jogando()


def contador_lista_erros_jogador2(chute, lista_erros_jogador2):
    if chute not in palavra_secreta_jogador2:
        lista_erros_jogador2.append(chute)
        while (len(lista_erros_jogador2) < len(palavra_secreta_jogador2)):
            print('Ops, você errou! Faltam {} tentativas'.format(len(palavra_secreta_jogador2) - len(lista_erros_jogador2)))
            sleep(1)
            desenha_forca_j2(len(lista_erros_jogador2))

            print('\nVez do jogador 1:\n')
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
            print(letras_acertadas_jogador1)
            chute = str(input('\nQual letra:')).lower().strip()

            if chute in palavra_secreta_jogador1:
                indice = 0
                for letra in palavra_secreta_jogador1:
                    if chute == letra:
                        letras_acertadas_jogador1[indice] = letra
                    indice += 1

            if (len(lista_erros_jogador1) == len(palavra_secreta_jogador1)):
                enforcou_jogador1 = True

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
            print(letras_acertadas_jogador2)
            chute = str(input('\nQual letra:')).lower().strip()

            if chute in palavra_secreta_jogador2:
                indice = 0
                for letra in palavra_secreta_jogador2:
                    if chute == letra:
                        letras_acertadas_jogador2[indice] = letra
                    indice += 1

            if (len(lista_erros_jogador2) == len(palavra_secreta_jogador2)):
                enforcou_jogador2 = True

            if '_' not in letras_acertadas_jogador2:
                acertou_jogador2 = True
                mensagem_acertou_j2()

            else:
                contador_lista_erros_jogador2(chute, lista_erros_jogador2)
                mensagem_enforcou_j2(palavra_secreta_jogador2)

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
    print('\nPoxa vida, você perdeu jogador 1!')
    sleep(0.5)
    print(f'A palavra era: {palavra_secreta_jogador1.upper()}')
    sleep(0.5)
    print("\n    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")



def mensagem_enforcou_j2(palavra_secreta_jogador2):
    print('\nPoxa vida, você perdeu jogador 2!')
    sleep(0.5)
    print(f'A palavra era {palavra_secreta_jogador2.upper()}')
    sleep(0.5)
    print("\n    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

    jogar_novamente()


def mensagem_acertou_j1():
    print("\nParabéns, você ganhou jogador 1!")
    sleep(1)
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
    sleep(1)
    print('\n*** FIM DE JOGO! ****')
    exit()


def mensagem_acertou_j2():
    print("\nParabéns, você ganhou jogador 2!")
    sleep(1)
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
    sleep(1)
    print('\n*** FIM DE JOGO! ****')
    exit()


if (__name__ == '__main__'):
    jogar()