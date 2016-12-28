import pygame

pygame.init()

display_info = pygame.display.Info()

print display_info.current_w


screen = pygame.display.set_mode((640, 704))

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.display.flip()