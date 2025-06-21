import pygame

class Textos(pygame.sprite.Sprite):
    def __init__(self, X_texto, Y_texto, tipo, nova_largura, nova_altura):
        pygame.sprite.Sprite.__init__(self)


        imagens_originais = {
            1: pygame.image.load("Assets/Textos/Start_refeito.png").convert_alpha(),
            2: pygame.image.load("Assets/Textos/logo.png").convert_alpha(),
            3: pygame.image.load("Assets/Textos/Creditos.png").convert_alpha(),
            
            5: pygame.image.load("Assets/Textos/Start_refeito_hover.png").convert_alpha(),
            6: pygame.image.load("Assets/Textos/logo.png").convert_alpha(),
            7: pygame.image.load("Assets/Textos/Creditos_hover.png").convert_alpha(),
        }

        self.Textos_escalados = {}

        for num, img in imagens_originais.items():
            self.Textos_escalados[num] = pygame.transform.scale(
                img, (nova_largura, nova_altura)
            )

        self.qual_texto = tipo
        self.qual_texto2 = tipo + 4
        self.image = self.Textos_escalados[self.qual_texto]

        self.rect = self.image.get_rect()
        self.rect.topleft = (X_texto, Y_texto)

    def update(self):
        pos_mouse = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos_mouse):
            self.image = self.Textos_escalados[self.qual_texto2]
        else:
            self.image = self.Textos_escalados[self.qual_texto]
