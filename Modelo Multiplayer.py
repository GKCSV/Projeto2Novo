palavra_secreta_jogador1 = 'abacate'
palavra_secreta_jogador2 = 'morango'
letras_acertadas_jogador1 = ['_' for letra in palavra_secreta_jogador1]
letras_acertadas_jogador2 = ['_' for letra in palavra_secreta_jogador2]

jogando = True
while jogando:
    enforcou = False
    acertou = False
    letras_jogador1 = []
    while not acertou and not enforcou:
            p1jogando = True
            p2jogando = False
            while p1jogando:
             chute = str(input('Qual letra:')).lower().strip()[0]
             if chute in palavra_secreta_jogador1:
                    for indice, letra in enumerate(palavra_secreta_jogador1):
                        if chute == letra:
                            letras_acertadas_jogador1[indice] = letra
                    print(letras_acertadas_jogador1)
             else:
                    print('Vez do jogador 2:')
                    p1jogando = False
                    p2jogando = True

            while p2jogando:
             chute = str(input('Qual letra:')).lower().strip()[0]
             if chute in palavra_secreta_jogador2:
                    for indice, letra in enumerate(palavra_secreta_jogador2):
                        if chute == letra:
                            letras_acertadas_jogador2[indice] = letra
                    print(palavra_secreta_jogador2)
                    print(letras_acertadas_jogador2)

             else:
                    print('Vez do jogador 1:')
                    p2jogando = False
                    p1jogando = True


if acertou:
        print('Você ganhou!')

else:
        print('Você perdeu!')