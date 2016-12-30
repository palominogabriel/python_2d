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
        self.objects_on_screen = list()
        self.objects_on_screen.append(self)
        self.objects_on_screen.append(self.player)

    #@property
    #def objects_on_screen(self):
    #    return self.__objects_on_screen

    #@objects_on_screen.setter
    #def objects_on_screen(self, value):
    #    self.__objects_on_screen = value

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
            count = 0
            for obj in self.objects_on_screen:
                if obj.name == 'enemy':
                    count += 1

            if count == 0:
                self.objects_on_screen.append(Enemy(self.screen))

            print self.objects_on_screen

            # Draw objects on screen
            self.render()

            # Updates the shoots positions
            for i in range(len(self.objects_on_screen) - 1, 0, -1):
                if self.objects_on_screen[i].name == 'enemy':
                    # Updates enemy position on screen
                    self.objects_on_screen[i].update_position()
                    # Remove enemy if hits the end of the screen
                    if self.objects_on_screen[i].y >= self.objects_on_screen[i].get_screen_size()[1] - self.objects_on_screen[i].height:
                        self.objects_on_screen.pop(i)

            # Updates the shoots positions
            for i in range(len(self.objects_on_screen)-1,0,-1):
                if self.objects_on_screen[i].name == 'shoot':
                    # Updates shoot position on screen
                    self.objects_on_screen[i].update_position()

                    # Checks shoot collision
                    for j in range(len(self.objects_on_screen) - 1, 0, -1):
                        # Checks if hits an enemy and update score
                        if self.objects_on_screen[j].name == 'enemy':
                            if self.objects_on_screen[i].colliderect(self.objects_on_screen[j]):
                                self.objects_on_screen.pop(j)
                                self.player.score += 10
                                self.player.remaining_enemies -= 1
                        # Checks if hits the player and update score and life
                        if self.objects_on_screen[j].name == 'player':
                            if self.objects_on_screen[i].colliderect(self.objects_on_screen[j]):
                                self.player.life -= 1
                                self.player.score -= 5

                    # If it is a player shoot and it is at the end of the screen
                    if self.objects_on_screen[i].y <= 0:
                        self.objects_on_screen.pop(i)
                    # If it is an enemy shoot and it is at the end of the screen
                    elif self.objects_on_screen[i].y >= self.objects_on_screen[i].get_screen_size()[1] - self.objects_on_screen[i].height:
                        self.objects_on_screen.pop(i)



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
