import pygame
import settings
import Auxiliar_Menu
import TelaJogo
import TelaCreditos

pygame.init()

def menu():

    X_start = 220
    y_start = 208

    X_creditos = 220
    y_creditos = 291

    x_logo = 32
    y_logo = 30

    tipo_start = 1
    tipo_creditos = 3
    tipo_logo = 2

    constantes = settings.Constantes()
    largura = constantes[0]
    altura = constantes[1]
    
    rodando = True

    PRETO = settings.Cores()[1]

    # TELA/JANELA
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Menu")

    relogio = pygame.time.Clock()

    texto_start = Auxiliar_Menu.Textos(X_start,y_start,tipo_start,nova_largura=200,nova_altura=63)

    texto_creditos = Auxiliar_Menu.Textos(X_creditos,y_creditos,tipo_creditos,nova_largura=200,nova_altura=52)

    texto_logo = Auxiliar_Menu.Textos(x_logo,y_logo,tipo_logo,nova_largura=576,nova_altura=107)

    grupo_sprite_textos = pygame.sprite.Group()

    grupo_sprite_textos.add(texto_start)
    grupo_sprite_textos.add(texto_creditos)
    grupo_sprite_textos.add(texto_logo)
    
    while rodando:
        
        tela.fill(PRETO)

        grupo_sprite_textos.draw(tela)
        grupo_sprite_textos.update()

        relogio.tick(30)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:
                    pos_mouse = pygame.mouse.get_pos()
                    if texto_start.rect.collidepoint(pos_mouse):
                        TelaJogo.jogo()
                    elif texto_creditos.rect.collidepoint(pos_mouse):
                        TelaCreditos.creditos()
                    elif texto_logo.rect.collidepoint(pos_mouse):
                        print("Clicou no logo!")

        pygame.display.update()

    pygame.quit()
