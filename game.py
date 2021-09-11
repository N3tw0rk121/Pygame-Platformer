import pygame, sys
from pygame.locals import *
pygame.init() #initiates Pygame

WINDOWS_SIZE = (720, 1080)

screen = pygame.display.set_mode(WINDOWS_SIZE,0,32)

while True: #Loop

    for event in pygame.event.get():
        if event.type == QUIT
            pygame.quit
            sys.exit()

    pygame.display.update()