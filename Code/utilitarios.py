# Módulos utilitários (colisões, helpers)

import pygame
import settings

constantes = settings.Constantes()
largura = constantes[0]
altura = constantes[1]
Largura_sprites = constantes[2]
Altura_sprites = constantes[3]

pygame.init()

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
