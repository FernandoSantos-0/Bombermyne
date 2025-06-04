# Onde ficara futuramente a função jogo para criar a o botao no menu

import pygame
import settings
import Teclado
import player

Largura,Altura,Largura_sprites,Altura_sprites = settings.Constantes() # Constantes 

Rodando, FPS = settings.variaveis() # Variaveis 

PRETO, BRANCO = settings.Cores() # Cores

pygame.init()

Tela = pygame.display.set_mode((Largura,Altura)) # Criando tela
pygame.display.set_caption("BomberMyne")


jogador = player.Player(x=100, y=100, sprite_path="Assets/sprites/character/idle-front.png")
grupo_sprites = pygame.sprite.Group(jogador)

Relogio = pygame.time.Clock()

while Rodando:

    Relogio.tick(FPS)

    Tela.fill(PRETO)

    Rodando = Teclado.teclado()

    grupo_sprites.update()

    grupo_sprites.draw(Tela)

    pygame.display.flip()

