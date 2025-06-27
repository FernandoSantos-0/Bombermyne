# Configurações globais

def Constantes():
    
    Largura = 640
    Altura = 480
    Largura_sprites = 32
    Altura_sprites = 32
    flag_boneco_parado = 1
    flag_bomba = 0
    
    return Largura,Altura,Largura_sprites,Altura_sprites,flag_boneco_parado,flag_bomba

def variaveis():
    
    Rodando = True
    FPS = 60
    X_Jogador = 64
    Y_Jogador = 32
    Velocidade = 3
    estado = 'parado_frente'
    quantidade_bombas = 1

    return Rodando,FPS, X_Jogador,Y_Jogador,Velocidade,estado,quantidade_bombas

def Cores():
    
    PRETO = (0,0,0)
    BRANCO = (255,255,255)

    return PRETO,BRANCO
