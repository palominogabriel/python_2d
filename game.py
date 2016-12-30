import pygame
from game_object import Game_Object
from player import Player
from enemy import Enemy

class Game(Game_Object):
    def __init__(self, screen):
        Game_Object.__init__(self,'game_screen',screen)
        self.sprite = pygame.image.load("imgs/BG.png").convert()
        self.__font = pygame.font.SysFont("monospace", 15)
        self.__player = Player(self.screen)
        self.__objects_on_screen = list()
        self.objects_on_screen.append(self)
        self.objects_on_screen.append(self.player)

    @property
    def objects_on_screen(self):
        return self.__objects_on_screen

    @objects_on_screen.setter
    def objects_on_screen(self, value):
        self.__objects_on_screen = value

    @property
    def player(self):
        return self.__player

    @player.setter
    def player(self, value):
        self.__player = value

    def render(self):
        # Clean screen
        self.screen.fill((0, 0, 0))
        # Draw objects
        for obj in self.objects_on_screen:
            self.screen.blit(obj.sprite, obj.pos())
        # Update screen
        pygame.display.flip()

    def loop(self):
        in_game = True
        while in_game and self.player.life > 0:
            # Updates the shoots positions
            for obj in self.objects_on_screen:
                if obj.name == 'shoot':
                    obj.y += (obj.direction * obj.speed)
                    # If it is a player shoot and it is at the end of the screen
                    if obj.y <= 0:
                        self.objects_on_screen.remove(obj)
                    # If it is an enemy shoot and it is at the end of the screen
                    elif obj.y >= obj.get_screen_size()[1] - obj.height:
                        self.objects_on_screen.remove(obj)
                    # Checks shoot collision
                    for obj2 in self.objects_on_screen:
                        # Checks if hits an enemy and update score
                        if obj2.name == 'enemy':
                            if obj.colliderect(obj2):
                                self.objects_on_screen.remove(obj2)
                                self.player.score += 10
                                self.player.remaining_enemies -= 1
                        # Checks if hits the player and update score and life
                        if obj2.name == 'player':
                            if obj.colliderect(obj2):
                                self.player.life -= 1
                                self.player.score -= 5

            self.render()
            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.player.move_left()
                    elif event.key == pygame.K_RIGHT:
                        self.player.move_right()
                    elif event.key == pygame.K_SPACE:
                        self.objects_on_screen.append(self.player.shoot())

                # CLOSE WINDOW
                if event.type == pygame.QUIT:
                    in_game = False
