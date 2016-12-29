import pygame
from menu_screen import Selection
from menu_screen import Menu_GameObject
from menu_screen import Instruction_GameObject
pygame.init()

display_info = pygame.display.Info()

screen = pygame.display.set_mode((640, 704))
pygame.mouse.set_visible(1)

# Assign the screen images to the respective variables
menu_screen = Menu_GameObject()
selection = Selection()
instruction_screen = Instruction_GameObject()

# List of objects to draw
objects_on_screen = list()
objects_on_screen.append(menu_screen)
objects_on_screen.append(selection)

game_over = False
while not game_over:
    # Clean screen
    screen.fill((0,0,0))

    # Draw objects
    for obj in objects_on_screen:
        screen.blit(obj.sprite, obj.pos())

    # Get events
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:

            # MENU SCREEN
            if objects_on_screen.__contains__(menu_screen):
                if event.key == pygame.K_DOWN:
                    objects_on_screen[objects_on_screen.index(selection)].state_up()
                if event.key == pygame.K_UP:
                    objects_on_screen[objects_on_screen.index(selection)].state_down()
                if event.key == pygame.K_RETURN:
                    if objects_on_screen[objects_on_screen.index(selection)].state == 0:
                        # Start the game
                        pass
                    elif objects_on_screen[objects_on_screen.index(selection)].state == 1:
                        # Load the instruction Screen
                        for obj in objects_on_screen:
                            objects_on_screen.remove(obj)
                        objects_on_screen.append(instruction_screen)
                        break
                    else:
                        game_over = True

            # INSTRUCTION SCREEN
            if objects_on_screen.__contains__(instruction_screen):
                if event.key == pygame.K_RETURN:
                    for obj in objects_on_screen:
                        objects_on_screen.remove(obj)

                    objects_on_screen.append(menu_screen)
                    objects_on_screen.append(selection)

        if event.type == pygame.QUIT:
            game_over = True


    pygame.display.flip()


'''
    if pygame.mouse.get_pressed()[0]:
        x, y = pygame.mouse.get_pos()
        print 'x:'+ str(x) + ' y:' + str(y)
'''