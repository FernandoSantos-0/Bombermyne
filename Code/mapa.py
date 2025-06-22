# onde sera colocado as funcoes de sprites e construcao do mapa

import pygame
import obstaculos

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

def Mapa1(grupo_sprites_mapa, grupo_sprites_mapa_colisoes, grupo_obstaculos):
    
    size_textura = 32

    matriz_mapa1 = [

    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,1,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,1,1,2],
    [2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,4,2],
    [2,4,1,4,1,4,1,1,1,1,1,4,1,4,1,4,1,4,1,2],
    [2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,1,2],
    [2,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,2],
    [2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,1,2],
    [2,4,1,4,1,4,1,1,1,1,1,4,1,4,1,4,1,4,1,2],
    [2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,4,2],
    [2,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,1,2],
    [2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,1,2],
    [2,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,2],
    [2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,4,2],
    [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
    [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],

    ]

    for y, linha in enumerate(matriz_mapa1):
        for x, coluna in enumerate(linha):
            px = x * size_textura
            py = y * size_textura

            if coluna == 1:
                estado = "bloco_grama"
           
            elif coluna == 2:
                estado = "bloco_muro_sombra"
           
            elif coluna == 3:
                estado = "bloco_muro"
           
            elif coluna == 4:
                
                bloco_grama = Texturas_para_mapa(px, py, "bloco_grama")
                grupo_sprites_mapa.add(bloco_grama)

                caixa = obstaculos.Obstaculos_Caixas(px, py, "Caixa_Madeira")
                grupo_obstaculos.add(caixa)
                grupo_sprites_mapa_colisoes.add(caixa)
                continue 

            else:
                continue

            bloco = Texturas_para_mapa(px, py, estado)
            grupo_sprites_mapa.add(bloco)

            if estado in ["bloco_muro", "bloco_muro_sombra"]:
                grupo_sprites_mapa_colisoes.add(bloco)
