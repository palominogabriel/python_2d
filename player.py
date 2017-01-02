import pygame
import math
from shoot import Shoot
from game_object import Game_Object

class Player(Game_Object):
    def __init__(self, screen):
        Game_Object.__init__(self,'player',screen)
        self.sprite = pygame.image.load("imgs/player.png")
        self.width, self.height = self.sprite.get_size()
        self.x = math.ceil(self.get_screen_size()[0] / 2) - math.ceil(self.width / 2)
        self.y = self.get_screen_size()[1] - self.height - 35
        self.__speed = 0.2
        self.__score = 0
        self.__life = 3
        self.__remaining_enemies = 10
        self.__phase = 1

    # Getters and setters
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self,value):
        if value > self.get_screen_size()[0] - math.ceil(self.width / 2):
            self.__x = self.get_screen_size()[0] - math.ceil(self.width / 2)
        elif value < -math.ceil(self.width / 2):
            self.__x = -math.ceil(self.width / 2)
        else:
            self.__x = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        self.__speed = value

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        self.__score = value

    @property
    def life(self):
        return self.__life

    @life.setter
    def life(self, value):
        self.__life = value

    @property
    def remaining_enemies(self):
        return self.__remaining_enemies

    @remaining_enemies.setter
    def remaining_enemies(self, value):
        self.__remaining_enemies = value

    @property
    def phase(self):
        return self.__phase

    @phase.setter
    def phase(self, value):
        self.__phase = value

    # Behavior
    def move_left(self):
        self.x -= 3


    def move_right(self):
        self.x += 3


    def shoot(self):
        myShoot = Shoot(self.screen)
        myShoot.direction = -1
        myShoot.x = self.x + math.ceil(self.width / 2) - math.ceil(myShoot.width / 2)
        myShoot.y = self.y - myShoot.height - 1
        return myShoot


    # continuous player movement while holding down the move keys
    def handle_move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            self.move_right()
        if key[pygame.K_LEFT]:
            self.move_left()
