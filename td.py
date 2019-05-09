#Import pygame module
import pygame
from pygame.locals import *

pygame.init()

pygame.font.init() 

####game variables####
width = 640     # width of game screen
height = 480    # height of screen

#Create the screen
screen=pygame.display.set_mode((width, height))

f=pygame.font.Font('freesansbold.ttf',32)

GREEN = (0, 168, 42)

BLACK = (0, 0, 0) 

player=pygame.image.load("monkeyrobo.png")

player = pygame.transform.scale(player,[40,40])

player2=pygame.image.load("robomonkey.png")

player2 = pygame.transform.scale(player2,[40,40])

player3=pygame.image.load("bank.png")

player3 = pygame.transform.scale(player3,[40,40])

road=pygame.image.load("roadstreet.png")

road = pygame.transform.scale(road,[150,150])

road2 = pygame.transform.rotate(road,90)

coin=pygame.image.load("gold.png")

coin = pygame.transform.scale(coin,[40,40])

goldc=600

gameClock = pygame.time.Clock()

pos1=[600,320]
MousePressed=False
while (True):

    screen.fill(GREEN)

    screen.blit(player,pos1) 

    screen.blit(player2,[600,370])

    screen.blit(player3,[600,410])

    screen.blit(road,[0,190])

    screen.blit(road,[150,190])

    screen.blit(road,[300,190])

    screen.blit(road,[450,190])

    screen.blit(road,[600,190])

    screen.blit(road2,[450,300])

    screen.blit(road2,[450,360])

    screen.blit(road2,[300,85])

    screen.blit(road2,[300,40])

    screen.blit(road2,[300,0]) 

    screen.blit(coin,[0,10])

    screen.blit(f.render(str(int(goldc)),True,BLACK),[40,10])

    pygame.display.flip()

    gameActive = True

    goldc+=0.05

    if MousePressed==True:
        pos1 = pygame.mouse.get_pos()

    gameClock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:             #The user quit
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            MousePressed=True
        if event.type == pygame.MOUSEBUTTONUP:
            MousePressed=False 

    





