import pygame

class Game:
    def __init__(self):
        self.__background = pygame.image.load("imgs/BG.png")
        self.__font = pygame.font.SysFont("monospace", 15)