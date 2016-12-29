import pygame
from game_object import Game_Object
from random import randint

class Enemy(Game_Object):
    def __init__(self, screen):
        Game_Object.__init__(self,'enemy', screen)
        self.sprite = pygame.image.load("imgs/e" + str(randint(1,8)) + ".png").convert()
        self.width, self.height = self.sprite.get_size()
        self.__speed = 1
        self.__direction = 270 # From 180 to 360
        self.x = randint(0, self.get_screen_size()[0] - self.width)
        self.y = 0

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
        if value < 180:
            self.__direction = 180
        elif value > 360:
            self.__direction = 360
        else:
            self.__direction = value