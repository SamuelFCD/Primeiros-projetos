import random
import pygame as py
import os
from time import sleep
def tocar_musica_vitoria():
    py.init()
    # iniciando o pygame

    py.mixer.music.load('musica_forca.mp3')
    # 'chamando' a musica

    py.mixer.music.play(1)
    #quantasvezes e para rodas

    input()
    py.event.wait()
def tocar_musica_derrota():
    py.init()
    # iniciando o pygame

    py.mixer.music.load('musica_forca_derrota.mp3')
    # 'chamando' a musica

    py.mixer.music.play(100)
    # quantasvezes e para rodas

    input()
    py.event.wait()
def toque_da_vitoria():
    py.init()
    # iniciando o pygame

    py.mixer.music.load('musica_forca_plim.mp4')
    # 'chamando' a musica

    py.mixer.music.play(1)
    # quantasvezes e para rodas

    input()
    py.event.wait()

def nome_jogador():
    nome = input('\033[1mDigite o seu nome jogado 1 :').capitalize().strip()
    return nome
def banco_de_palavras_frutas():
    banco_de_palavras_frutas = {'Frutas': ['ABACAXI', 'BANANA', 'GOIABA', 'MAÇA']}
    return banco_de_palavras_frutas
def banco_de_palavras_carros():
    banco_de_palavras_carros = {'Carros': ['MACLAREN', 'MERCEDES', 'FERRARI', 'FIAT']}
    return banco_de_palavras_carros
def banco_de_palavras_paises():
    banco_de_palavras_paises = {'Paises': ['BRASIL', 'ARGENTINA', 'FRANÇA', 'INGLATERRA']}
    return banco_de_palavras_paises
def banco_de_palavras_dicas_frutas():
    banco_de_palavras_dicas_frutas = {'ABACAXI':'\033[1mDICA : E pontudo na parte de cima','BANANA': '\033[1mDICA : Ela e amarela.', 'GOIABA': '\033[1mDICA : Essa fruta e redonda e verde.','MAÇA':'\033[1mDICA : Ela e vermelha.'}
    return banco_de_palavras_dicas_frutas
def banco_de_palavras_dicas_carros():
    banco_de_palavras_dicas_carros = {'FERRARI': '\033[1mDICA : Essa marca Produz carros vermelhos muito famosos','MACLAREN':'\033[1mDICA : Essa marca,e uma das grandes campeas da historia da Formula 1','MERCEDES':'\033[1mDICA : E uma marca de carros Alemã','FIAT':'\033[1mDICA : Possui um carro muito mistico aqui no Brasil'}
    return banco_de_palavras_dicas_carros
def banco_de_palavras_dicas_paises():
    banco_de_palavras_dicas_paises = {'BRASIL':'\033[1mDICA : Pais muito vitorioso em copas do mundo','ARGENTINA':'\033[1mDICA : Pais com grande rivalidade com os brasileiros','FRANÇA':'\033[1mDICA : Dentro deste pais,tem uma Cidade/Estado chamado Mõnaco','INGLATERRA':'\033[1mDICA : nomeia pessoas com titulo de Sir(senhor)'}
    return banco_de_palavras_dicas_paises

def estatisticas_jogadores(nome, pontos, erros, vida): #funçao de estatisticas do jogador
    banco_jogador1 = {'NOME': [nome], 'Pontuação': [pontos], 'ERROS': [erros], 'VIDA': [vida]}
    return banco_jogador1
def palavra_secreta_tema_fruta():
    frutas = banco_de_palavras_frutas()
    #dicas = banco_de_palavras_dicas_frutas()
    palavras_secreta = random.choice(frutas['Frutas'])
    return palavras_secreta
def dicas_tema_frutas(palavras_secreta):
    dicas = banco_de_palavras_dicas_frutas()
    if palavras_secreta == 'ABACAXI':
        print(dicas['ABACAXI'])
    if palavras_secreta == 'GOIABA':
        print(dicas['GOIABA'])
    if palavras_secreta == 'BANANA':
        print(dicas['BANANA'])
    if palavras_secreta == 'MAÇA':
        print(dicas['MAÇA'])
def palavra_secreta_tema_carros():
    carros = banco_de_palavras_carros()
    palavras_secreta = random.choice(carros['Carros'])
    return palavras_secreta
def dicas_tema_carros(palavras_secreta):
    dicas = banco_de_palavras_dicas_carros()
    if palavras_secreta == 'MACLAREN':
        print(dicas['MACLAREN'])
    if palavras_secreta == 'MERCEDES':
        print(dicas['MERCEDES'])
    if palavras_secreta == 'FERRARI':
        print(dicas['FERRARI'])
    if palavras_secreta == 'FIAT':
        print(dicas['FIAT'])
def palavra_secreta_tema_paises():
    paises = banco_de_palavras_paises()
    palavras_secreta = random.choice(paises['Paises'])
    return palavras_secreta

def dicas_tema_paises(palavras_secreta):
    dicas = banco_de_palavras_dicas_paises()
    if palavras_secreta == 'INGLATERRA':
        print(dicas['INGLATERRA'])
    if palavras_secreta == 'BRASIL':
        print(dicas['BRASIL'])
    if palavras_secreta == 'FRANÇA':
        print(dicas['FRANÇA'])
    if palavras_secreta == 'ARGENTINA':
        print(dicas['ARGENTINA'])

def mostrar_dica(escolha,palavra):
    if escolha == 'FRUTAS':
        print('\033[1;36m-=-\033[m' * 10)
        dicas_tema_frutas(palavra)
    if escolha == 'CARROS':
        print('\033[1;36m-=-\033[m' * 10)
        dicas_tema_carros(palavra)
    if escolha == 'PAISES':
        print('\033[1;36m-=-\033[m' * 10)
        dicas_tema_paises(palavra)

def mostrar_trofeu():
    print("\033[1;33m       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
def mostrar_caveira():


     print(    "\033[1;31m    _______________         ")
     print(    "   /               \       ")
     print(    "  /                 \      ")
     print(   "/\/                   \/\  ")
     print(   "\ |  XXXX     XXXX   | /   ")
     print(   " \|  XXXX     XXXX   |/     ")
     print(    " |   XXX       XXX   |      ")
     print(    " |                   |      ")
     print(    " \__      XXX      __/     ")
     print(    "   |\     XXX     /|       ")
     print(    "   | |           | |        ")
     print(    "   | I I I I I I I |        ")
     print(    "   |  I I I I I I  |        ")
     print(    "   \_             _/       ")
     print(    "     \_         _/         ")
     print(    "       \_______/           ")


def forca_vazia():
    print('     _________')
    print('     |       |')
    print('             |')
    print('             |')
    print('             |')
    print('             |')
    print('             |')
def forca_cabeça():
    print('     _________')
    print('     |       |')
    print('     O       |')
    print('             |')
    print('             |')
    print('             |')
    print('             |')
def forca_cabeça_tronco():
    print('     _________')
    print('     |       |')
    print('     O       |')
    print('     |       |')
    print('             |')
    print('             |')
    print('             |')
def forca_cabeça_tronco_braço_esquerdo():
    print('     _________')
    print('     |       |')
    print('     O       |')
    print('     |\      |')
    print('             |')
    print('             |')
    print('             |')
def forca_cabeça_tronco_braços_():
    print('     _________')
    print('     |       |')
    print('     O       |')
    print('    /|\      |')
    print('             |')
    print('             |')
    print('             |')
def forca_cabeça_tronco_braços_perna_esquerda():
    print('     _________')
    print('     |       |')
    print('     O       |')
    print('    /|\      |')
    print('      \      |')
    print('             |')
    print('             |')
def forca_cabeça_tronco_braços_pernas():
    print('     _________')
    print('     |       |')
    print('     O       |')
    print('    /|\      |')
    print('    / \      |')
    print('             |')
    print('             |')
def mostrar_boneco_facil_j1(vida):
    if vida == 13 or vida == 12 or vida == 11:
        forca_vazia()
    if vida == 10 or vida == 9:
        forca_cabeça()
    if vida == 8 or vida == 7:
        forca_cabeça_tronco()
    if vida == 6 or vida == 5:
        forca_cabeça_tronco_braço_esquerdo()
    if vida == 4 or vida == 3:
        forca_cabeça_tronco_braços_()
    if vida == 2 or vida == 1:
        forca_cabeça_tronco_braços_perna_esquerda()
    if vida == 0:
        forca_cabeça_tronco_braços_pernas()
def mostrar_boneco_medio_j1(vida):
    if vida == 11 or vida == 10 or vida == 9:
        forca_vazia()
    if vida == 8 or vida == 7:
        forca_cabeça()
    if vida == 6 or vida == 5:
        forca_cabeça_tronco()
    if vida == 4 :
        forca_cabeça_tronco_braço_esquerdo()
    if vida == 3:
        forca_cabeça_tronco_braços_()
    if vida == 2 :
        forca_cabeça_tronco_braços_perna_esquerda()
    if vida == 1:
        forca_cabeça_tronco_braços_pernas()
    if vida == 0:
        forca_cabeça_tronco_braços_pernas()


def mostrar_boneco_dificl_j1(vida):
    if vida == 7 or vida == 6:
        forca_vazia()
    if vida == 5 or vida == 4 :
        forca_cabeça_tronco()
    if vida == 3 or  vida == 2 or vida == 1:
        forca_cabeça_tronco_braços_()
    if vida == 0:
        forca_cabeça_tronco_braços_pernas()
def acertou_modo_solo(acertou,nome,pontos,vida,erros,letras_acertadas,palavra):
    acertou = '_' not in letras_acertadas
    if acertou == True:

        print(f'Paraben,voce ganhou {nome}')
        print(estatisticas_jogadores(nome, pontos, erros, vida))
        print('\033[33')
        mostrar_trofeu()
        tocar_musica_vitoria()

    if vida == 0:
        print('Você perdeu {}'.format(nome))
        print('A palavra secreta era :',palavra)
        print(estatisticas_jogadores(nome, pontos, erros, vida))
        mostrar_caveira()
        # tocar_musica_derrota()
def acertou_modo_multiplayer(acertou1,acertou2,nome1,nome2,pontos1,pontos2,vida1,vida2,erros1,erros2,letras_acertadas1,letras_acertadas2):
    if acertou1 == True and letras_acertadas1 == letras_acertadas2:
        print('parece que os dois ganharam ein,empate.')
        print(estatisticas_jogadores(nome1, pontos1, erros1, vida1))
        print(estatisticas_jogadores(nome2, pontos2, erros2, vida2))
    elif acertou2 == True and letras_acertadas2 == letras_acertadas1:
        print('parece que os dois ganharam ein,empate.')
        print(estatisticas_jogadores(nome1, pontos1, erros1, vida1))
        print(estatisticas_jogadores(nome2, pontos2, erros2, vida2))
    elif acertou1 == True:
        print('Você ganhou {}!'.format(nome1))
        print(estatisticas_jogadores(nome1, pontos1, erros1, vida1))
        print(estatisticas_jogadores(nome2, pontos2, erros1, vida2))
        mostrar_trofeu()
        tocar_musica_vitoria()
    elif acertou2 == True:
        print('Você ganhou {}!'.format(nome2))
        print(estatisticas_jogadores(nome2, pontos2, erros2, vida2))
        print(estatisticas_jogadores(nome1, pontos1, erros1, vida1))
        mostrar_trofeu()
        tocar_musica_vitoria()


    elif vida1 == 0 and vida2 == 0:
        print('parece que ouve um empate ein,os dois morreram')
        print(estatisticas_jogadores(nome1, pontos1, erros1, vida1))
        print(estatisticas_jogadores(nome2, pontos2, erros2, vida2))
        mostrar_caveira()


    elif vida1 == 0:
        print('Você perdeu {},{} ganhou!'.format(nome2, nome1))
        print(estatisticas_jogadores(nome1, pontos1, erros1, vida1))
        print(estatisticas_jogadores(nome2, pontos2, erros2, vida2))
        mostrar_trofeu()
        tocar_musica_vitoria()
    elif vida2 == 0:
        print('Você perdeu {},{} ganhou!'.format(nome1, nome2))
        print(estatisticas_jogadores(nome2, pontos2, erros2, vida2))
        print(estatisticas_jogadores(nome1, pontos1, erros1, vida1))
        mostrar_trofeu()
        tocar_musica_vitoria()
def vida_modo_facil_j1():
    vida_jogador_1 = 12
    return vida_jogador_1
def pontos_modo_facil_j1():
        pontos_jogador_1 = 0
        return pontos_jogador_1


def jogar_facil(): #funçao do modo facil
    acertou1 = False
    print('\033[1;36m-=-\033[m' * 20)
    print('\033[1mAqui nesse modo,o seu boneco tem 12 vidas,cada erro e -1 de vida\nVocê começara com 0 PTS,cada acerto e +20 PTS\nCada erro e -5 PTS.')
    print('\033[1;36m-=-\033[m' * 20)
    vida_j1 = vida_modo_facil_j1()
    pontos_j1 = pontos_modo_facil_j1()
    nome1 = nome_jogador()
    escolha = input('\033[1mescolha um tema; Frutas,carros ou paises : ').upper()
    os.system('cls')
    if escolha == 'FRUTAS':
        palavra_j1 = palavra_secreta_tema_fruta()
        print('\033[1;36m-=-\033[m' * 10)
        dicas_tema_frutas(palavra_j1)
    if escolha == 'CARROS':
        palavra_j1 = palavra_secreta_tema_carros()
        print('\033[1;36m-=-\033[m' * 10)
        dicas_tema_carros(palavra_j1)
    if escolha == 'PAISES':
        palavra_j1 = palavra_secreta_tema_paises()
        print('\033[1;36m-=-\033[m' * 10)
        dicas_tema_paises(palavra_j1)
    letras_acertadas = []
    letras_chute = []
    for x in palavra_j1:
        letras_acertadas.append('_')
    erros_j1 = 0

    while vida_j1 != 0 and not acertou1:
        tentativa_jogador_1 = input('\033[1mQual letra {},voce tambem pode tentar chutar a palavra de uma so vez! ?'.format(nome1)).upper()
        letras_chute.append(tentativa_jogador_1)
        os.system('cls')
        if tentativa_jogador_1 == palavra_j1.upper():
            os.system('cls')
            pontos_j1 += 100
            print('\033[1mVocê ganhou {}!!\nConseguiu um bonus de 100 PTS!'.format(nome1))
            print(estatisticas_jogadores(nome1, pontos_j1, erros_j1, vida_j1))
            mostrar_trofeu()
            tocar_musica_vitoria()
            break
        if tentativa_jogador_1.upper() in palavra_j1:
            #toque_da_vitoria()
            posicao_1 = 0
            pontos_j1 = pontos_j1 + 20
            print('\033[1;36m-=-\033[m' * 10)
            print('\033[1mparece que voce acertou ein,tem a letra {} na palavra!\n+{} PTS'.format(tentativa_jogador_1,20))
            print('\033[1;36m-=-\033[m' * 10)
            for letra in palavra_j1:
                if tentativa_jogador_1.upper() == letra.upper():
                    letras_acertadas[posicao_1] = letra
                posicao_1 = posicao_1 + 1
        else:
            print('\033[1;36m-=-\033[m' * 10)
            print('\033[1mparece que voce errou!nao tem a letra {} na pa palavra!\n-{} PTS,o seu bonequinho perdera parte do corpo!'.format(
                    tentativa_jogador_1, 5))
            vida_j1 -= 1
            erros_j1 += 1
            pontos_j1 = pontos_j1 - 5
        if tentativa_jogador_1 == palavra_j1[0]:
            vida_j1 = vida_j1 + 1
            print(f'\033[1mParabens {nome1},ganhou 1 vida extra por acertar a primeira letra da palavra secreta!')
            sleep(5)
        os.system("cls")
        print('\033[36m-=-\033[m' * 10)
        print('\033[1mLetras chutadas :',letras_chute)
        print('\033[1mLetras acertadas :',letras_acertadas)
        mostrar_dica(escolha, palavra_j1)
        print('\033[1mForca :')
        mostrar_boneco_facil_j1(vida_j1)
        acertou_modo_solo(acertou1, nome1, pontos_j1, vida_j1, erros_j1, letras_acertadas,palavra_j1)

def vida_modo_medio_j1():
    vida_jogador_1 = 10
    return vida_jogador_1
def pontos_modo_medio_j1():
    pontos_jogador_1 = 0
    return pontos_jogador_1

def jogar_medio(): #funçao do modo facil
    acertou1 = False
    print('\033[1;36m-=-\033[m' * 20)
    print('\033[1mAqui nesse modo,o seu boneco tem 10 vidas,cada erro e -2 de vida\nPorem,se atingir 4 de vida,começara a perder apenas 1 de vida\nVocê começara com 0 PTS,cada acerto e +50 PTS\nCada erro e -10 PTS.')
    print('\033[1;36m-=-\033[m' * 20)
    vida_j1 = vida_modo_medio_j1()
    pontos_j1 = pontos_modo_medio_j1()
    nome1 = nome_jogador()
    escolha = input('\033[1mescolha um tema; Frutas,carros ou paises : ').upper()
    os.system('cls')
    if escolha == 'FRUTAS':
        palavra_j1 = palavra_secreta_tema_fruta()
        print('\033[1;36m-=-\033[m' * 10)
        dicas_tema_frutas(palavra_j1)
    if escolha == 'CARROS':
        palavra_j1 = palavra_secreta_tema_carros()
        print('\033[1;36m-=-\033[m' * 10)
        dicas_tema_carros(palavra_j1)
    if escolha == 'PAISES':
        palavra_j1 = palavra_secreta_tema_paises()
        print('\033[1;36m-=-\033[m' * 10)
        dicas_tema_paises(palavra_j1)
    letras_acertadas = []
    letras_chute = []
    for x in palavra_j1:
        letras_acertadas.append('_')
    erros_j1 = 0

    while vida_j1 != 0 and not acertou1:
        tentativa_jogador_1 = input('\033[1mQual letra {},voce tabem pode tentar chutar a palavra de uma so vez! ?'.format(nome1)).upper()
        letras_chute.append(tentativa_jogador_1)
        os.system('cls')
        if tentativa_jogador_1 == palavra_j1.upper():
            os.system('cls')
            pontos_j1 += 100
            print('\033[1mVocê ganhou {}!!\nConseguiu um bonus de 100 PTS!'.format(nome1))
            print(estatisticas_jogadores(nome1, pontos_j1, erros_j1, vida_j1))
            mostrar_trofeu()
            tocar_musica_vitoria()
            break
        if tentativa_jogador_1.upper() in palavra_j1:
            # toque_da_vitoria()
            posicao_1 = 0
            pontos_j1 = pontos_j1 + 50
            print('\033[1;36m-=-\033[m' * 10)
            print('\033[1mparece que voce acertou ein,tem a letra {} na palavra!\n+{} PTS'.format(tentativa_jogador_1, 20))
            print('\033[1;36m-=-\033[m' * 10)
            for letra in palavra_j1:
                if tentativa_jogador_1.upper() == letra.upper():
                    letras_acertadas[posicao_1] = letra
                posicao_1 = posicao_1 + 1
        else:
            print('\033[1;36m-=-\033[m' * 10)
            print('\033[1mparece que voce errou!nao tem a letra {} na pa palavra!\n-{} PTS,o seu bonequinho perdera parte do corpo!'.format(
                    tentativa_jogador_1, 5))
            vida_j1 -= 1
            erros_j1 += 1
            pontos_j1 = pontos_j1 - 10
        if tentativa_jogador_1 == palavra_j1[0]:
            vida_j1 = vida_j1 + 1
            print('\033[1;36m-=-\033[m' * 10)
            print(f'\033[1mParabens {nome1},ganhou 1 vida extra por acertar a primeira letra da palavra secreta!')
            sleep(5)
        os.system("cls")
        print('\033[1;36m-=-\033[m' * 10)
        print('\033[1mLetras chutadas :', letras_chute)
        print('\033[1mLetras acertadas :', letras_acertadas)
        mostrar_dica(escolha, palavra_j1)
        print('\033[1mForca :')
        mostrar_boneco_facil_j1(vida_j1)
        acertou_modo_solo(acertou1, nome1, pontos_j1, vida_j1, erros_j1, letras_acertadas,palavra_j1)
def vida_modo_dificil_j1():
    vida_jogador_1 = 6
    return vida_jogador_1
def pontos_modo_dificil_j1():
    pontos_jogador_1 = 0
    return pontos_jogador_1

def jogar_dificl(): #funçao do modo facil
    acertou1 = False
    print('\033[1;36m-=-\033[m' * 20)
    print('\033[1mAqui nesse modo,o seu boneco tem 6 vidas,cada erro -2 de vida\nVocê começara com 0 PTS,cada acerto e +100 PTS\nCada erro e -20 PTS.')
    print('\033[1;36m-=-\033[m' * 20)
    vida_j1 = vida_modo_dificil_j1()
    pontos_j1 = pontos_modo_dificil_j1()
    nome1 = nome_jogador()
    escolha = input('\033[1mescolha um tema; Frutas,carros ou paises : ').upper()
    os.system('cls')
    if escolha == 'FRUTAS':
        palavra_j1 = palavra_secreta_tema_fruta()
        print('\033[1;36m-=-\033[m' * 10)
        dicas_tema_frutas(palavra_j1)
    if escolha == 'CARROS':
        palavra_j1 = palavra_secreta_tema_carros()
        print('\033[1;36m-=-\033[m' * 10)
        dicas_tema_carros(palavra_j1)
    if escolha == 'PAISES':
        palavra_j1 = palavra_secreta_tema_paises()
        print('\033[1;36m-=-\033[m' * 10)
        dicas_tema_paises(palavra_j1)
    letras_acertadas = []
    letras_chute = []
    for x in palavra_j1:
        letras_acertadas.append('_')
    erros_j1 = 0

    while vida_j1 != 0 and not acertou1:
        tentativa_jogador_1 = input('\033[1mQual letra {},voce tabem pode tentar chutar a palavra de uma so vez! ?'.format(nome1)).upper()
        letras_chute.append(tentativa_jogador_1)
        os.system('cls')
        if tentativa_jogador_1 == palavra_j1.upper():
            os.system('cls')
            pontos_j1 += 100
            print('\033[1mVocê ganhou {}!!\nConseguiu um bonus de 100 PTS!'.format(nome1))
            print(estatisticas_jogadores(nome1, pontos_j1, erros_j1, vida_j1))
            mostrar_trofeu()
            tocar_musica_vitoria()
            break
        if tentativa_jogador_1.upper() in palavra_j1:
            # toque_da_vitoria()
            posicao_1 = 0
            pontos_j1 = pontos_j1 + 100
            print('\033[1;36m-=-\033[m' * 10)
            print('parece que voce acertou ein,tem a letra {} na palavra!\n+{} PTS'.format(tentativa_jogador_1, 20))
            print('\033[1;36m-=-\033[m' * 10)
            for letra in palavra_j1:
                if tentativa_jogador_1.upper() == letra.upper():
                    letras_acertadas[posicao_1] = letra
                posicao_1 = posicao_1 + 1
        else:
            print('\033[1;36m-=-\033[m' * 10)
            print('\033[1mparece que voce errou!nao tem a letra {} na pa palavra!\n-{} PTS,o seu bonequinho perdera parte do corpo!'.format(
                    tentativa_jogador_1, 5))
            vida_j1 -= 2
            erros_j1 += 1
            pontos_j1 = pontos_j1 - 20
        if tentativa_jogador_1 == palavra_j1[0]:
            vida_j1 = vida_j1 + 1
            print('\033[1;36m-=-\033[m' * 10)
            print(f'\033[1mParabens {nome1},ganhou 1 vida extra por acertar a primeira letra da palavra secreta!')
            sleep(5)
        os.system("cls")
        print('\033[1;36m-=-\033[m' * 10)
        print('\033[1mLetras chutadas :', letras_chute)
        print('\033[1mLetras acertadas :', letras_acertadas)
        mostrar_dica(escolha, palavra_j1)
        print('\033[1mForca :')
        mostrar_boneco_dificl_j1(vida_j1)
        acertou_modo_solo(acertou1, nome1, pontos_j1, vida_j1, erros_j1, letras_acertadas,palavra_j1)
#jogador 2
def nome_jogador2():
    nome2 = input('\033[1mDigite o nome do jogador 2 : ').capitalize().strip()
    return nome2
def vida_modo_facil_j2():
    vida_jogador_2 = 12
    return vida_jogador_2
def pontos_modo_facil_j2():
        pontos_jogador_2 = 0
        return pontos_jogador_2
def jogar_facil_multiplayer(): #funçao do modo facil
    acertou1 = False
    acertou2 = False
    print('\033[1;36m-=-\033[m' * 20)
    print('\033[1mAqui nesse modo,oo seus bonecos tem 12 vidas,os seus bonecos perderão 1 parte a cada -2 vidas\nCada um começara com 0 PTS,cada acerto e +20 PTS\nCada erro e -5 PTS.\nOBS: a dica sera introduzida no começo do jogo apenas(aumentando a dificuldade)\nOBS 2 :se por acaso o jogador 1,digitar a palavra completa,ele ganhara automaticamente.')
    print('\033[1;36m-=-\033[m' * 20)
    os.system('cls')
    pontos_j1 = pontos_modo_facil_j1()
    vida_j1 = vida_modo_facil_j1()
    nome1 = nome_jogador()
    pontos_j2 = pontos_modo_facil_j2()
    vida_j2 = vida_modo_facil_j2()
    nome2 = nome_jogador2()
    escolha = input('\033[1mescolha um tema; Frutas,carros ou paises : ').upper()
    os.system('cls')
    if escolha == 'FRUTAS':
        palavra_j1 = palavra_secreta_tema_fruta()
        palavra_j2 = palavra_j1
        print('\033[1;36m-=-\033[m' * 10)
        dicas_tema_frutas(palavra_j1)
        print('\033[1m10 seg. para os jogadores memorizarem...')
        sleep(10)
        os.system('cls')
    if escolha == 'CARROS':
        palavra_j1 = palavra_secreta_tema_carros()
        palavra_j2 = palavra_j1
        print('\033[1;36m-=-\033[m' * 10)
        dicas_tema_carros(palavra_j1)
        print('\033[1m10 seg. para os jogadores memorizarem...')
        sleep(10)
        os.system('cls')
    if escolha == 'PAISES':
        palavra_j1 = palavra_secreta_tema_paises()
        palavra_j2 = palavra_j1
        print('\033[1;36m-=-\033[m' * 10)
        dicas_tema_paises(palavra_j1)
        print('\033[1m10 seg. para os jogadores memorizarem...')
        sleep(10)
        os.system('cls')
    letras_acertadas_j1 = []
    letras_acertadas_j2 = []
    letras_chutadas_j1 = []
    letras_chutadas_j2 = []
    for x in palavra_j1:
        letras_acertadas_j1.append('_')
    for x in palavra_j2:
        letras_acertadas_j2.append('_')

    erros_j1 = 0
    erros_j2 = 0
    while vida_j1!= 0 and not acertou1 and vida_j2 != 0 and not acertou2:
        tentativa_jogador_1 = input('\033[1mQual letra {},voce tabem pode tentar chutar a palavra de uma so vez! ?'.format(nome1)).upper()
        letras_chutadas_j1.append(tentativa_jogador_1)
        if tentativa_jogador_1 == palavra_j1.upper():
            os.system('cls')
            pontos_j1 += 100
            print('\033[1mVocê ganhou {}!!\nConseguiu um bonus de 100 PTS!\nSobrou {} vidas!'.format(nome1, vida_j1))
            print(estatisticas_jogadores(nome1, pontos_j1,erros_j1, vida_j1))
            print(estatisticas_jogadores(nome2, pontos_j2, erros_j2, vida_j2))
            mostrar_trofeu()
            tocar_musica_vitoria()
            break
        if tentativa_jogador_1.upper() in palavra_j1:
            #toque_da_vitoria()
            posicao_1 = 0
            pontos_j1 = pontos_j1 + 20

            for letra in palavra_j1:
                if tentativa_jogador_1.upper() == letra.upper():
                    letras_acertadas_j1[posicao_1] = letra
                posicao_1 = posicao_1 + 1
        else:
            vida_j1 -= 1
            erros_j1 += 1
            pontos_j1 = pontos_j1 - 5
        if tentativa_jogador_1 == palavra_j1[0]:
            vida_j1 = vida_j1 + 1
            print(f'\033[1mParabens {nome1},ganhou 1 vida extra por acertar a primeira letra da palavra secreta!')
        print('\033[1mvoce esta assim no momento {} : {}'.format(nome1, letras_acertadas_j1))
        print('\033[1mLetras chutadas :', letras_chutadas_j1, '\nForca :')
        mostrar_boneco_facil_j1(vida_j1)
        print('\033[1mprepare-se jogador 2,agora e sua vez...')
        sleep(5)
        os.system('cls')
        tentativa_jogador_2 = input('\033[1mQual letra {},voce tabem pode tentar chutar a palavra de uma so vez! ?'.format(nome2)).upper()
        letras_chutadas_j2.append(tentativa_jogador_2)
        if tentativa_jogador_2 == palavra_j2.upper():
            os.system('cls')
            pontos_j2 += 100
            print('\033[1mVocê ganhou {}!!\nConseguiu um bonus de 100 PTS!'.format(nome2, pontos_j2, vida_j2))
            print(estatisticas_jogadores(nome2, pontos_j2, erros_j2, vida_j2))
            print(estatisticas_jogadores(nome1, pontos_j1, erros_j1, vida_j1))
            mostrar_trofeu()
            tocar_musica_vitoria()
            break
        if tentativa_jogador_2.upper() in palavra_j2:
            # toque_da_vitoria()
            posicao_2 = 0
            pontos_j2 = pontos_j2 + 20
            for letra in palavra_j2:
                if tentativa_jogador_2.upper() == letra.upper():
                    letras_acertadas_j2[posicao_2] = letra
                posicao_2 = posicao_2 + 1
        else:
            vida_j2 -= 1
            erros_j2 += 1
            pontos_j2 = pontos_j2 - 5
        if tentativa_jogador_2 == palavra_j2[0]:
            vida_j2 = vida_j2 + 1
            print('\033[1;36m-=-\033[m' * 10)
            print(f'\033[1mParabens {nome2},ganhou 1 vida extra por acertar a primeira letra da palavra secreta!')
        print('\033[1mvoce esta assim no momento {} : {}'.format(nome2, letras_acertadas_j2))
        print('\033[1mLetras chutadas :', letras_chutadas_j2, '\nForca :')
        mostrar_boneco_facil_j1(vida_j2)
        print('\033[1mprepare-se jogador 1,agora e sua vez...')
        sleep(5)
        os.system('cls')
        acertou1 = '_' not in letras_acertadas_j1
        acertou2 = '_' not in letras_acertadas_j2
        acertou_modo_multiplayer(acertou1, acertou2,nome1, nome2, pontos_j1, pontos_j2,vida_j1, vida_j2,erros_j1, erros_j2,letras_acertadas_j1, letras_acertadas_j2)



def vida_modo_medio_j2():
    vida_jogador_2 = 10
    return vida_jogador_2
def pontos_modo_medio_j2():
    pontos_jogador_2 = 0
    return pontos_jogador_2

def jogar_medio_multiplayer(): #funçao do modo facil
    acertou1 = False
    acertou2 = False
    print('\033[1;36m-=-\033[m' * 20)
    print('\033[1mAqui nesse modo,oo seus bonecos tem 10 vidas,os seus bonecos perderão 1 parte a cada -2 vidas\nPorem,se a vida chegar a 4,começara a perder -2 vidas\nCada um começara com 0 PTS,cada acerto e +50 PTS\nCada erro e -10 PTS.OBS: a dica sera introduzida no começo do jogo apenas(aumentando a dificuldade)\nOBS 2 :se por acaso o jogador 1,digitar a palavra completa,ele ganhara automaticamente.')
    print('\033[1;36m-=-\033[m' * 20)
    pontos_j1 = pontos_modo_medio_j1()
    vida_j1 = vida_modo_medio_j1()
    nome1 = nome_jogador()
    pontos_j2 = pontos_modo_medio_j2()
    vida_j2 = vida_modo_medio_j2()
    nome2 = nome_jogador2()
    escolha = input('\033[1mEscolha um tema; Frutas,carros ou paises : ').upper()
    os.system('cls')
    if escolha == 'FRUTAS':
        palavra_j1 = palavra_secreta_tema_fruta()
        palavra_j2 = palavra_j1
        print('\033[1;36m-=-\033[m' * 10)
        dicas_tema_frutas(palavra_j1)
        print('\033[1m10 seg. para os jogadores memorizarem...')
        sleep(10)
        os.system('cls')
    if escolha == 'CARROS':
        palavra_j1 = palavra_secreta_tema_carros()
        palavra_j2 = palavra_j1
        print('\033[1;36m-=-\033[m' * 10)
        dicas_tema_carros(palavra_j1)
        print('\033[1m10 seg. para os jogadores memorizarem...')
        sleep(10)
        os.system('cls')
    if escolha == 'PAISES':
        palavra_j1 = palavra_secreta_tema_paises()
        palavra_j2 = palavra_j1
        print('\033[1;36m-=-\033[m' * 10)
        dicas_tema_paises(palavra_j1)
        print('\033[1m10 seg. para os jogadores memorizarem...')
        sleep(10)
        os.system('cls')
    letras_acertadas_j1 = []
    letras_acertadas_j2 = []
    letras_chutadas_j1 = []
    letras_chutadas_j2 = []
    for x in palavra_j1:
        letras_acertadas_j1.append('_')
    for x in palavra_j2:
        letras_acertadas_j2.append('_')

    erros_j1 = 0
    erros_j2 = 0
    while vida_j1 != 0 and not acertou1 and vida_j2 != 0 and not acertou2:
        tentativa_jogador_1 = input('\033[1mQual letra {},voce tabem pode tentar chutar a palavra de uma so vez! ?'.format(nome1)).upper()
        letras_chutadas_j1.append(tentativa_jogador_1)
        os.system('cls')
        if tentativa_jogador_1 == palavra_j1.upper():
            os.system('cls')
            pontos_j1 += 100
            print('\033[1mVocê ganhou {}!!\nConseguiu um bonus de 100 PTS!'.format(nome1, vida_j1))
            print(estatisticas_jogadores(nome1, pontos_j1, erros_j1, vida_j1))
            print(estatisticas_jogadores(nome2, pontos_j2, erros_j2, vida_j2))
            mostrar_trofeu()
            tocar_musica_vitoria()
            break
        if tentativa_jogador_1.upper() in palavra_j1:
            # toque_da_vitoria()
            posicao_1 = 0
            pontos_j1 = pontos_j1 + 50

            for letra in palavra_j1:
                if tentativa_jogador_1.upper() == letra.upper():
                    letras_acertadas_j1[posicao_1] = letra
                posicao_1 = posicao_1 + 1
        else:
            vida_j1 -= 1
            erros_j1 += 1
            pontos_j1 = pontos_j1 - 10
        if tentativa_jogador_1 == palavra_j1[0]:
            vida_j1 = vida_j1 + 1
            print(f'\033[1mParabens {nome1},ganhou 1 vida extra por acertar a primeira letra da palavra secreta!')
        print('\033[1mvoce esta assim no momento {} : {}'.format(nome1, letras_acertadas_j1))
        print('\033[1mLetras chutadas :', letras_chutadas_j1, '\nForca :')
        mostrar_boneco_medio_j1(vida_j1)
        print('\033[1mprepare-se jogador 2,agora e sua vez...')
        sleep(5)
        os.system('cls')
        tentativa_jogador_2 = input('\033[1mQual letra {},voce tabem pode tentar chutar a palavra de uma so vez! ?'.format(nome2)).upper()
        letras_chutadas_j2.append(tentativa_jogador_2)
        if tentativa_jogador_2 == palavra_j2.upper():
            pontos_j2 += 100
            print('\033[1mVocê ganhou {}!!\nConseguiu um bonus de 100 PTS!'.format(nome2, pontos_j2, vida_j2))
            print(estatisticas_jogadores(nome2, pontos_j2, erros_j2, vida_j2))
            print(estatisticas_jogadores(nome1, pontos_j1, erros_j1, vida_j1))
            mostrar_trofeu()
            tocar_musica_vitoria()
            break
        if tentativa_jogador_2.upper() in palavra_j2:
            # toque_da_vitoria()
            posicao_2 = 0
            pontos_j2 = pontos_j2 + 50
            for letra in palavra_j2:
                if tentativa_jogador_2.upper() == letra.upper():
                    letras_acertadas_j2[posicao_2] = letra
                posicao_2 = posicao_2 + 1
        else:
            vida_j2 -= 1
            erros_j2 += 1
            pontos_j2 = pontos_j2 - 10
        if tentativa_jogador_2 == palavra_j2[0]:
            vida_j2 = vida_j2 + 1
            print(f'\033[1mParabens {nome2},ganhou 1 vida extra por acertar a primeira letra da palavra secreta!')
        print('voce esta assim no momento {} : {}'.format(nome2, letras_acertadas_j2))
        print('Letras chutadas :', letras_chutadas_j2, '\nForca :')
        mostrar_boneco_medio_j1(vida_j2)
        print('prepare-se jogador 1,agora e sua vez...')
        sleep(5)
        os.system('cls')
        acertou1 = '_' not in letras_acertadas_j1
        acertou2 = '_' not in letras_acertadas_j2
        acertou_modo_multiplayer(acertou1, acertou2, nome1, nome2, pontos_j1, pontos_j2, vida_j1, vida_j2, erros_j1,
                                 erros_j2, letras_acertadas_j1, letras_acertadas_j2)


def vida_modo_dificil_j2():
    vida_jogador_2 = 6
    return vida_jogador_2
def pontos_modo_dificil_j2():
    pontos_jogador_2 = 0
    return pontos_jogador_2
def jogar_dificl_multiplayer():
    acertou1 = False
    acertou2 = False
    print('\033[1;36m-=-\033[m' * 20)
    print('\033[1mAqui nesse modo,oo seus bonecos tem 6 vidas,os seus bonecos perderão 2 parte a cada -2 vidas\nCada um começara com 0 PTS,cada acerto e +100 PTS\nCada erro e -20 PTS.\nOBS: a dica sera introduzida no começo do jogo apenas(aumentando a dificuldade)\nOBS 2 :se por acaso o jogador 1,digitar a palavra completa,ele ganhara automaticamente.')
    print('\033[1;36m-=-\033[m' * 20)
    pontos_j1 = pontos_modo_dificil_j1()
    vida_j1 = vida_modo_dificil_j1()
    nome1 = nome_jogador()
    pontos_j2 = pontos_modo_dificil_j2()
    vida_j2 = vida_modo_dificil_j2()
    nome2 = nome_jogador2()
    escolha = input('\033[1mescolha um tema; Frutas,carros ou paises : ').upper()
    os.system('cls')
    if escolha == 'FRUTAS':
        palavra_j1 = palavra_secreta_tema_fruta()
        palavra_j2 = palavra_j1
        print('\033[1;36m-=-\033[m' * 10)
        dicas_tema_frutas(palavra_j1)
        print('\033[1m10 seg. para os jogadores memorizarem...')
        sleep(10)
        os.system('cls')
    if escolha == 'CARROS':
        palavra_j1 = palavra_secreta_tema_carros()
        palavra_j2 = palavra_j1
        print('\033[1;36m-=-\033[m' * 10)
        dicas_tema_carros(palavra_j1)
        print('\033[1m10 seg. para os jogadores memorizarem...')
        sleep(10)
        os.system('cls')
    if escolha == 'PAISES':
        palavra_j1 = palavra_secreta_tema_paises()
        palavra_j2 = palavra_j1
        print('\033[1;36m-=-\033[m' * 10)
        dicas_tema_paises(palavra_j1)
        print('\033[1m10 seg. para os jogadores memorizarem...')
        sleep(10)
        os.system('cls')
    letras_acertadas_j1 = []
    letras_acertadas_j2 = []
    letras_chutadas_j1 = []
    letras_chutadas_j2 = []
    for x in palavra_j1:
        letras_acertadas_j1.append('_')
    for x in palavra_j2:
        letras_acertadas_j2.append('_')

    erros_j1 = 0
    erros_j2 = 0
    while vida_j1 != 0 and not acertou1 and vida_j2 != 0 and not acertou2:
        tentativa_jogador_1 = input('\033[1mQual letra {},voce tabem pode tentar chutar a palavra de uma so vez! ?'.format(nome1)).upper()
        letras_chutadas_j1.append(tentativa_jogador_1)
        os.system('cls')
        if tentativa_jogador_1 == palavra_j1.upper():
            os.system('cls')
            pontos_j1 += 100
            print('\033[1mVocê ganhou {}!!\nConseguiu um bonus de 100 PTS!\nSobrou {} vidas!'.format(nome1, vida_j1))
            print(estatisticas_jogadores(nome1, pontos_j1, erros_j1, vida_j1))
            print(estatisticas_jogadores(nome2, pontos_j2, erros_j2, vida_j2))
            mostrar_trofeu()
            tocar_musica_vitoria()
            break
        if tentativa_jogador_1.upper() in palavra_j1:
            # toque_da_vitoria()
            posicao_1 = 0
            pontos_j1 = pontos_j1 + 100

            for letra in palavra_j1:
                if tentativa_jogador_1.upper() == letra.upper():
                    letras_acertadas_j1[posicao_1] = letra
                posicao_1 = posicao_1 + 1
        else:
            vida_j1 -= 2
            erros_j1 += 1
            pontos_j1 = pontos_j1 - 20
        if tentativa_jogador_1 == palavra_j1[0]:
            vida_j1 = vida_j1 + 1
            print(f'\033[1mParabens {nome1},ganhou 1 vida extra por acertar a primeira letra da palavra secreta!')
        print('voce esta assim no momento {} : {}'.format(nome1, letras_acertadas_j1))
        print('Letras chutadas :', letras_chutadas_j1,'\nForca :')
        mostrar_boneco_dificl_j1(vida_j1)
        print('prepare-se jogador 2,agora e sua vez...')
        sleep(5)
        os.system('cls')
        tentativa_jogador_2 = input('\033[1mQual letra {},voce tabem pode tentar chutar a palavra de uma so vez! ?'.format(nome2)).upper()
        letras_chutadas_j2.append(tentativa_jogador_2)
        if tentativa_jogador_2 == palavra_j2.upper():
            os.system('cls')
            pontos_j2 += 100
            print('\033[1mVocê ganhou {}!!\nConseguiu um bonus de 100 PTS!'.format(nome2, pontos_j2, vida_j2))
            print(estatisticas_jogadores(nome2, pontos_j2, erros_j2, vida_j2))
            print(estatisticas_jogadores(nome1, pontos_j1, erros_j1, vida_j1))
            mostrar_trofeu()
            tocar_musica_vitoria()
            break
        if tentativa_jogador_2.upper() in palavra_j2:
            # toque_da_vitoria()
            posicao_2 = 0
            pontos_j2 = pontos_j2 + 100
            for letra in palavra_j2:
                if tentativa_jogador_2.upper() == letra.upper():
                    letras_acertadas_j2[posicao_2] = letra
                posicao_2 = posicao_2 + 1
        else:
            vida_j2 -= 2
            erros_j2 += 1
            pontos_j2 = pontos_j2 - 20
        if tentativa_jogador_2 == palavra_j2[0]:
            vida_j2 = vida_j2 + 1
            print(f'\033[1mParabens {nome2},ganhou 1 vida extra por acertar a primeira letra da palavra secreta!')
        print('voce esta assim no momento {} : {}'.format(nome2, letras_acertadas_j2))
        print('Letras chutadas :', letras_chutadas_j2, '\nForca :')
        mostrar_boneco_dificl_j1(vida_j2)
        print('prepare-se jogador 1,agora e sua vez...')
        sleep(5)
        os.system('cls')
        acertou1 = '_' not in letras_acertadas_j1
        acertou2 = '_' not in letras_acertadas_j2
        acertou_modo_multiplayer(acertou1, acertou2, nome1, nome2, pontos_j1, pontos_j2, vida_j1, vida_j2, erros_j1,erros_j2, letras_acertadas_j1, letras_acertadas_j2)


def modo_solo():
    print(
        '\033[1mEscolha o modo de jogo logo abaixo :\033[m\n\033[1;32m-Facil\033[m\n\033[1;33m-Medio\033[m\n\033[1;31m-Dificl\033[m')
    escolha2 = input(':').lower()
    os.system('cls')
    if escolha2 == 'facil':
        # toque_da_vitoria()
        jogar_facil()
    if escolha2 == 'medio':

        jogar_medio()
        # toque_da_vitoria()
    if escolha2 == 'dificil':
        # toque_da_vitoria()
        jogar_dificl()
        # funçao princip

def modo_multiplayer():
    print('\033[1mEscolha o modo de jogo logo abaixo :\033[m\n\033[1;32m-Facil\033[m\n\033[1;33m-Medio\033[m\n\033[1;31m-Dificl\033[m')
    escolha2 = input(':').lower()
    os.system('cls')
    if escolha2 == 'facil':
        # toque_da_vitoria()
        jogar_facil_multiplayer()
    if escolha2 == 'medio':
        jogar_medio_multiplayer()
        # toque_da_vitoria()
    if escolha2 == 'dificil':
        # toque_da_vitoria()
        jogar_dificl_multiplayer()
        # funçao princip
def escolher_modo_de_jogo(): #funçao ''principal''
    print('\033[1;36m-=-\033[m'*10)
    print('\033[1mOlá,sejam bem-vindos(as) ao jogo da forca!')
    print('Deseja jogar Solo ou Multiplayer : ')
    escolha1 = input(':').upper()
    os.system('cls')
    if escolha1 == 'SOLO':
        modo_solo()
    else:
        modo_multiplayer()

escolher_modo_de_jogo() #function principal



