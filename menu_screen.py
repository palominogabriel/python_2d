import pygame
import screen

# State position constants
X_0 = 151
Y_0 = 226

X_1 = 21
Y_1 = 400

X_2 = 165
Y_2 = 569

class Menu_Screen(screen.Screen):
    def __init__(self):
        screen.Screen.__init__(self,'menu_screen')
        self.sprite = pygame.image.load("imgs/Menu.png")

class Instruction_Screen(screen.Screen):
    def __init__(self):
        screen.Screen.__init__(self,'instruction_screen')
        self.sprite = pygame.image.load("imgs/Instructions.png")

class Selection(screen.Screen):

    def __init__(self):
        screen.Screen.__init__(self,'menu_selection')
        self.sprite = pygame.image.load("imgs/selection.png")
        self.__state = 0
        self.x = X_0
        self.y = Y_0

    # Setters and getters
    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self,value):
        self.__state = value

    def update_position(self, state):
        if state == 0:
            self.x = X_0
            self.y = Y_0
        elif state == 1:
            self.x = X_1
            self.y = Y_1
        else:
            self.x = X_2
            self.y = Y_2

    def state_up(self):
        if self.state < 2:
            self.state += 1
            self.update_position(self.state)

    def state_down(self):
        if self.state > 0:
            self.state -= 1
            self.update_position(self.state)

