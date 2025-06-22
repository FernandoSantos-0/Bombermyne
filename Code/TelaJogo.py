# Onde ficara futuramente a função jogo para criar a o botao no menu

import pygame
import settings
import Teclado
import player 
import bomba
import utilitarios
import mapa

def jogo():
    
    Largura,Altura,Largura_sprites,Altura_sprites,flag_boneco_parado,flag_bomba = settings.Constantes() # Constantes 

    Rodando, FPS, X_Jogador,Y_Jogador,Velocidade,estado = settings.variaveis() # Variaveis 

    PRETO, BRANCO = settings.Cores() # Cores

    pygame.init()

    Tela = pygame.display.set_mode((Largura,Altura)) # Criando tela
    pygame.display.set_caption("BomberMyne") # Nomeando a Tela

    Relogio = pygame.time.Clock() # Definindo relogio

    jogador = player.Player(Largura_sprites, Altura_sprites,X_Jogador, Y_Jogador)

    grupo_sprites,grupo_sprites_bomba,grupo_sprites_explosa,grupo_sprites_mapa,grupo_sprites_mapa_colisoes,grupo_obstaculos  = utilitarios.Grupos_De_Sprites(jogador)

    mapa.Mapa1(grupo_sprites_mapa,grupo_sprites_mapa_colisoes,grupo_obstaculos) # cria o mapa

    while Rodando:

        Relogio.tick(FPS) # FPS

        Tela.fill(PRETO) # Pintando a tela de Preto

        utilitarios.Desenhar_mapa(grupo_sprites_mapa,grupo_sprites_mapa_colisoes,grupo_obstaculos,Tela,grupo_sprites_explosa)

        utilitarios.Colisao_explosao(grupo_sprites_explosa,grupo_sprites_mapa_colisoes)

        x_anterio = X_Jogador
        y_anterior = Y_Jogador

        Rodando,X_Jogador,Y_Jogador,estado,flag_boneco_parado,flag_bomba= Teclado.teclado(X_Jogador,Y_Jogador,Velocidade,estado,flag_boneco_parado,flag_bomba) # Integração com o teclado

        if flag_bomba == 1:       
            nova_bomba = bomba.Bomba(Largura_sprites, Altura_sprites,X_Jogador, Y_Jogador)
            grupo_sprites_bomba.add(nova_bomba)
            flag_bomba = 0

        bomba.Sprites_Bomba(Tela,grupo_sprites_bomba,grupo_sprites_explosa) # comando necessario para o desenha na tela a bomba e chamar a class bomba
        
        bomba.sprites_explosao(Tela,grupo_sprites_explosa) # desenha a explosao

        player.sprites_jogador(grupo_sprites,Tela,jogador,X_Jogador,Y_Jogador,estado) # comando necessario para desenha na tela o player 

        X_Jogador,Y_Jogador = utilitarios.Colisao_mapa(jogador,grupo_sprites_mapa_colisoes,x_anterio,y_anterior, X_Jogador,Y_Jogador)

        X_Jogador,Y_Jogador = utilitarios.Colisao_janela(X_Jogador,Y_Jogador)
        
        pygame.display.flip() # Atualiza a tela
