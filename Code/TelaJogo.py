# Onde ficara futuramente a função jogo para criar a o botao no menu

import pygame
import settings
import Teclado
import player 
import bomba
import utilitarios

Largura,Altura,Largura_sprites,Altura_sprites,flag_boneco_parado,flag_bomba = settings.Constantes() # Constantes 

Rodando, FPS, X_Jogador,Y_Jogador,Velocidade,estado = settings.variaveis() # Variaveis 

PRETO, BRANCO = settings.Cores() # Cores

pygame.init()

Tela = pygame.display.set_mode((Largura,Altura)) # Criando tela
pygame.display.set_caption("BomberMyne") # Nomeando a Tela

Relogio = pygame.time.Clock() # Definindo relogio

jogador = player.Player(Largura_sprites, Altura_sprites,X_Jogador, Y_Jogador)
grupo_sprites = pygame.sprite.Group(jogador)

grupo_sprites_bomba = pygame.sprite.Group() # incializando um grupos de sprites para bombas

grupo_sprites_explosa = pygame.sprite.Group() # incializando um grupos de sprites para explosoes

while Rodando:

    Relogio.tick(FPS) # FPS

    Tela.fill(PRETO) # Pintando a tela de Preto

    Rodando,X_Jogador,Y_Jogador,estado,flag_boneco_parado,flag_bomba = Teclado.teclado(X_Jogador,Y_Jogador,Velocidade,estado,flag_boneco_parado,flag_bomba) # Integração com o teclado
    
    if flag_bomba == 1:       
        nova_bomba = bomba.Bomba(Largura_sprites, Altura_sprites,X_Jogador, Y_Jogador)
        grupo_sprites_bomba.add(nova_bomba)
        flag_bomba = 0

    bomba.Sprites_Bomba(Tela,grupo_sprites_bomba,grupo_sprites_explosa) # comando necessario para o desenha na tela a bomba e chamar a class bomba
    
    bomba.sprites_explosao(Tela,grupo_sprites_explosa) # desenha a explosao

    player.sprites_jogador(grupo_sprites,Tela,jogador,X_Jogador,Y_Jogador,estado) # comando necessario para desenha na tela o player 

    for sprite in grupo_sprites:
        utilitarios.Colisao_janela(sprite, Largura, Altura)

    pygame.display.flip() # Atualiza a tela

