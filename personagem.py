import pygame

class player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/player.png")
        self.image = pygame.transform.scale(self.image, [400, 400])
        self.rect = pygame.Rect(50, 250, 100, 100)

    # Movimentação
    def update(self, *args):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            self.rect.x += 6
        elif keys[pygame.K_a]:
            self.rect.x -= 6
        elif keys[pygame.K_w]:
            self.rect.y -= 6
        elif keys[pygame.K_s]:
            self.rect.y += 6

    # Limite do contato com a tela
        if self.rect.top < 40:
            self.rect.top = 40
        elif self.rect.bottom > 360:
            self.rect.bottom = 360
        if self.rect.right > 1100:
            self.rect.right = 1100
        elif self.rect.left < 0:
            self.rect.left = 0