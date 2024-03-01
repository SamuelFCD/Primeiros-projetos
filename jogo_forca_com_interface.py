import pygame as pg
import random
import os
# Cores do jogo
branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (205,0,0)
verde_claro = (0, 255, 0)
verde_escuro = (0,139,69)
marrom = (139,69,0)
cinza = (139,129,76)
# Setup da tela do Jogo
window = pg.display.set_mode((1000, 600)) #tamanho da tela

# Inicializando fonte
pg.font.init()
# Escolhendo uma fonte e tamanho
fonte = pg.font.SysFont("Courier New", 35, 1) #fonte da palavra chave
fonte_rb = pg.font.SysFont("Courier New", 30, 1) #fonte do recomeçar
fonte_vida = pg.font.SysFont("Courier New",20,1) #fonte da vida
fonte_perdeu = pg.font.SysFont("Courier New",20,1) #fonte para aparecer o perdeu
fonte_dica = pg.font.SysFont("Courier New",20,1) #fonte da dica
palavras = ['PARALELEPIPEDO',
            'ORNITORINCO',
            'APARTAMENTO',
            'XICARA DE CHA',
            'MAX VESTAPPEN',
            'LEWIS HEMILTON',
            'AVIAO',
            'CARRO',
            'NUVEM',
            'ELEFANTE',
            'PEDRA',
            'TELHA',
            'PALHA',
            'MATRIX',
            'DIAMANTE',
            'MINECRAFT',
            'SBT',
            'GLOBO',
            'AFRICA',
            'CORINTHIANS',
            'SAO PAULO',
            'COMPUTADOR']

tentativas_de_letras = [' ', '-'] #ifem,para nao fazer a contagem
palavra_escolhida = ''
palavra_camuflada = ''
end_game = True #final do jogo
chance = 0
vida = 6
pontos = 1000
letra = ' '
click_last_status = False #clicar no botao derecomeçar
def desenho_perde(window):
    texto = fonte_perdeu.render('Voce perdeu!',1,vermelho)
    window.blit(texto,(98, 42))
def desenho_vida_inicial(window,vida):
    texto = fonte_vida.render(f'TOTAL DE CHANCES : {vida} ', 1, cinza)
    window.blit(texto, (98, 42))

def desenhando_bordas_do_jogo(window):
    pg.draw.rect(window, preto, [0, 570, 2000, 65])
    pg.draw.rect(window, preto, [0, 0, 45, 2000])
    pg.draw.rect(window, preto, [960, 0, 45, 2000])
    pg.draw.rect(window, preto, [20, 0, 2000, 40])
def Desenho_da_Forca(window, chance, vida):
    # Desenho da Forca
    pg.draw.rect(window, branco, (0, 0, 1000, 600))
    pg.draw.line(window, marrom, (100, 700), (100, 100), 10)
    pg.draw.line(window, verde_escuro, (0, 600), (1000, 600), 400)
    pg.draw.line(window, marrom,(150,100),(100, 150),10) # primeiro e as codernadas iniciais,depois finais
    pg.draw.line(window, marrom, (100, 100), (300, 100), 10)
    pg.draw.line(window, marrom, (300, 100), (300, 150), 10)

    if chance == 0:
        desenho_vida_inicial(window, vida)
    if chance >= 1:
        # Cabeça
        pg.draw.circle(window, preto, (300, 200), 50, 7)#primeiro e as coordenadas(x e y),depois o tamanho e a largura
        vida -= 1
    if chance >= 2:
        # Tronco
        pg.draw.line(window, preto, (300, 250), (300, 350), 7)
        vida -= 1
    if chance >= 3:
        # Braço Direito
        pg.draw.line(window, preto, (300, 260),(280, 350), 7)
        vida -= 1
    if chance >= 4:
        # Braço Esquerdo
        pg.draw.line(window, preto, (300, 260), (320, 350), 7)
        pg.draw.circle(window, vermelho, (240, 450), 5, 100)
        vida -= 1
    if chance >= 5:
        # Perna Direita
        pg.draw.line(window, preto, (300, 320), (315, 420), 7)
        pg.draw.circle(window, vermelho, (300, 500), 5, 100)
        vida -= 1
    if chance >= 6:
        # Perna Direita
        pg.draw.line(window, preto, (300, 320), (292, 420), 7)
        pg.draw.circle(window, vermelho, (240, 450), 5, 100)
        pg.draw.circle(window, vermelho, (370, 420), 5, 100)
        vida -= 1
        desenho_perde(window)
        mostrando_palavra(palavra_escolhida)
def Desenho_Restart_Button(window):
    texto = fonte_rb.render('RECOMEÇAR', 1, cinza)
    window.blit(texto, (710, 120))

def Sorteando_Palavra(palavras, palavra_escolhida, end_game): #verifica se o jogo terminou
    if end_game == True:
        palavra_n = random.randint(0, len(palavras) - 1) # numeors de palavras que tem
        palavra_escolhida = palavras[palavra_n]
        end_game = False
        chance = 0
    return palavra_escolhida, end_game
def mostrando_palavra(palavra):
    texto = fonte_dica.render(f'A PALAVRA SECRETA ERA : {palavra}', 1, cinza)
    window.blit(texto, (500, 250))
def dica(palavra_ecolhida):
    if palavra_ecolhida == 'PARALELEPIPEDO':
        texto = fonte_dica.render('DICA : TEM NAS RUAS', 1, cinza)
        window.blit(texto, (98, 66))
    if palavra_ecolhida == 'ORNITORINCO':
        texto = fonte_dica.render('DICA : E UM ANIMAL', 1, cinza)
        window.blit(texto, (98, 66))
    if palavra_ecolhida == 'APARTAMENTO':
        texto = fonte_dica.render('DICA : MORA-SE NESSE LOCAL', 1, cinza)
        window.blit(texto, (98, 66))
    if palavra_ecolhida == 'XICARA DE CHA':
        texto = fonte_dica.render('DICA : E UMA BEBIDA', 1, cinza)
        window.blit(texto, (98, 66))
    if palavra_ecolhida == 'MAX VESTAPPEN':
        texto = fonte_dica.render('DICA : E UM PILOTO,QUE CORRE PELA RED BULL RACING NA F1', 1, cinza)
        window.blit(texto, (98, 66))
    if palavra_ecolhida == 'LEWIS HEMILTON':
        texto = fonte_dica.render('DICA : E UM PILOTO,QUE CORRE PELA MERCEDES AMG NA F1', 1, cinza)
        window.blit(texto, (98, 66))
    if palavra_ecolhida == 'AVIAO':
        texto = fonte_dica.render('DICA : ELE VOA', 1, cinza)
        window.blit(texto, (98, 66))
    if palavra_ecolhida == 'CARRO':
        texto = fonte_dica.render('DICA : TEM RODAS', 1, cinza)
        window.blit(texto, (98, 66))
    if palavra_ecolhida == 'NUVEM':
        texto = fonte_dica.render('DICA : CAUSA A CHUVA', 1, cinza)
        window.blit(texto, (98, 66))
    if palavra_ecolhida == 'ELEFANTE':
        texto = fonte_dica.render('DICA : TEM 4 JOELHOS', 1, cinza)
        window.blit(texto, (98, 66))
    if palavra_ecolhida == 'PEDRA':
        texto = fonte_dica.render('DICA : TEM VALOR ECONOMICO', 1, cinza)
        window.blit(texto, (98, 66))
    if palavra_ecolhida == 'TELHA':
        texto = fonte_dica.render('DICA : TEM EM CIMA DAS CASAS', 1, cinza)
        window.blit(texto, (98, 66))
    if palavra_ecolhida == 'PALHA':
        texto = fonte_dica.render('DICA : FOGO DE...', 1, cinza)
        window.blit(texto, (98, 66))
    if palavra_ecolhida == 'MATRIX':
        texto = fonte_dica.render('DICA : ERRO NA...', 1, cinza)
        window.blit(texto, (98, 66))
    if palavra_ecolhida == 'DIAMANTE':
        texto = fonte_dica.render('DICA : E UM MINERAL', 1, cinza)
        window.blit(texto, (98, 66))
    if palavra_ecolhida == 'MINECRAFT':
        texto = fonte_dica.render('DICA : JOGO QUADRADO', 1, cinza)
        window.blit(texto, (98, 66))
    if palavra_ecolhida == 'SBT':
        texto = fonte_dica.render('DICA : "QUEM QUER DINHEIRO?', 1, cinza)
        window.blit(texto, (98, 66))
    if palavra_ecolhida == 'GLOBO':
        texto = fonte_dica.render('DICA : E UMA EMISSORA DE TV', 1, cinza)
        window.blit(texto, (98, 66))
    if palavra_ecolhida == 'AFRICA':
        texto = fonte_dica.render('DICA : E UM CONTINENTE', 1, cinza)
        window.blit(texto, (98, 66))
    if palavra_ecolhida == 'CORINTHIANS':
        texto = fonte_dica.render('DICA : APELIDADO DE TIMÃO', 1, cinza)
        window.blit(texto, (98, 66))
    if palavra_ecolhida == 'SAO PAULO':
        texto = fonte_dica.render('DICA : APELIDADO DE TRICOLOR', 1, cinza)
        window.blit(texto, (98, 66))
    if palavra_ecolhida == 'COMPUTADOR':
        texto = fonte_dica.render('DICA : APARELHO/OBJETO INDISPENSAVEL NOS DIAS ATUAIS', 1, cinza)
        window.blit(texto, (98, 66))



def Camuflando_Palavra(palavra_escolhida, palavra_camuflada, tentativas_de_letras): #camuflar a palavra escolhida
    palavra_camuflada = palavra_escolhida
    for n in range(len(palavra_camuflada)):
        if palavra_camuflada[n:n + 1] not in tentativas_de_letras: #aqui esta fazendo brasimente e
                                                                    #por exemplo,se P nao tiver em em tentativas,coloca a ? em cima da letra
            palavra_camuflada = palavra_camuflada.replace(palavra_camuflada[n], '?') #o replace esta colocando o ?
    return palavra_camuflada

def Tentando_uma_Letra(tentativas_de_letras, palavra_escolhida, letra, chance, pontos):
    if letra not in tentativas_de_letras:
        pontos -= 10
        tentativas_de_letras.append(letra)
        if letra not in palavra_escolhida:
            chance += 1
    elif letra in tentativas_de_letras:
        pass
    return tentativas_de_letras, chance, pontos

def Palavra_do_Jogo(window, palavra_camuflada):
    palavra = fonte.render(palavra_camuflada, 1, preto)
    window.blit(palavra, (450, 450))
def pontos_jogador(pontos):
    texto = fonte_dica.render(f'PONTOS : {pontos} ', 1, cinza)#o render,vai renderizar,ou seja,mostrar a str(pontos)
    window.blit(texto, (400, 10))

def Restart_do_Jogo(palavra_camuflada, end_game, chance, letra, tentativas_de_letras, click_last_status, click, x, y):
    count = 0
    limite = len(palavra_camuflada) #comprimento da palavra
    for n in range(len(palavra_camuflada)):
        if palavra_camuflada[n] != '#': #vai passar analisando se ainda tem ? no jogo,aq no mue caso isso
                                        #sempre vai ser True
            count += 1
    if count == limite and click_last_status == False and click[0] == True:
        print('Ok')
        if x >= 700 and x <= 900 and y >= 100 and y <= 165: #especificar onde clicar dentro do botao
            tentativas_de_letras = [' ', '-']
            end_game = True
            chance = 0
            letra = ' '
    return end_game, chance, tentativas_de_letras, letra

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        if event.type == pg.KEYDOWN:
            letra = str(pg.key.name(event.key)).upper() #ver qual variavel foi inputada dentro do jogo
            print(letra)
    # Declarando variavel da posição do mouse
    mouse = pg.mouse.get_pos() # posiçao do mause(x e y)
    mouse_position_x = mouse[0] #eixo x
    mouse_position_y = mouse[1] #eixo y

    # Declarando variavel do click do mouse
    click = pg.mouse.get_pressed() #clique do mause

    # Jogo
    Desenho_da_Forca(window, chance,vida)
    desenhando_bordas_do_jogo(window)
    Desenho_Restart_Button(window)
    palavra_escolhida, end_game = Sorteando_Palavra(palavras, palavra_escolhida, end_game)
    dica(palavra_escolhida)
    palavra_camuflada = Camuflando_Palavra(palavra_escolhida, palavra_camuflada, tentativas_de_letras)
    tentativas_de_letras, chance, pontos = Tentando_uma_Letra(tentativas_de_letras, palavra_escolhida, letra, chance, pontos)
    pontos_jogador(pontos)
    Palavra_do_Jogo(window, palavra_camuflada)
    end_game, chance, tentativas_de_letras, letra = Restart_do_Jogo(palavra_camuflada, end_game, chance, letra, tentativas_de_letras, click_last_status, click, mouse_position_x, mouse_position_y)

    # Click Last Status
    if click[0] == True:
        click_last_status = True
    else:
        click_last_status = False

    pg.display.update()