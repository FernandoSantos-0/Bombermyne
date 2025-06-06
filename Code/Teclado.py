import pygame


def teclado(X_Jogador, Y_Jogador, velocidade,estado,flag_boneco_parado,flag_bomba):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False, X_Jogador, Y_Jogador,estado,flag_boneco_parado,flag_bomba
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                flag_bomba = 1

    teclas = pygame.key.get_pressed()
    estado = None

    if teclas[pygame.K_UP]:
        Y_Jogador -= velocidade
        estado = 'andando_cima'
        flag_boneco_parado = 1

    elif teclas[pygame.K_DOWN]:
        Y_Jogador += velocidade
        estado = 'andando_baixo'
        flag_boneco_parado = 2

    elif teclas[pygame.K_LEFT]:
        X_Jogador -= velocidade
        estado = 'andando_esquerda'
        flag_boneco_parado = 3

    elif teclas[pygame.K_RIGHT]:
        X_Jogador += velocidade
        estado = 'andando_direita'
        flag_boneco_parado = 4

    else:
        if(flag_boneco_parado == 1):
            estado = 'parado_cima'
        
        elif(flag_boneco_parado == 2):
            estado = 'parado_baixo'
        
        elif(flag_boneco_parado == 3):
            estado = 'parado_esquerda'
        
        elif(flag_boneco_parado == 4):
            estado = 'parado_direita'

    return True, X_Jogador, Y_Jogador,estado,flag_boneco_parado,flag_bomba
