import pygame
import settings
import TelaMenu

pygame.init()

def menu():

    constantes = settings.Constantes()
    largura = constantes[0]
    altura = constantes[1]
    
    rodando = settings.variaveis()[0]

    PRETO = settings.Cores()[0]

    # TELA/JANELA
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Menu")

    relogio = pygame.time.Clock()

    while rodando:

        tela.fill(PRETO)
        relogio.tick(30)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

        pygame.display.update()

    pygame.quit()

