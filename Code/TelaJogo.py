# Onde ficara futuramente a função jogo para criar a o botao no menu

import pygame
import settings
import Teclado
import player

Largura,Altura,Largura_sprites,Altura_sprites,flag_boneco_parado = settings.Constantes() # Constantes 

Rodando, FPS, X_Jogador,Y_Jogador,Velocidade,estado = settings.variaveis() # Variaveis 


PRETO, BRANCO = settings.Cores() # Cores

pygame.init()

Tela = pygame.display.set_mode((Largura,Altura)) # Criando tela
pygame.display.set_caption("BomberMyne") # Nomeando a Tela

Relogio = pygame.time.Clock() # Definindo relogio

jogador = player.Player(Largura_sprites, Altura_sprites,X_Jogador, Y_Jogador)
grupo_sprites = pygame.sprite.Group(jogador)

while Rodando:

    Relogio.tick(FPS) # FPS

    Tela.fill(PRETO) # Pintando a tela de Preto

    Rodando,X_Jogador,Y_Jogador,estado,flag_boneco_parado = Teclado.teclado(X_Jogador,Y_Jogador,Velocidade,estado,flag_boneco_parado) # Integração com o teclado
    
    grupo_sprites.draw(Tela) # Desenha o sprite 
    
    jogador.atualizar_sprites() # atualiza o sprite para no proximo rodada do while ser outra

    jogador.rect.topleft = (X_Jogador, Y_Jogador) # atualiza as cordenadas no X e Y do personagem

    if jogador.estado != estado: # checa se o estado dentro da class e o criado na pasta settings sao diferentes
        jogador.estado = estado 
        jogador.frames = jogador.animacoes[estado]
        jogador.frames_index = 0

        # se forem entao o estado dentro do class e mudado o index e reiniciado e a animacao e trocado para a 
        # o que representa o estado novo(o que foi definido pelas teclas)

    pygame.display.flip() # Atualiza a tela

