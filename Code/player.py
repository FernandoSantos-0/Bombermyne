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

        # Separa e carrega uma lista com as sprites no msm png
        self.frames = Separa_Sprites_Mesmo_PNG(sprite_path, Largura_sprites, Altura_sprites)

        # Inicializa o frame atual
        self.frame_index = 0
        self.image = self.frames[self.frame_index]

        # Posição
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        # Controle da animação
        self.contador_animacao = 0
        self.velocidade_animacao = 10  # menor = mais rápido

    def update(self):
        # Atualiza a animação
        self.contador_animacao += 1
        if self.contador_animacao >= self.velocidade_animacao:
            self.contador_animacao = 0
            self.frame_index = (self.frame_index + 1) % len(self.frames)
            self.image = self.frames[self.frame_index]