# Módulos utilitários (colisões, helpers)

import pygame

pygame.init()

def Colisao_janela(sprite, largura_janela, altura_janela):
    if sprite.rect.left < 0:
        sprite.rect.left = 0
    if sprite.rect.right > largura_janela:
        sprite.rect.right = largura_janela
    if sprite.rect.top < 0:
        sprite.rect.top = 0
    if sprite.rect.bottom > altura_janela:
        sprite.rect.bottom = altura_janela
