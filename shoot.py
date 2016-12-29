import pygame
import math
from game_object import Game_Object


class Shoot(Game_Object):
    def __init__(self):
        Game_Object.__init__(self,'shoot')
        self.__sprite = pygame.image.load("imgs/s1.png")
        self.__width = 10
        self.__height = 35
        self.x = math.ceil(self.X_MAX / 2) - math.ceil(self.__width / 2)
        self.y = self.Y_MAX - self.__height
        self.__direction = -1
        self.__speed = 2

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self,value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self,value):
        self.__height = value

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