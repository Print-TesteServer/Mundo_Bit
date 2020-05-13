import pygame


class José(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/GarotoNinjaTeste.png")
        self.image = pygame.transform.scale(self.image, [100, 100])
        self.rect = pygame.Rect(50, 50, 100, 100)

    def update(self, *args):
        # Lógica
        keys = pygame.key.get_pressed()

        if keys [pygame.K_d]:
            self.rect.x += 1
        elif keys [pygame.K_a]:
            self.rect.x -= 1