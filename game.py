import pygame
from game_object import Game_Object
from player import Player
from enemy import Enemy
from island import Island


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

class Game(Game_Object):
    def __init__(self, screen):
        Game_Object.__init__(self,'game_screen',screen)
        self.sprite = pygame.image.load("imgs/BG.png").convert()
        self.__font = pygame.font.SysFont("monospace", 15)
        self.__player = Player(self.screen)
        self.__objects_on_screen = None

    # Getters and Setter
    @property
    def font(self):
        return self.__font

    @font.setter
    def font(self, value):
        self.__font = value

    @property
    def player(self):
        return self.__player

    @player.setter
    def player(self, value):
        self.__player = value

    @property
    def objects_on_screen(self):
        return self.__objects_on_screen

    @objects_on_screen.setter
    def objects_on_screen(self, value):
        self.__objects_on_screen = value

    def render(self):
        # Clean screen
        self.screen.fill((0, 0, 0))
        # Draw objects
        for obj in self.objects_on_screen:
            self.screen.blit(obj.sprite, obj.pos())

        # self.render(str('TESTE'), 1, (255, 255, 255), (0, 0, 0))
        # Update screen
        pygame.display.flip()

    def loop(self):
        self.objects_on_screen = list()
        self.objects_on_screen.append(self)
        self.objects_on_screen.append(self.player)
        self.player.life = 3
        in_game = True
        frame_count = 0
        interval = 0
        while in_game and self.player.life > 0:
            # Count game frames
            frame_count += 1

            # Adds Enemy
            count_enemies_on_screen = 0
            for obj in self.objects_on_screen:
                if obj.name == 'enemy':
                    count_enemies_on_screen += 1
            if count_enemies_on_screen == 0:
                self.objects_on_screen.append(Enemy(self.screen))

            # Adds Ilands on screen
            count_islands_on_screen = 0
            first = True
            for obj in self.objects_on_screen:
                if obj.name == 'island':
                    count_islands_on_screen += 1
                    # Gets the interval of the first island to determine when to add new islands
                    if first:
                        first = False
                        interval = obj.island_interval

            # Add island right above the background
            if count_islands_on_screen < 3 and interval <= 0:
                head = [self.objects_on_screen[0]]
                tail = self.objects_on_screen[1:]
                head.append(Island(self.screen))
                head.extend(tail)
                self.objects_on_screen = head

            print self.objects_on_screen
            # Draw objects on screen
            self.render()

            # Updates the islands
            for i in range(len(self.objects_on_screen) - 1, 0, -1):
                if self.objects_on_screen[i].name == 'island':
                    self.objects_on_screen[i].update_position(self.player.speed)
                    # Remove the island when hits the end of the screen
                    if self.objects_on_screen[i].y >= self.objects_on_screen[i].get_screen_size()[1]:
                        self.objects_on_screen.pop(i)

            # Updates the enemies
            for i in range(len(self.objects_on_screen) - 1, 0, -1):
                if self.objects_on_screen[i].name == 'enemy':
                    # Updates enemy position on screen
                    self.objects_on_screen[i].update_position()
                    # Enemy shoots in the interval
                    if frame_count % self.objects_on_screen[i].shoot_interval == 0:
                        self.objects_on_screen.append(self.objects_on_screen[i].shoot())
                        enemy_shoot_count = 0
                    # Remove enemy if hits the end of the screen
                    if self.objects_on_screen[i].y >= self.objects_on_screen[i].get_screen_size()[1] - self.objects_on_screen[i].height:
                        self.objects_on_screen.pop(i)

            # Updates the shoots
            for i in range(len(self.objects_on_screen)-1,0,-1):
                if self.objects_on_screen[i].name == 'shoot':
                    # Updates shoot position on screen
                    self.objects_on_screen[i].update_position()

                    # Checks shoot collision
                    for j in range(len(self.objects_on_screen) - 1, 0, -1):
                        # Checks if hits an enemy and update score
                        if self.objects_on_screen[j].name == 'enemy':
                            #if self.objects_on_screen[i].colliderect(self.objects_on_screen[j]):
                            if detectCollision(self.objects_on_screen[i], self.objects_on_screen[j]):
                                self.objects_on_screen.pop(i)
                                self.objects_on_screen.pop(j)
                                self.player.score += 10
                                self.player.remaining_enemies -= 1
                        # Checks if hits the player and update score and life
                        if self.objects_on_screen[j].name == 'player':
                            #if self.objects_on_screen[i].colliderect(self.objects_on_screen[j]):
                            if detectCollision(self.objects_on_screen[i], self.objects_on_screen[j]):
                                self.objects_on_screen.pop(i)
                                self.player.life -= 1
                                self.player.score -= 5

                    # If it is a player shoot and it is at the end of the screen
                    if self.objects_on_screen[i].y <= 0:
                        self.objects_on_screen.pop(i)
                    # If it is an enemy shoot and it is at the end of the screen
                    elif self.objects_on_screen[i].y >= self.objects_on_screen[i].get_screen_size()[1] - self.objects_on_screen[i].height:
                        self.objects_on_screen.pop(i)
            # Player movement
            self.player.handle_move()

            # Player shoot
            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        self.objects_on_screen.append(self.player.shoot())

                # CLOSE WINDOW
                if event.type == pygame.QUIT:
                    return False  # Window closed

        # Window not closed
        return True
