# Módulos utilitários (colisões, helpers)

import pygame
import settings

constantes = settings.Constantes()
largura = constantes[0]
altura = constantes[1]
Largura_sprites = constantes[2]
Altura_sprites = constantes[3]

pygame.init()

def Grupos_De_Sprites(jogador):
    
    grupo_sprites = pygame.sprite.Group(jogador)
    grupo_sprites_bomba = pygame.sprite.Group() # incializando um grupos de sprites para bombas
    grupo_sprites_explosa = pygame.sprite.Group() # incializando um grupos de sprites para explosoes
    grupo_sprites_mapa = pygame.sprite.Group()
    grupo_sprites_mapa_colisoes = pygame.sprite.Group()
    grupo_obstaculos = pygame.sprite.Group()

    return grupo_sprites,grupo_sprites_bomba,grupo_sprites_explosa,grupo_sprites_mapa,grupo_sprites_mapa_colisoes,grupo_obstaculos 

def Colisao_janela(X_Jogador,Y_Jogador):
    if X_Jogador < 0:  
        X_Jogador = 0
    
    if X_Jogador > largura-32:
        X_Jogador = largura - Largura_sprites

    if Y_Jogador < 0:  
        Y_Jogador = 0
    
    if Y_Jogador > altura-32:
        Y_Jogador = altura - Altura_sprites

    return X_Jogador,Y_Jogador

def Colisao_mapa(jogador,grupo_sprites_mapa_colisoes,x_anterio,y_anterior, X_Jogador,Y_Jogador):
    if pygame.sprite.spritecollideany(jogador,grupo_sprites_mapa_colisoes):
        X_Jogador = x_anterio
        Y_Jogador = y_anterior
    return X_Jogador,Y_Jogador

def colisao_bomba(jogador,grupo_sprites_bomba,x_anterio,y_anterio, X_Jogador,Y_Jogador,bomba_atual):

    bomba_colidida = pygame.sprite.spritecollideany(jogador,grupo_sprites_bomba)

    if bomba_colidida:

        if bomba_colidida == bomba_atual:
            return X_Jogador,Y_Jogador, bomba_atual
        else:
            X_Jogador = x_anterio
            Y_Jogador = y_anterio
            return X_Jogador,Y_Jogador, bomba_atual
    else:
        return X_Jogador,Y_Jogador,None

def Desenhar_mapa(grupo_sprites_mapa,grupo_sprites_mapa_colisoes,grupo_obstaculos,Tela,grupo_sprites_explosa):    
    
    grupo_sprites_mapa.draw(Tela)
    
    grupo_sprites_explosa.draw(Tela)
    grupo_sprites_explosa.update()
    
    grupo_sprites_mapa_colisoes.draw(Tela)
    
    grupo_obstaculos.draw(Tela)
    grupo_obstaculos.update(grupo_sprites_explosa)
