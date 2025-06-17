# onde sera colocado as funcoes de sprites e construcao do mapa

import pygame

pygame.init()

class Texturas_para_mapa(pygame.sprite.Sprite):
    def __init__(self,X_mapa,Y_mapa,estado):
        pygame.sprite.Sprite.__init__(self)

        self.texturas = {
            "bloco_muro_sombra": pygame.image.load("Assets/sprites2/blocofrente-1.png").convert_alpha(),
            "bloco_muro": pygame.image.load("Assets/sprites2/bloco-1.png").convert_alpha(),
            "bloco_grama": pygame.image.load("Assets/sprites/terrain/grass - Copia.png").convert_alpha(),
        }

        self.estado_textura = estado
        self.image = self.texturas[self.estado_textura]

        self.rect = self.image.get_rect() # pegando o tamanho da image em pixiel
        self.rect.topleft = (X_mapa,Y_mapa)   # X e Y onde a image vai sert desenhada 
    
    def mudar_estado(self,estado):
        self.image = self.texturas[estado]

def Mapa1(grupo_sprites_mapa,grupo_sprites_mapa_colisoes):

    size_textura = 32

    # bloco_grama = 1, bloco_muro_sombra = 2, bloco_muro = 3, vazio = 0
    # matriz que representa a tela do jogo ultilizando blocos de 32x32 px

    matriz_mapa1 = [

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
        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
        
    ]

    for y, linha in enumerate(matriz_mapa1):
        for x, coluna in enumerate(linha):
            if coluna == 1:
                estado = "bloco_grama"
                
            elif coluna == 2:
                estado = "bloco_muro_sombra"

            elif coluna == 3:
                estado = "bloco_muro"

            else:
                continue

            if estado == "bloco_muro_sombra" or estado == "bloco_muro":
                bloco_colisao = Texturas_para_mapa(x * size_textura, y * size_textura, estado)
                grupo_sprites_mapa_colisoes.add(bloco_colisao)    
            
            bloco = Texturas_para_mapa(x * size_textura, y * size_textura, estado)
            grupo_sprites_mapa.add(bloco)
