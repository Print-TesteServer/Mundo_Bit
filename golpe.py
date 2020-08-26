import pygame

class golpe1(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/golpe1.png")
        self.image = pygame.transform.scale(self.image, [300, 300])
        self.rect = pygame.Rect(0, 0, 10, 10)

        self.speed = 4

    def update(self, *args):
        self.rect.x += self.speed

        if self.rect.left > 1280:
            self.kill()