import pygame
import random

class inimigo1(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/inimigo1.png")
        self.image = pygame.transform.scale(self.image, [130, 130])
        self.rect = pygame.Rect(100, 390, 100, 100)

        self.rect.x = 720 + random.randint(720, 720)

        self.speed = 1 + random.random() * 2

    def update(self, *args):
        self.rect.x -= self.speed

        if self.rect.right < 0:
            self.kill()