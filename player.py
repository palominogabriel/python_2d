import pygame
import math
from shoot import Shoot
from game_object import Game_Object

PX_MIDDLE = 204
PY_BOTTOM = 582

P_WIDTH = 232
P_HEIGHT = 121

class Player(Game_Object):
    def __init__(self):
        Game_Object.__init__(self,'player')
        self.sprite = pygame.image.load("imgs/player.png")
        self.x = PX_MIDDLE
        self.y = PY_BOTTOM
        self.__width = 232
        self.__height = 121
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
        if value > self.X_MAX - self.width:
            self.__x = self.X_MAX - self.width
        elif value < 0:
            self.__x = 0
        else:
            self.__x = value
            
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
    def height(self, value):
        self.__height = value

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
        self.x -= 1

    def move_right(self):
        self.x += 1

    def shoot(self):
        myShoot = Shoot()
        myShoot.direction = -1
        myShoot.x = self.x + math.ceil(self.width / 2)
        myShoot.y = self.y + math.ceil(myShoot.height / 2)

