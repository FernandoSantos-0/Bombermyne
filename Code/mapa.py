# onde sera colocado as funcoes de sprites e construcao do mapa

import pygame
import obstaculos
import random

pygame.init()

class Texturas_para_mapa(pygame.sprite.Sprite):
    def __init__(self, X_mapa, Y_mapa, estado):
        pygame.sprite.Sprite.__init__(self)

        self.estado_textura = estado
        self.random = random.randint(0, 31)

        self.texturas = {
            "bloco_muro_sombra": pygame.image.load("Assets/sprites2/blocofrente-1.png").convert_alpha(),
            "bloco_muro": pygame.image.load("Assets/sprites2/bloco-1.png").convert_alpha(),
            "bloco_grama": Separa_Sprites_Mesmo_PNG("Assets/sprites3/TX Tileset Grass.png"), 
        }

        if self.estado_textura == 'bloco_grama':
            self.frames = self.texturas['bloco_grama']
            self.image = self.frames[self.random] 
        else:
            self.image = self.texturas[self.estado_textura]

        self.rect = self.image.get_rect()
        self.rect.topleft = (X_mapa, Y_mapa)


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

def Separa_Sprites_Mesmo_PNG(path):
    
    Largura_sprites=32 
    Altura_sprites = 32
    
    Imagem = pygame.image.load(path).convert_alpha()
    Largura_total_da_imagen, Altura_total_da_imagen = Imagem.get_size()
    
    N_colunas = Largura_total_da_imagen // Largura_sprites
    N_linhas = Altura_total_da_imagen // Altura_sprites

    frames = []

    for lin in range(N_linhas):
        for col in range(N_colunas):
            x = col * Largura_sprites
            y = lin * Altura_sprites
            rect = pygame.Rect(x, y, Largura_sprites, Altura_sprites)

            frame_surf = pygame.Surface((Largura_sprites, Altura_sprites), pygame.SRCALPHA)
            frame_surf.blit(Imagem, (0, 0), rect)

            frames.append(frame_surf)

    return frames
