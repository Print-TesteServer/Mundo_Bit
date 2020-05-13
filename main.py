import pygame
from personagem import José

# Inicializando o Pygame e criando uma Janela
pygame.init()
display = pygame.display.set_mode([1080,720])
pygame.display.set_caption("Mundo Bit")

# Objetos
objectGroup = pygame.sprite.Group()

personagem = José(objectGroup)


# Músicas
pygame.mixer.music.load("data/Juhani Junkala [Retro Game Music Pack] Level 3.wav")
pygame.mixer.music.play(-1)

# Sons
espada = pygame.mixer.Sound("data/sfx_wpn_sword1.wav")


# Adicionando Imputs
gameLoop = True
if __name__ == "__main__":
    while gameLoop:
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                gameLoop = False
            elif event.type ==pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    espada.play()
        # Update

        objectGroup.update()

        # Adicionando cor e imagens a Janela
        display.fill([19, 173, 235])

        objectGroup.draw(display)

        pygame.display.update()