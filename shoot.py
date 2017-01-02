import pygame
from game_object import Game_Object

def detectCollision(obj1, obj2):
    if (
                        obj1.x + obj1.width >= obj2.x >= obj1.x and obj1.y + obj1.height >= obj2.y >= obj1.y or obj2.x + obj2.width >= obj1.x >= obj2.x and obj2.y + obj2.height >= obj1.y >= obj2.y):
        return True
    elif (
                        obj1.x + obj1.width >= obj2.x + obj2.width >= obj1.x and obj1.y + obj1.height >= obj2.y >= obj1.y or obj2.x + obj2.width >= obj1.x + obj1.width >= obj2.x and obj2.y + obj2.height >= obj1.y >= obj2.y):
        return True
    elif (
                        obj1.x + obj1.width >= obj2.x >= obj1.x and obj1.y + obj1.height >= obj2.y + obj2.height >= obj1.y or obj2.x + obj2.width >= obj1.x >= obj2.x and obj2.y + obj2.height >= obj1.y + obj1.height >= obj2.y):
        return True
    elif (
                        obj1.x + obj1.width >= obj2.x + obj2.width >= obj1.x and obj1.y + obj1.height >= obj2.y + obj2.height >= obj1.y or obj2.x + obj2.width >= obj1.x + obj1.width >= obj2.x and obj2.y + obj2.height >= obj1.y + obj1.height >= obj2.y):
        return True
    else:
        return False

class Shoot(Game_Object):
    def __init__(self, screen, player=True):
        Game_Object.__init__(self,'shoot', screen)
        self.sprite = (pygame.image.load("imgs/s1.png") if player else pygame.image.load("imgs/s2.png"))
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

    def update_position(self):
        self.y += (self.direction * self.speed)
        '''
        # If it is a player shoot and it is at the end of the screen
        if self.y <= 0:
            objects_on_screen.remove(self)
        # If it is an enemy shoot and it is at the end of the screen
        elif self.y >= self.get_screen_size()[1] - self.height:
            objects_on_screen.remove(self)

        for i in range(len(objects_on_screen) - 1, 0, -1):
            collided = False
            try:
                if objects_on_screen[i].name == 'enemy':
                    if detectCollision(self, objects_on_screen[i]):
                        collided = True
                        player.score += 10
                        player.remaining_enemies -= 1
                        objects_on_screen.pop(i)
                elif objects_on_screen[i].name == 'player':
                    if detectCollision(self, objects_on_screen[i]):
                        collided = True
                        player.life -= 1
                        player.score -= 5
                        if player.life <= 0:
                            objects_on_screen.pop(i)

                if collided:
                    objects_on_screen.remove(self)
            except(IndexError):
                break
        '''
