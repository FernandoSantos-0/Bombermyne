# onde ficara o codigo dos obstaculos

import pygame

pygame.init()

class Obstaculos_Caixas(pygame.sprite.Sprite):
    def __init__(self,X,Y,tipo):
        pygame.sprite.Sprite.__init__(self)

        self.blocos = {
            "Caixa_Madeira" :pygame.image.load("Assets/sprites/items/box_unica.png").convert_alpha(),
        }

        self.index = tipo
        self.image = self.blocos[self.index]

        self.rect = self.image.get_rect()
        self.rect.topleft = (X,Y)

    def update(self,grupo_sprites_explosa):
        if  pygame.sprite.spritecollide(self, grupo_sprites_explosa, False):
            self.kill()
             