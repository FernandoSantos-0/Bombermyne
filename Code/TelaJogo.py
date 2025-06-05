# Onde ficara futuramente a função jogo para criar a o botao no menu

import pygame
import settings
import Teclado
import player 
import bomba

Largura,Altura,Largura_sprites,Altura_sprites,flag_boneco_parado = settings.Constantes() # Constantes 

Rodando, FPS, X_Jogador,Y_Jogador,Velocidade,estado = settings.variaveis() # Variaveis 


PRETO, BRANCO = settings.Cores() # Cores

pygame.init()

Tela = pygame.display.set_mode((Largura,Altura)) # Criando tela
pygame.display.set_caption("BomberMyne") # Nomeando a Tela

Relogio = pygame.time.Clock() # Definindo relogio

jogador = player.Player(Largura_sprites, Altura_sprites,X_Jogador, Y_Jogador)
grupo_sprites = pygame.sprite.Group(jogador)

dynamite = bomba.Bomba(Largura_sprites, Altura_sprites,X_Jogador, Y_Jogador)
grupo_sprites_bomba = pygame.sprite.Group(dynamite)

while Rodando:

    Relogio.tick(FPS) # FPS

    Tela.fill(PRETO) # Pintando a tela de Preto

    Rodando,X_Jogador,Y_Jogador,estado,flag_boneco_parado = Teclado.teclado(X_Jogador,Y_Jogador,Velocidade,estado,flag_boneco_parado) # Integração com o teclado
    
    bomba.Sprites_Bomba(Tela,grupo_sprites_bomba,dynamite) # comando necessario para o desenha na tela a bomba

    player.sprites_jogador(grupo_sprites,Tela,jogador,X_Jogador,Y_Jogador,estado) # comando necessario para desenha na tela o player 

    pygame.display.flip() # Atualiza a tela

