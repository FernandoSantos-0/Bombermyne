# Comportamento das bombas

import pygame

pygame.init()

def arredondar_para_32(n, tolerancia=16):
    resto = n % 32
    if resto <= tolerancia:
        return n - resto
    elif 32 - resto <= tolerancia:
        return n + (32 - resto)
    return n 

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

        X_Jogador = arredondar_para_32(X_Jogador)
        Y_jogador = arredondar_para_32(Y_jogador)

        self.rect = self.image.get_rect()
        self.rect.topleft = (X_Jogador,Y_jogador)

        self.tempo_incial = pygame.time.get_ticks() # marca o tempo que a bomba foi colocada

        self.x_jogador_explosa = X_Jogador
        self.y_jogador_explosa = Y_jogador
        self.altura_sprite = Altura_sprites
        self.largura_sprites = Largura_sprites

        self.raio = 1 # controla raio da explosao = tamanho do raio - 1

    def update(self, grupo_sprites_explosa, grupo_sprites_mapa_colisoes,grupo_sprites_bomba):
        self.frames_index += 0.25
        if self.frames_index >= len(self.frames):
            self.frames_index = 0

        self.image = self.frames[int(self.frames_index)]

        self.tempo_atual = pygame.time.get_ticks()
        if (self.tempo_atual - self.tempo_incial) >= 2000:

            grupo_sprites_explosa.add(Explosao(self.largura_sprites, self.altura_sprite, self.x_jogador_explosa, self.y_jogador_explosa))

            direcoes = [(0, -1), (0, 1), (1, 0), (-1, 0)]

            for direcao_x, direcao_y in direcoes:
                for i in range(1, self.raio + 1):
                    x = self.x_jogador_explosa + direcao_x * 32 * i
                    y = self.y_jogador_explosa + direcao_y * 32 * i

                    nova_explosao = Explosao(self.largura_sprites, self.altura_sprite, x, y)

                    if pygame.sprite.spritecollide(nova_explosao, grupo_sprites_mapa_colisoes, False):
                        grupo_sprites_explosa.add(nova_explosao)  
                        break  
                    else:
                        grupo_sprites_explosa.add(nova_explosao)
                    
                    bomba_colisao = pygame.sprite.spritecollide(nova_explosao, grupo_sprites_bomba, False)
                    for bomba in bomba_colisao:
                        bomba.tempo_incial = 0
                    
            self.kill() 

def Sprites_Bomba(Tela,grupo_sprites_bomba,grupo_sprites_explosa,grupo_sprites_mapa_colisoes):
    grupo_sprites_bomba.update(grupo_sprites_explosa,grupo_sprites_mapa_colisoes,grupo_sprites_bomba)
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
        