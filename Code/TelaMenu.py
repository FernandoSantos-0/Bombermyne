# onde ficara a funcao menu que chamara as funcoes jogo e creditos

import pygame
import settings
import Auxiliar_Menu
import TelaJogo
import TelaCreditos

pygame.init()

def menu():

    constantes = settings.Constantes()
    largura = constantes[0]
    altura = constantes[1]
    rodando = True

    PRETO = settings.Cores()[0]

    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Menu")
    relogio = pygame.time.Clock()

    x_central = (largura - 200) // 2
    
    texto_start = Auxiliar_Menu.Textos(x_central, 210, tipo=1)
    texto_creditos = Auxiliar_Menu.Textos(x_central, 270, tipo=2)
    texto_exit = Auxiliar_Menu.Textos(x_central, 330, tipo=3)
    texto_logo = Auxiliar_Menu.Textos(32, 30, tipo=4)

    grupo_sprite_textos = pygame.sprite.Group(
        texto_logo, texto_start, texto_creditos, texto_exit
    )

    while rodando:

        relogio.tick(60)

        tela.fill(PRETO)
        
        grupo_sprite_textos.draw(tela)
        grupo_sprite_textos.update()

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
                    elif texto_exit.rect.collidepoint(pos_mouse):
                        rodando = False

        pygame.display.update()

    pygame.quit()
