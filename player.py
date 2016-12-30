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
        self.y = self.get_screen_size()[1] - self.height - 5
        self.__score = 0
        self.__life = 3
        self.__remaining_enemies = 10
        self.__hit = False

    # Getters and setters
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self,value):
        if value > self.get_screen_size()[0] - self.width:
            self.__x = self.get_screen_size()[0] - self.width
        elif value < 0:
            self.__x = 0
        else:
            self.__x = value

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
    def hit(self):
        return self.__hit

    @hit.setter
    def hit(self, value):
        self.__hit = value

    # Behavior
    def move_left(self):
        self.x -= 10

    def move_right(self):
        self.x += 10

    def shoot(self):
        myShoot = Shoot(self.screen)
        myShoot.direction = -1
        myShoot.x = self.x + math.ceil(self.width / 2) - math.ceil(myShoot.width / 2)
        myShoot.y = self.y - myShoot.height - 1
        return myShoot

