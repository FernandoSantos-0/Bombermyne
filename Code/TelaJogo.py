# Onde ficara futuramente a função jogo para criar a o botao no menu

import pygame
import settings
import Teclado

Largura,Altura,Largura_sprites,Altura_sprites = settings.Constantes() # Constantes 

Rodando = settings.variaveis() # Variaveis 

PRETO = settings.Cores() # Cores

pygame.init()

Tela = pygame.display.set_mode((Largura,Altura)) # Criando tela
pygame.display.set_caption("BomberMyne")

while Rodando:

    Tela.fill(PRETO)

    Rodando = Teclado.teclado()

    pygame.display.flip()

