import pygame

class Textos(pygame.sprite.Sprite):
    def __init__(self, X_texto, Y_texto, tipo):
        pygame.sprite.Sprite.__init__(self)

        self.imagens_originais = {
            1: pygame.image.load("Assets/Textos/start1.png").convert_alpha(),
            5: pygame.image.load("Assets/Textos/start_hover.png").convert_alpha(),

            2: pygame.image.load("Assets/Textos/credits.png").convert_alpha(),
            6: pygame.image.load("Assets/Textos/credits_hover.png").convert_alpha(),
            
            3: pygame.image.load("Assets/Textos/exit.png").convert_alpha(),
            7: pygame.image.load("Assets/Textos/exit_hover.png").convert_alpha(),

            4: pygame.image.load("Assets/Textos/logo.png").convert_alpha(),
            8: pygame.image.load("Assets/Textos/logo.png").convert_alpha(),
        }

        self.qual_texto = tipo
        self.qual_texto2 = tipo + 4

        imagem_normal = self.imagens_originais[self.qual_texto]
        imagem_hover = self.imagens_originais[self.qual_texto2]

        if tipo == 4:  
            largura_desejada = 576
        else:
            largura_desejada = 200

        largura_original = imagem_normal.get_width()
        altura_original = imagem_normal.get_height()
        altura_desejada = int(altura_original * (largura_desejada / largura_original))

        self.image_normal = pygame.transform.scale(imagem_normal, (largura_desejada, altura_desejada))
        self.image_hover = pygame.transform.scale(imagem_hover, (largura_desejada, altura_desejada))

        self.image = self.image_normal
        self.rect = self.image.get_rect()
        self.rect.topleft = (X_texto, Y_texto)

    def update(self):
        pos_mouse = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos_mouse):
            self.image = self.image_hover
        else:
            self.image = self.image_normal
