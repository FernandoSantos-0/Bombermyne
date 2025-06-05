# Lógica do jogador

import pygame

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
    def __init__(self,path, Largura_sprites, Altura_sprites,X_Jogador,Y_jogador):
        pygame.sprite.Sprite.__init__(self)
        
        # aqui e criado uma lista com as imagen que foram recortadas na funcao
        self.frames = Separa_Sprites_Mesmo_PNG(path, Largura_sprites, Altura_sprites) 
        
        
        self.frames_index = 0 #criando variavel valendo x
        self.image = self.frames[self.frames_index] # separando uma imagen da lista usando a variavel crianda anteriormente

        self.rect = self.image.get_rect() # pegando o tamanho da imagen em pixiel
        self.rect.topleft = (X_Jogador,Y_jogador)   # X e Y onde a imagen vai sert desenhada 

    def atualizar_sprites(self):
        self.frames_index += 0.25 # controla a velocidade por aqui quanto menor mais lento
        
        if self.frames_index >= len(self.frames): # verifica quando a variavel index for maior doque a quantidade de sprites

            self.frames_index = 0 # voltando o valor da variavel para 0 para por animacao em loop
        
        self.image = self.frames[int(self.frames_index)] # atualizando a imagen a ser desenhada 