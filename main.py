import pygame
import pygame_gui
import random

from pygame.locals import *

from animation import *

from personagem import player
from inimigos import inimigo1
from inimigos import inimigo2
from golpe import golpe1


# Criando o Menu
class GameApp():
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((1080, 480), pygame.RESIZABLE)
        pygame.display.set_caption("Mundo Bit")
        self.fps = 60
        self.clock = pygame.time.Clock()
        self.run = True

        # STATES
        self.game_state = "menu"

        # MANAGERS
        self.menu_manager = pygame_gui.UIManager((1080, 480))
        self.options_manager = pygame_gui.UIManager((1080, 480))
        self.help_manager = pygame_gui.UIManager((1080, 480))

        # Elementos do menu manager
        self.Play_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect
        ((int((1080 / 2) - 60), int(300 / 2)), (100, 50)), text="Jogar", manager=self.menu_manager)
        self.Options_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect
        ((int((1080 / 2) - 60), int(400 / 2)), (100, 50)), text="Opções", manager=self.menu_manager)
        self.Exit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect
        ((int((1080 / 2) - 60), int(500 / 2)), (100, 50)), text="Sair", manager=self.menu_manager)
        self.Help_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect
        ((int((1080 / 2) - 40), int(600 / 2)), (60, 40)), text="Ajuda", manager=self.menu_manager)

        self.textbox = pygame_gui.elements.UITextBox(html_text="Versão 0.1", relative_rect=pygame.Rect
        ((0, 475 - 30), (100, 35)), manager=self.menu_manager)

        # Elementos do help manager
        self.textbox = pygame_gui.elements.UITextBox(html_text="Bem-Vindo! <br> <br>"
            "- História: <br>"
            "Em um mundo muito distante, na era dos 8 e 16 Pixels... Um grande ataque do Rei ogro está em andamento para conquistar o castelo "
            "humano, apenas você, um humilde mas corajoso aventureiro e seu canhão, podem impedir os ogros! <br> <br>"
            "- Como Jogar: <br> Use [A] e [D] para se mover na horizontal, [W] e [S] para se mover na vertical, [Espaço] para atacar e NÃO!, você não anda na diagonal... <br> <br>"
            "- Apoio: <br> O Jogo tem seu código publicado no Github, caso queira contribuir com o mesmo: https://github.com/Print-TesteServer",
            relative_rect=pygame.Rect
            ((30, 30), (1020, 390)), manager=self.help_manager)

        self.Back_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect
        (((0), 430), (100, 50)), text="Voltar", manager=self.help_manager)

        # Elementos do options manager
        self.Back2_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect
        (((0), 430), (100, 50)), text="Voltar", manager=self.options_manager)

        self.textbox = pygame_gui.elements.UITextBox(html_text="Em construção", relative_rect=pygame.Rect
        ((50, 50), (980, 380)),manager=self.options_manager)

        # Slider
        self.slider = pygame_gui.elements.UIHorizontalSlider(
            relative_rect=pygame.Rect(((1080 / 2) - 40, 480 / 2 - 100), (200, 30)),
            start_value=0.5,
            value_range=(0.0, 1.0),
            manager=self.options_manager
        )
        self.label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(((1080 / 2) - 90, 480 / 2 - 100), (50, 30)),
            text="Som",
            manager=self.options_manager
        )
        self.label2 = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(((1080 / 2) + 160, 480 / 2 - 100), (50, 30)),
            text="Text",
            manager=self.options_manager
        )
        self.slider2 = pygame_gui.elements.UIHorizontalSlider(
            relative_rect=pygame.Rect(((1080 / 2) - 40, 480 / 2 - 60), (200, 30)),
            start_value=0.5,
            value_range=(0.0, 1.0),
            manager=self.options_manager
        )
        self.slider3 = pygame_gui.elements.UIHorizontalSlider(
            relative_rect=pygame.Rect(((1080 / 2) - 40, 480 / 2 - 20), (200, 30)),
            start_value=0.5,
            value_range=(0, 1),
            manager=self.options_manager
        )

        self.labe3 = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(((1080 / 2) - 100, 480 / 2 - 60), (50, 30)),
            text="Idioma",
            manager=self.options_manager
        )

        self.label4 = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(((1080 / 2) + 160, 480 / 2 - 60), (50, 30)),
            text="Text",
            manager=self.options_manager
        )

        self.golpe = Animation([
                "data/golpe1.png"
        ], 0.5)

        # Rodando o jogo
        while self.run:
            self.deltaTime = self.clock.tick(self.fps)
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.run = False
                if self.game_state == "menu":
                    self.menu_manager.process_events(event)
                elif self.game_state == "options":
                    self.options_manager.process_events(event)
                elif self.game_state == "help":
                    self.help_manager.process_events(event)

                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if self.game_state == "menu":
                            if event.ui_element == self.Exit_button:
                                self.run = False
                            if event.ui_element == self.Play_button:
                                self.game_state = "game"
                            if event.ui_element == self.Options_button:
                                self.game_state = "options"
                            if event.ui_element == self.Help_button:
                                self.game_state = "help"
                        if self.game_state == "help":
                            if event.ui_element == self.Back_button:
                                self.game_state = "menu"
                        if self.game_state == "options":
                            if event.ui_element == self.Back2_button:
                                self.game_state = "menu"

                # Slider
                if self.game_state == "options":
                    slider_value = str(self.slider.get_current_value())[:3]
                    self.label2.set_text(slider_value)
                    self.options_manager.draw_ui(self.display)

                pygame.display.update()

            if self.game_state == "menu":
                self.display.fill([0, 122, 179])  # FUNDO DO MENU
                self.menu_manager.update(self.deltaTime)
                self.menu_manager.draw_ui(self.display)

            elif self.game_state == "options":
                self.display.fill([0, 122, 179])  # FUNDO DO OPTIONS
                self.options_manager.update(self.deltaTime)
                self.options_manager.draw_ui(self.display)

            elif self.game_state == "help":
                self.display.fill([0, 122, 179])  # FUNDO DO HELP
                self.help_manager.update(self.deltaTime)
                self.help_manager.draw_ui(self.display)

            elif self.game_state == "game":
                display = pygame.display.set_mode([1280, 720])
                display.blit(self.golpe.image, (200,300))
                pygame.display.set_caption("Mundo Bit")

                # Objetos
                objectGroup = pygame.sprite.Group()
                inimigosGroup = pygame.sprite.Group()
                golpeGroup = pygame.sprite.Group()

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
                            if event.type == QUIT:
                                gameLoop = False
                                self.run = False
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_SPACE:
                                    timer += 1
                                    if timer > 19:
                                        timer = 0
                                        espadasom.play()
                                        novogolpe = golpe1(objectGroup, golpeGroup)
                                        novogolpe.rect.center = personagem.rect.center
                                        novogolpe.rect.right = personagem.rect.right

                        # Update
                        objectGroup.update()

                        timer += 1
                        if timer > 30:
                            timer = 0
                            if random.random() < 0.4:
                                NovoInimigo = inimigo1(objectGroup, inimigosGroup)

                        timer += 1
                        if timer > 30:
                            timer = 0
                            if random.random() < 0.2:
                                NovoInimigo2 = inimigo2(objectGroup, inimigosGroup)

                        collisions = pygame.sprite.spritecollide(personagem, inimigosGroup, False, pygame.sprite.collide_mask)

                        if collisions:
                            gameLoop = False

                        hits = pygame.sprite.groupcollide(golpeGroup, inimigosGroup, True, True, pygame.sprite.collide_mask)

                        # Adicionando cor e imagens a Janela
                        objectGroup.draw(display)

                        self.golpe.update()
                        pygame.display.update()

            pygame.display.update()

if __name__ == "__main__":
    GameApp()