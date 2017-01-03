import pygame
from game_object import Game_Object
from random import randint


class Island(Game_Object):
    def __init__(self, screen):
        Game_Object.__init__(self, 'island', screen)
        self.sprite = pygame.image.load("imgs/i" + str(randint(1, 5)) + ".png")
        self.width, self.height = self.sprite.get_size()
        self.__direction = 1
        self.__island_interval = 2000
        self.x = randint(0, self.get_screen_size()[0] - self.width)
        self.y = -self.height

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

    @property
    def island_interval(self):
        return self.__island_interval

    @island_interval.setter
    def island_interval(self, value):
        self.__island_interval = value

    def update_position(self, player_speed):
        if self.island_interval <= 0:
            self.island_interval = 2000
        self.island_interval -= 1
        self.y += (self.direction * player_speed)
