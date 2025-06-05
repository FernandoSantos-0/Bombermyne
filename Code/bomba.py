# Comportamento das bombas

import pygame

pygame.init()

def Separa_Sprites_Bomba(Largura_sprites, Altura_sprites):
    
    Imagem = pygame.image.load("Assets\sprites\items\dynamite-pack.png").convert_alpha()
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

class Bomba(pygame.sprite.Sprite):
    def __init__(self, Largura_sprites, Altura_sprites,X_Jogador,Y_jogador):
        pygame.sprite.Sprite.__init__(self)

        self.frames = Separa_Sprites_Bomba(Largura_sprites, Altura_sprites) # definindo lista com todas as sprites recortadas 
                                                                            # (resto do codigo esplicado no arquivo player)

        self.frames_index = 0
        self.image = self.frames[self.frames_index]

        self.rect = self.image.get_rect()
        self.rect.topleft = (X_Jogador,Y_jogador)

    def Atualizar_sprite_Bomba(self):
        self.frames_index += 0.25

        if self.frames_index >= len(self.frames):
            self.frames_index = 0

        self.image = self.frames[int(self.frames_index)]

def Sprites_Bomba(Tela,grupo_sprites_bomba,dynamite):
   
    grupo_sprites_bomba.draw(Tela)
    
    dynamite.Atualizar_sprite_Bomba()    