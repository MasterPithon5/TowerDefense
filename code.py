#Import pygame module
import pygame
from pygame.locals import *

pygame.init()

####game variables####
width = 640     # width of game screen
height = 480    # height of screen

#Create the screen
screen=pygame.display.set_mode((width, height))

GREEN = (0, 168, 42) 

player=pygame.image.load("bluecirclereplace.png")

player = pygame.transform.scale(player,[20,20])

player = pygame.image.load(
gameClock = pygame.time.Clock()
while (True):

    screen.fill(GREEN)

    screen.blit(player,[600,320])

    pygame.display.flip()

    gameActive = True

    gameClock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:             #The user quit
            pygame.quit()

