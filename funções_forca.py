palavra_secreta_jogador1 = 'abacate'
palavra_secreta_jogador2 = 'morango'

letras_acertadas_jogador1 = ['_' for letra in palavra_secreta_jogador1]
letras_acertadas_jogador2 = ['_' for letra in palavra_secreta_jogador2]


def imprimir_msg_abertura():
    print('*****************************************')
    print('****** Bem-vindo ao jogo da Forca *******')
    print('*****************************************')

    print('\nEste é um jogo para dois jogadores, chame seu adversário e que vença o melhor!')

    print('\nVocê começa jogador1')

    p1jogando()


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if (erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def p1jogando():
    enforcou_jogador1 = False
    acertou_jogador1 = False
    erros_jogador1 = 0

    while not acertou_jogador1 and not enforcou_jogador1:
        p1jogando = True
        p2jogando = False

        while p1jogando:
            chute = str(input('Qual letra:')).lower().strip()
            if chute in palavra_secreta_jogador1:
                indice = 0
                for letra in palavra_secreta_jogador1:
                    if chute == letra:
                        letras_acertadas_jogador1[indice] = letra
                    indice += 1
                print(letras_acertadas_jogador1)

            else:
                erros_jogador1 += 1
                print('Ops, você errou! Faltam {} tentativas'.format(len(palavra_secreta_jogador1) - erros_jogador1))
                desenha_forca(erros_jogador1)

                print('Vez do jogador 2:')
                p1jogando = False
                p2jogando = True

            enforcou_jogador1 = erros_jogador1 == len(palavra_secreta_jogador1)
            acertou_jogador1 = '_' not in letras_acertadas_jogador1

            if acertou_jogador1:
                print('Você ganhou jogador1, parabéns!')
                print('***FIM DO JOGO***')
                break

            elif enforcou_jogador1:
                print('Poxa vida, você perdeu!')


def p2jogando():
    enforcou_jogador2 = False
    acertou_jogador2 = False
    erros_jogador2 = 0

    while p2jogando:
        chute = str(input('Qual letra:')).lower().strip()

        if chute in palavra_secreta_jogador2:
            indice = 0
            for letra in palavra_secreta_jogador2:
                if chute == letra:
                    letras_acertadas_jogador2[indice] = letra
                indice += 1
            print(letras_acertadas_jogador2)

        else:
            erros_jogador2 += 1
            print('Ops, você errou! Faltam {} tentativas'.format(len(palavra_secreta_jogador2) - erros_jogador2))
            desenha_forca(erros_jogador2)

            print('Vez do jogador 1:')
            p2jogando = False
            p1jogando = True

        enforcou_jogador2 = erros_jogador2 == len(palavra_secreta_jogador2)
        acertou_jogador2 = '_' not in letras_acertadas_jogador2

        if acertou_jogador2:
            print('Você ganhou jogador2, parabéns!')
            print('***FIM DO JOGO***')
            break

        elif enforcou_jogador2:
            print('Poxa vida, você perdeu!')