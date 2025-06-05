import pygame
import settings

Rodando, FPS, X_Jogador,Y_Jogador,Velocidade = settings.variaveis() # Variaveis 

import pygame

def teclado(X_Jogador, Y_Jogador, velocidade):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False, X_Jogador, Y_Jogador
        
    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_UP]:
        Y_Jogador -= velocidade

    if teclas[pygame.K_DOWN]:
        Y_Jogador += velocidade

    if teclas[pygame.K_LEFT]:
        X_Jogador -= velocidade

    if teclas[pygame.K_RIGHT]:
        X_Jogador += velocidade
        

    return True, X_Jogador, Y_Jogador
