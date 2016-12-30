import pygame
from game_object import Game_Object
from random import randint
from shoot import Shoot
import math

class Enemy(Game_Object):
    def __init__(self, screen):
        Game_Object.__init__(self,'enemy', screen)
        self.sprite = pygame.image.load("imgs/e" + str(randint(1,8)) + ".png").convert()
        self.width, self.height = self.sprite.get_size()
        self.__speed = 1
        self.__direction = 1 # From 180 to 360
        self.x = randint(0, self.get_screen_size()[0] - self.width)
        self.y = 0
        self.image = pygame.image.load("imgs/e" + str(randint(1,8)) + ".png").convert()
        self.rectBox()
    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self,value):
        if value <= 0:
            self.__speed = 1
        else:
            self.__speed = value

    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, value):
        if value < -1:
            self.__direction = -1
        elif value > 1:
            self.__direction = 1
        elif value == 0:
            self.__direction = 1
        else:
            self.__direction = value

    def shoot(self):
        myShoot = Shoot(self.screen, False)
        myShoot.direction = 1
        myShoot.x = self.x + self.height + math.ceil(self.width / 2) - math.ceil(myShoot.width / 2)
        myShoot.y = self.y + myShoot.height + self.height + 1
        return myShoot