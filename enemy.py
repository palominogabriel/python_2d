import pygame
from game_object import Game_Object
from random import randint

class Enemy(Game_Object):
    def __init__(self):
        Game_Object.__init__(self,'enemy')
        self.sprite = pygame.image.load("imgs/e" + str(randint(1,8)) + ".png")
        #TODO: Get the height and width from sprite and assign other atributes