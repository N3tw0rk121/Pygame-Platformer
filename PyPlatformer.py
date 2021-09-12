import pygame, sys
from pygame.locals import *
pygame.init() #initiates Pygame

clock = pygame.time.Clock()

pygame.display.set_caption("PyPlatformer")

WINDOWS_SIZE = (400, 400)

screen = pygame.display.set_mode(WINDOWS_SIZE,0,32)

player_image = pygame.image.load ("assets\clown_main-300%.png")

moving_right = False
moving_left = False

player_location = [50,50]
player_vetical_momentum = 0

while True: #Loop
    screen.fill((146,244,255))

    screen.blit(player_image,player_location)

    if player_location[1] > WINDOWS_SIZE[1]-player_image.get_height() :
        player_vetical_momentum = -player_vetical_momentum
    else:
        player_vetical_momentum += 0.2
    player_location[1] += player_vetical_momentum
    
    if moving_right == True:
        player_location[0] += 4
    if moving_left == True:
        player_location[0] -= 4


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                moving_right = True
            if event.key == K_LEFT:
                moving_left = True
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                moving_right = False
            if event.key == K_LEFT:
                moving_left = False

    pygame.display.update()
    clock.tick(40)

    input()