# Comportamento das bombas

import pygame

pygame.init()

def Separa_Sprites_Bomba(path,Largura_sprites, Altura_sprites):
    
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

class Bomba(pygame.sprite.Sprite):
    def __init__(self, Largura_sprites, Altura_sprites,X_Jogador,Y_jogador):
        pygame.sprite.Sprite.__init__(self)

        self.frames = Separa_Sprites_Bomba("Assets/sprites/items/dynamite-pack.png",Largura_sprites, Altura_sprites) 
        # definindo lista com todas as sprites recorta (resto do codigo esplicado no arquivo player).

        self.frames_index = 0
        self.image = self.frames[self.frames_index]

        self.rect = self.image.get_rect()
        self.rect.topleft = (X_Jogador,Y_jogador)

        self.tempo_incial = pygame.time.get_ticks() # marca o tempo que a bomba foi colocada

        self.x_jogador_explosa = X_Jogador
        self.y_jogador_explosa = Y_jogador
        self.altura_sprite = Altura_sprites
        self.largura_sprites = Largura_sprites


    def update(self,grupo_sprites_explosa):
        self.frames_index += 0.25

        if self.frames_index >= len(self.frames):
            self.frames_index = 0

        self.image = self.frames[int(self.frames_index)]
        
        self.tempo_atual = pygame.time.get_ticks()
        if (self.tempo_atual - self.tempo_incial) >= 2000:
            nova_explosao = Explosao(self.largura_sprites,self.altura_sprite,self.x_jogador_explosa,self.y_jogador_explosa)
            grupo_sprites_explosa.add(nova_explosao) 
            self.kill() # remove a bomba

def Sprites_Bomba(Tela,grupo_sprites_bomba,grupo_sprites_explosa):
    grupo_sprites_bomba.update(grupo_sprites_explosa)
    grupo_sprites_bomba.draw(Tela)
    
class Explosao(pygame.sprite.Sprite):
    def __init__(self,Largura_sprites, Altura_sprites,X_Jogador,Y_Jogador):
        pygame.sprite.Sprite.__init__(self)

        self.animacao_explosao = {
            'explosao': Separa_Sprites_Bomba("Assets/sprites/fxs/explosion.png", Largura_sprites, Altura_sprites)
        }
        self.estado = 'explosao'
        self.frames = self.animacao_explosao[self.estado]

        self.frames_index = 0
        self.image = self.frames[self.frames_index]

        self.rect = self.image.get_rect()
        self.rect.topleft = (X_Jogador,Y_Jogador)

        self.time_incio = pygame.time.get_ticks()

    def update(self):
        self.frames_index += 0.25

        if self.frames_index >= len(self.frames):
            self.frames_index = 0

        self.image = self.frames[int(self.frames_index)]

        self.time_atual = pygame.time.get_ticks()
        if (self.time_atual - self.time_incio) >= 500:
            self.kill()

def sprites_explosao(Tela,grupo_sprites_explosao):
    
    grupo_sprites_explosao.update()
    grupo_sprites_explosao.draw(Tela)
            