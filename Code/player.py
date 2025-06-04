# Lógica do jogador

import pygame
import settings

Largura,Altura,Largura_sprites,Altura_sprites = settings.Constantes() # Constantes 

pygame.init()

def Separa_Sprites_Mesmo_PNG(path, Largura_sprites, Altura_sprites):
    
    Imagem = pygame.image.load(path).convert_alpha()
    sheet_width, sheet_height = Imagem.get_size()
    
    N_colunas = sheet_width // Largura_sprites
    N_linhas = sheet_height // Altura_sprites

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

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, sprite_path):
        super().__init__()

        # Separa e carrega uma lista com as sprites (frames) que estão no mesmo PNG
        self.frames = Separa_Sprites_Mesmo_PNG(sprite_path, Largura_sprites, Altura_sprites)

        # Inicializa o índice do frame atual e define a imagem que será desenhada
        self.frame_index = 0
        self.image = self.frames[self.frame_index]

        # Cria o rect (retângulo) de posicionamento com base na imagem
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        # Contadores para controlar a troca de frames (animação)
        self.contador_animacao = 0
        self.velocidade_animacao = 10  # quanto menor, mais rápida a troca de frames

    def update(self):
        # Aumenta o contador a cada chamada de update()
        self.contador_animacao += 1

        # Quando o contador alcança 'velocidade_animacao', troca de frame
        if self.contador_animacao >= self.velocidade_animacao:
            self.contador_animacao = 0
            # calcula o próximo índice de frame (cíclico, com %)
            self.frame_index = (self.frame_index + 1) % len(self.frames)
            # atualiza a imagem que será desenhada
            self.image = self.frames[self.frame_index]
