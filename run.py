import pygame
from menu_screen import Menu_Screen

# Initiates the pygame lib
pygame.init()
# Set the window resolution
screen = pygame.display.set_mode((640, 704))

# Set the mouse invisible
pygame.mouse.set_visible(0)

# Menu screen
menu_screen = Menu_Screen(screen)

# Start Menu screen loop
menu_screen.render()
menu_screen.loop()