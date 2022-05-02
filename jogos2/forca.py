import random

def jogar():

    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    print(letras_acertadas)
    enforcou = False
    acertou = False
    erros = 0

    while (not acertou and not enforcou):

        chute = pede_chute()

        if (chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            enforcou = erros == 6
            acertou = '_' not in letras_acertadas
            print(letras_acertadas)

    if (acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

def inicializa_letras_acertadas(palavra):
    return ['_' for letra in palavra]

def imprime_mensagem_abertura():
    print('*********************************')
    print('***Bem vindo ao jogo da Forca!***')
    print('*********************************')

def carrega_palavra_secreta():
    arquivo = open('palavras.txt','r')
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero].upper()

    return palavra_secreta

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    posicao = 0
    for letra in palavra_secreta:
        if (chute.upper() == letra.upper()):
            letras_acertadas[posicao] = letra
        posicao += 1

def pede_chute():
    chute = input('Qual a letra? ')
    chute = chute.strip().upper()
    return chute

def imprime_mensagem_vencedor():
    print('Parabéns, Você ganhou!!')
    print("       ___________       ")
    print("      '._==_==_=_.'      ")
    print("      ._\\:      /_.     ")
    print("     | (|:.     |) |     ")
    print("      '-|:.     |-'      ")
    print("        \\::.    /       ")
    print("         '::.  .'        ")
    print("           )  (          ")
    print("           '  '          ")
    print("         _'    '_        ")
    print("        '________'       ")

def imprime_mensagem_perdedor(palavra_secreta):
    print('Puxa, voce foi enforcado! ')
    print('A palavra era {}'.format(palavra_secreta))
    print("     ______________         ")
    print("   /                \       ")
    print("  /                  \      ")
    print("//                    \/\   ")
    print("\|     Xxxx    xxxX   | /   ")
    print(" |     xxxx    xxxx   |/    ")
    print(" |     xxx      xxx   |     ")
    print(" |                    |     ")
    print(" \__       xxx      __/     ")
    print("   |\      xxx     /|       ")
    print("   | |            | |       ")
    print("   | I I I II I I I |       ")
    print("   |   I I II I I   |       ")
    print("   \_              _/       ")
    print("     \_          _/         ")
    print("       \________/           ")

    print('Fim do jogo')


