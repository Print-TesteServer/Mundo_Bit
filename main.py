import pygame
import pygame_gui
import random

from pygame.locals import *

from personagem import player
from inimigos import inimigo1


# Criando o Menu
class GameApp():
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((1080, 480), pygame.RESIZABLE)
        self.display.fill([0, 122, 179])
        pygame.display.set_caption("Mundo Bit")
        self.fps = 60
        self.clock = pygame.time.Clock()
        self.run = True

        self.game_state = "menu"
        self.menu_manager = pygame_gui.UIManager((1080, 480))

        # Botões do Menu
        self.Play_button = pygame_gui.elements.UIButton(relative_rect = pygame.Rect
            (((1080/2) - 60, 300/2), (100, 50)), text = "Jogar", manager = self.menu_manager)
        self.Options_button = pygame_gui.elements.UIButton(relative_rect = pygame.Rect
            (((1080 / 2) - 60, 400 / 2), (100, 50)), text = "Opções", manager = self.menu_manager)
        self.Exit_button = pygame_gui.elements.UIButton(relative_rect = pygame.Rect
            (((1080/2) -60, 500/2), (100, 50)), text = "Sair", manager = self.menu_manager)
        self.Help_button = pygame_gui.elements.UIButton(relative_rect = pygame.Rect
            (((1080 / 2) - 40, 600 / 2), (60, 40)), text = "Ajuda", manager = self.menu_manager)

        self.textbox = pygame_gui.elements.UITextBox(html_text = "Versão 0.1", relative_rect = pygame.Rect
            ((0, 475 - 30), (100, 35)), manager = self.menu_manager)

        # Adicionando imputs aos botões
        while self.run:
            self.deltaTime = self.clock.tick(self.fps)
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.run = False
                if self.game_state == "menu":
                    self.menu_manager.process_events(event)

                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == self.Exit_button:
                            self.run = False
                        if event.ui_element == self.Play_button:
                            self.game_state = "game"
                        if event.ui_element == self.Help_button:
                            self.game_state = "help"

                if self.game_state == "menu":
                    self.menu_manager.update(self.deltaTime)

                # Rodando o menu
                if self.game_state == "menu":
                    self.menu_manager.draw_ui(self.display)

                if self.game_state == "help":
                    display = pygame.display.set_mode([1080, 480], pygame.RESIZABLE)
                    pygame.display.set_caption("Mundo Bit")
                    display.fill([230, 255, 255])

                    self.game_state = "help"
                    self.help_manager = pygame_gui.UIManager((1080, 480))

                    self.textbox = pygame_gui.elements.UITextBox(html_text="Bem-Vindo! <br> <br>"
                        "- História: <br>"
                        "Em um mundo muito distante, na era dos 8 e 16 Pixels... Um grande ataque do Rei ogro está em andamento para conquistar o castelo "
                        "humano, apenas você, um humilde mas corajoso aventureiro pode impedir os ogros! <br> <br>"
                        "- Como Jogar: <br> Use [A] e [D] para se mover no  cenário, [W] para Pular, [Espaço] para atacar <br> <br>"
                        "- Apoio: <br> O Jogo tem seu código publicado no Github, caso queira contribuir com o mesmo: https://github.com/Print-TesteServer", relative_rect=pygame.Rect
                        ((30, 30), (1020, 390)), manager=self.help_manager)

                    self.Back_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect
                        (((0) , 430), (100, 50)), text="Voltar", manager=self.help_manager)

                    for event in pygame.event.get():
                        if event.type == QUIT:
                            self.run = False
                        self.help_manager.process_events(event)

                        if event.type == pygame.USEREVENT:
                            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                                if event.ui_element == self.Back_button:
                                    self.game_state = "menu"

                    if self.game_state == "help":
                        self.help_manager.update(self.deltaTime)

                    if self.game_state == "help":
                        self.help_manager.draw_ui(display)

                # Rodando o jogo
                if self.game_state == "game":
                    display = pygame.display.set_mode([1280, 720])
                    pygame.display.set_caption("Mundo Bit")

                    # Objetos
                    objectGroup = pygame.sprite.Group()
                    inimigosGroup = pygame.sprite.Group()

                    # Cenário
                    bg = pygame.sprite.Sprite(objectGroup)
                    bg.image = pygame.image.load("data/TERRENO1.1.png")
                    bg.image = pygame.transform.scale(bg.image, [1280, 720])
                    bg.rect = bg.image.get_rect()

                    personagem = player(objectGroup)
                    inimigo = inimigo1(objectGroup)

                    # Músicas
                    pygame.mixer.music.load("data/Juhani Junkala [Retro Game Music Pack] Level 3.wav")
                    pygame.mixer.music.play(-1)

                    # Sons
                    espadasom = pygame.mixer.Sound("data/sfx_wpn_sword1.wav")

                    # Adicionando Imputs
                    gameLoop = True
                    timer = 0
                    clock = pygame.time.Clock()
                    if __name__ == "__main__":
                        while gameLoop:
                            clock.tick(60)

                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    gameLoop = False
                                elif event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_SPACE:
                                        espadasom.play()

                            # Update
                            objectGroup.update()

                            timer += 1
                            if timer > 30:
                                timer = 0
                                if random.random() < 0.2:
                                    NovoInimigo = inimigo1(objectGroup, inimigosGroup)

                            # Adicionando cor e imagens a Janela
                            objectGroup.draw(display)

                            pygame.display.update()

                pygame.display.update()

if __name__ == "__main__":
    GameApp()