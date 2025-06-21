import pygame

class Textos(pygame.sprite.Sprite):
    def __init__(self,X_texto,Y_texto,tipo,nova_largura,nova_altura):
        pygame.sprite.Sprite.__init__(self)

        self.Textos = {
            1: pygame.image.load("Assets/Textos/Start.png").convert_alpha(),
            2: pygame.image.load("Assets/Textos/logo.png").convert_alpha(),
            3: pygame.image.load("Assets/Textos/Creditos.png").convert_alpha(),

            5: pygame.image.load("Assets/Textos/Start.png").convert_alpha(),
            7: pygame.image.load("Assets/Textos/Creditos.png").convert_alpha(),
        }

        self.qual_texto = tipo
        self.qual_texto2 = tipo + 4
        self.image = self.Textos[self.qual_texto]

        self.image = pygame.transform.scale(self.Textos[self.qual_texto],(nova_largura, nova_altura))

        self.rect = self.image.get_rect()
        self.rect.topleft = (X_texto,Y_texto)

    def update(self):
        pos_mouse = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos_mouse):
            self.image = self.Textos[self.qual_texto2] 
        else:
            self.image = self.Textos[self.qual_texto]
