import pygame, sys
from pygame.locals import *
pygame.init() #initiates Pygame

clock = pygame.time.Clock()

pygame.display.set_caption("PyPlatformer")

WINDOWS_SIZE = (400, 400)

screen = pygame.display.set_mode(WINDOWS_SIZE,0,32)

player_image = pygame.image.load ("assets\clown_main.png")

while True: #Loop

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit
            sys.exit()

    pygame.display.update()
    clock.tick(40)