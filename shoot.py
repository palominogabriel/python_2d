import pygame
from game_object import Game_Object

class Shoot(Game_Object):
    def __init__(self, screen):
        Game_Object.__init__(self,'shoot', screen)
        self.sprite = pygame.image.load("imgs/s1.png")
        self.width, self.height = self.sprite.get_size()
        self.x = 0
        self.y = 0
        self.__direction = -1
        self.__speed = 2

    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self,value):
        if value < -1:
            self.__direction = -1
        elif value > 1:
            self.__direction = 1
        elif value == 0:
            self.__direction = -1
        else:
            self.__direction = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if value <= 0:
            self.__speed = 1
        elif value > 1:
            self.__speed = value