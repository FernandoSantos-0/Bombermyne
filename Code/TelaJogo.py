# Onde ficara futuramente a função jogo para criar a o botao no menu

import pygame
import settings
import Teclado
import player

Largura,Altura,Largura_sprites,Altura_sprites = settings.Constantes() # Constantes 

Rodando, FPS, X_Jogador,Y_Jogador,Velocidade = settings.variaveis() # Variaveis 

PRETO, BRANCO = settings.Cores() # Cores

pygame.init()

Tela = pygame.display.set_mode((Largura,Altura)) # Criando tela
pygame.display.set_caption("BomberMyne") # Nomeando a Tela

jogador = player.Player(X_Jogador, Y_Jogador, sprite_path="Assets/sprites/character/idle-front.png") 
grupo_sprites = pygame.sprite.Group(jogador)

Relogio = pygame.time.Clock() # Definindo relogio

while Rodando:

    Relogio.tick(FPS) # FPS

    Tela.fill(PRETO) # Pintando a tela de Preto

    Rodando,X_Jogador,Y_Jogador = Teclado.teclado(X_Jogador,Y_Jogador,Velocidade) # Integração com o teclado

    jogador.rect.topleft = (X_Jogador, Y_Jogador)

    grupo_sprites.update() #Atualiza as sprites

    grupo_sprites.draw(Tela) # desenha as sprites
    
    pygame.display.flip() # Atualiza a tela

