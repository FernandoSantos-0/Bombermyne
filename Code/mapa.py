# onde sera colocado as funcoes de sprites e construcao do mapa

import pygame

pygame.init()

def Mapa1(Tela):

    bloco_muro_sombra = pygame.image.load("Assets/sprites2/blocofrente-1.png").convert_alpha()

    bloco_muro = pygame.image.load("Assets/sprites2/bloco-1.png").convert_alpha()

    bloco_grama = pygame.image.load("Assets/sprites/terrain/grass - Copia.png").convert_alpha()

    size_textura = 32

    # bloco_grama = 1, bloco_muro_sombra = 2, bloco_muro = 3, vazio = 0

    matriz_mapa = [
        [3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3],
        [3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3],
        [3,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,3],
        [3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3],
        [3,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,3],
        [3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3],
        [3,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,3],
        [3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3],
        [3,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,3],
        [3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3],
        [3,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,3],
        [3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3],
        [3,1,2,1,2,1,2,1,2,1,1,2,1,2,1,2,1,2,1,3],
        [3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3],
        [3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3],
    ]


    for y, linha in enumerate(matriz_mapa):
        for x, coluna in enumerate(linha):
            if coluna == 1:
                Tela.blit(bloco_grama, (x * size_textura, y * size_textura))
            elif coluna == 2:
                Tela.blit(bloco_muro_sombra, (x * size_textura, y * size_textura))
            elif coluna == 3:
                Tela.blit(bloco_muro, (x * size_textura, y * size_textura))