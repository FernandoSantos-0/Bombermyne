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

Relogio = pygame.time.Clock() # Definindo relogio

jogador = player.Player("Assets/sprites/character/idle-front.png", Largura_sprites, Altura_sprites,X_Jogador, Y_Jogador)
grupo_sprites = pygame.sprite.Group(jogador)

while Rodando:

    Relogio.tick(FPS) # FPS

    Tela.fill(PRETO) # Pintando a tela de Preto

    Rodando,X_Jogador,Y_Jogador = Teclado.teclado(X_Jogador,Y_Jogador,Velocidade) # Integração com o teclado
    
    grupo_sprites.draw(Tela) # Desenha o sprite 
    
    jogador.atualizar_sprites() # atualiza o sprite para no proximo rodada do while ser outra

    jogador.rect.topleft = (X_Jogador, Y_Jogador) # atualiza as cordenadas no X e Y do personagem

    pygame.display.flip() # Atualiza a tela

