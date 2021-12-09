palavra_secreta_jogador1 = 'abacate'
palavra_secreta_jogador2 = 'morango'

letras_acertadas_jogador1 = ['_' for letra in palavra_secreta_jogador1]
letras_acertadas_jogador2 = ['_' for letra in palavra_secreta_jogador2]

lista_erros_jogador1 = []
lista_erros_jogador2 = []



def imprimir_msg_abertura():
    print('*****************************************')
    print('****** Bem-vindo ao jogo da Forca *******')
    print('*****************************************')

    print('\nEste é um jogo para dois jogadores, chame seu adversário e que vença o melhor!')

    print('\nVocê começa jogador1')



def ganhou_jogador2():
    acertou_j2 = '_' not in letras_acertadas_jogador2

    if acertou_j2:
        print('Você ganhou jogador2, parabéns!')
        print('***FIM DO JOGO***')
        jogar_novamente()

def perdeu_jogador2():
    enforcou_j2 = len(lista_erros_jogador2) == len(palavra_secreta_jogador2)

    if enforcou_j2:
        print('Poxa vida, você perdeu jogador 2!')
        jogar_novamente()


def contador_lista_erros_jogador1(chute, lista_erros_jogador1):
    if chute not in palavra_secreta_jogador1:
        lista_erros_jogador1.append(chute)
        print(lista_erros_jogador1)
        print('Ops, você errou! Faltam {} tentativas'.format(len(palavra_secreta_jogador1) - len(lista_erros_jogador1)))
        desenha_forca_j1(len(lista_erros_jogador1))

        print('Vez do jogador 2:')
        p2jogando()



def contador_lista_erros_jogador2(chute, lista_erros_jogador2):
    if chute not in palavra_secreta_jogador2:
        lista_erros_jogador2.append(chute)
        while (len(lista_erros_jogador2) < len(palavra_secreta_jogador2)):
            print(lista_erros_jogador2)
            print('Ops, você errou! Faltam {} tentativas'.format(len(palavra_secreta_jogador2) - len(lista_erros_jogador2)))
            desenha_forca_j2(len(lista_erros_jogador2))

            print('Vez do jogador 1:')
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

    print(" |            ")
    print("_|___         ")



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

    print(" |            ")
    print("_|___         ")


def p1jogando():
    enforcou_jogador1 = False
    acertou_jogador1 = False

    while not acertou_jogador1 and not enforcou_jogador1:
        p1jogando = True

        while p1jogando:
            print(palavra_secreta_jogador1)
            chute = str(input('Qual letra:')).lower().strip()
            if chute in palavra_secreta_jogador1:
                indice = 0
                for letra in palavra_secreta_jogador1:
                    if chute == letra:
                        letras_acertadas_jogador1[indice] = letra
                    indice += 1
                print(letras_acertadas_jogador1)
            
            if (len(lista_erros_jogador1) == len(palavra_secreta_jogador1)):
                enforcou_jogador1 = True
                print('Poxa vida, você perdeu jogador 1!')
                jogar_novamente()
            
            if '_' not in letras_acertadas_jogador1:
                acertou_jogador1 = True
                print('Você ganhou jogador 1, parabéns!')
                print('***FIM DO JOGO***')
                jogar_novamente()

            else:
                contador_lista_erros_jogador1(chute, lista_erros_jogador1)
            
    p1jogando = False



def p2jogando():
    enforcou_jogador2 = False
    acertou_jogador2 = False

    while not acertou_jogador2 and not enforcou_jogador2:
        p2jogando = True

        while p2jogando:
            print(palavra_secreta_jogador2)
            chute = str(input('Qual letra:')).lower().strip()

            if chute in palavra_secreta_jogador2:
                indice = 0
                for letra in palavra_secreta_jogador2:
                    if chute == letra:
                        letras_acertadas_jogador2[indice] = letra
                    indice += 1
                print(letras_acertadas_jogador2)

            if (len(lista_erros_jogador2) == len(palavra_secreta_jogador2)):
                enforcou_jogador2 = True
                print('Poxa vida, você perdeu jogador 2!')
                jogar_novamente()
    
            if '_' not in letras_acertadas_jogador2:
                acertou_jogador2 = True
                print('Você ganhou jogador 2, parabéns!')
                print('***FIM DO JOGO***')
                jogar_novamente()

            else:
                contador_lista_erros_jogador2(chute, lista_erros_jogador2)

    p2jogando = False


def jogar_novamente():
    resposta_jogarnovamente = input('Deseja jogar novamente? [S/N]')
    if (resposta_jogarnovamente).upper() == 'S':
        #principal_forca_multiplayer
        print('carregar jogo...')
    
    elif (resposta_jogarnovamente).upper() == 'N':
        print('Até a próxima!')
        exit()
    
    else:
        print('Digite uma resposta válida!')
        jogar_novamente()
