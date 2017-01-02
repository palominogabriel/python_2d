import pygame
from game_object import Game_Object
from game import Game
import math


class Menu_Screen(Game_Object):
    def __init__(self, screen):
        Game_Object.__init__(self, 'menu_screen', screen)
        self.sprite = pygame.image.load("imgs/Menu.png").convert()
        self.__selection = Selection(self.screen)
        self.__instruction_screen = Instruction_Screen(self.screen)
        self.__game_screen = Game(self.screen)
        self.__game_over_screen = Game_Over_Screen(self.screen)
        self.width, self.height = self.sprite.get_size()

    @property
    def selection(self):
        return self.__selection

    @selection.setter
    def selection(self,value):
        self.__selection = value

    @property
    def instruction_screen(self):
        return self.__instruction_screen

    @instruction_screen.setter
    def instruction_screen(self, value):
        self.__instruction_screen = value

    @property
    def game_screen(self):
        return self.__game_screen

    @game_screen.setter
    def game_screen(self, value):
        self.__game_screen = value

    @property
    def game_over_screen(self):
        return self.__game_over_screen

    @game_over_screen.setter
    def game_over_screen(self, value):
        self.__game_over_screen = value

    def render(self):
        # Clean screen
        self.screen.fill((0, 0, 0))
        # Draw background
        self.screen.blit(self.sprite, self.pos())
        # Draw selection
        self.screen.blit(self.selection.sprite, self.selection.pos())
        # Update screen
        pygame.display.flip()

    def loop(self):
        in_menu = True
        while in_menu:
            self.render()
            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_DOWN:
                        self.selection.state_up()
                    if event.key == pygame.K_UP:
                        self.selection.state_down()
                    if event.key == pygame.K_RETURN:
                        if self.selection.state == self.selection.START:
                            # Start the game
                            in_menu, score = self.game_screen.loop()
                            # Game Over
                            if in_menu:
                                self.game_over_screen.render(score)
                                in_menu = self.game_over_screen.loop()
                        elif self.selection.state == self.selection.INSTRUCTION:
                            # Load the instruction Screen
                            self.instruction_screen.render()
                            in_menu = self.instruction_screen.loop()
                        elif self.selection.state == self.selection.EXIT:
                            # Exit game
                            in_menu = False

                # CLOSE WINDOW
                if event.type == pygame.QUIT:
                    in_menu = False

class Instruction_Screen(Game_Object):
    def __init__(self, screen):
        Game_Object.__init__(self, 'instruction_screen', screen)
        self.sprite = pygame.image.load("imgs/Instructions.png").convert()
        self.width, self.height = self.sprite.get_size()

    def render(self):
        # Clean screen
        self.screen.fill((0, 0, 0))
        # Draw background
        self.screen.blit(self.sprite, self.pos())
        # Update screen
        pygame.display.flip()

    def loop(self):
        in_instruction = True
        window_open = True
        while in_instruction:
            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RETURN:
                        in_instruction = False
                # CLOSE WINDOW
                if event.type == pygame.QUIT:
                    window_open = False
                    in_instruction = False
        return window_open


class Game_Over_Screen(Game_Object):
    def __init__(self, screen):
        Game_Object.__init__(self, 'game_over_screen', screen)
        self.sprite = pygame.image.load("imgs/Game_Over.png").convert()
        self.width, self.height = self.sprite.get_size()
        self.__font = pygame.font.SysFont("Arial Black", 60)

    def render(self, score):
        # Clean screen
        self.screen.fill((0, 0, 0))
        # Draw background
        self.screen.blit(self.sprite, self.pos())
        # Draw Score
        label = self.__font.render(str(score), 1, (0, 0, 0))
        self.screen.blit(label, (math.ceil(self.get_screen_size()[0] / 2) - math.ceil(label.get_size()[0] / 2),
                                 math.ceil(self.get_screen_size()[1] / 2) - 100))
        # Update screen
        pygame.display.flip()

    def loop(self):
        in_game_over = True
        window_open = True
        while in_game_over:
            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RETURN:
                        in_game_over = False
                # CLOSE WINDOW
                if event.type == pygame.QUIT:
                    window_open = False
                    in_game_over = False
        return window_open


class Selection(Game_Object):
    def __init__(self, screen):
        Game_Object.__init__(self, 'menu_selection', screen)
        self.sprite = pygame.image.load("imgs/selection.png")
        self.START = 0
        self.INSTRUCTION = 1
        self.EXIT = 2
        self.__state = self.START
        self.x, self.y = self.get_state_pos(self.state)
        self.width, self.height = self.sprite.get_size()

    # Setters and getters
    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self,value):
        self.__state = value

    def get_state_pos(self, state):
        if state == self.START:
            return 151, 226
        elif state == self.INSTRUCTION:
            return 21, 400
        elif state == self.EXIT:
            return 165, 569
        else:
            return 0, 0

    def update_position(self, state):
        self.x, self.y = self.get_state_pos(state)

    def state_up(self):
        if self.state < 2:
            self.state += 1
            self.update_position(self.state)

    def state_down(self):
        if self.state > 0:
            self.state -= 1
            self.update_position(self.state)

