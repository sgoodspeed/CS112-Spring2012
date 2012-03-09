#!usr/bin/env python

import pygame
from pygame.locals import *
from pygame import draw
import random
pygame.font.init()


##Player attributes
#Colors
red = (255,0,0)
orange = (245,184,0)
blue = (0,46,184)
black = (0,0,0)
backg = (0,14,138)
#Start variables
startR = (20,15)
startB = (60,40)
scoreR = 0
scoreB = 0

##Directions
north = (0,-1)
east = (1,0)
south = (0,1)
west = (-1,0)



##Positions lists
posR = []
posB = []

##Game variables
playing = False
done = False
endGame = False
rounds = 0

##Screen and font variables

TILE = 10
WIDTH = 80
HEIGHT = 60

scoreFont = pygame.font.Font(None,60)

#########################################################################
##Draw functions
def drawPlayers(posR,posB):
    pygame.draw.rect(screen,orange,(posR[0]*TILE,posR[1]*TILE, TILE,TILE))
    pygame.draw.rect(screen,blue,(posB[0]*TILE,posB[1]*TILE,TILE,TILE))

def drawLine(posR,posB):
    for r in posR:
        pygame.draw.rect(screen,orange,(r[0]*TILE,r[1]*TILE,TILE,TILE))
        
    for b in posB:
        pygame.draw.rect(screen,blue,(b[0]*TILE,b[1]*TILE,TILE,TILE))


##Movement and Collision functions
def movePlayer(pos,dir):
    newPos = (pos[0]+dir[0],pos[1]+dir[1])
    return newPos

def collision(pos,posR,posB):
    if pos in posR:
        return True
    elif pos in posB:
        return True
    elif pos[0]<0 or pos[0]>=WIDTH:
        return True
    elif pos[1]>=HEIGHT or pos[1]<0:
        return True

    
##AI Junk and Nonsense
def

##Endgame function
def scoreBoard():
    scoreboard = "Red player score: %i  Blue player score: %i"%(scoreR,scoreB)
    text = scoreFont.render(scoreboard,True,(255,255,255),backg)
    textpos = text.get_rect()
    textpos.centerx = screen.get_rect().centerx
    screen.blit(text,textpos)
    pygame.display.flip()
        


############################################################################
pygame.init()
screen = pygame.display.set_mode((WIDTH*TILE,HEIGHT*TILE))
clock = pygame.time.Clock()

while not done:
    ##Quit and Game Start/Restar controls
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            done = True
        elif event.type ==KEYDOWN and event.key == K_SPACE:
            if rounds == 0:
                directR = east
                directB = west
                posR.append(startR)
                posB.append(startB)
                endGame = False
                playing = True
            else:
                del posR[:]
                del posB[:]
                directR = east
                directB = west
                posR.append(startR)
                posB.append(startB)
                endGame = False
                playing = True
        ##Player Red controls
        if event.type == KEYDOWN and event.key == K_DOWN and directR != north:
            directR = south
        elif event.type == KEYDOWN and event.key ==K_LEFT and directR != east:
            directR = west
        elif event.type == KEYDOWN and event.key == K_RIGHT and directR != west:
            directR = east
        elif event.type == KEYDOWN and event.key == K_UP and directR != south:
                directR = north

        

    ##Game shit
    if playing:
    

        #Moving players
        nextPosR = movePlayer(posR[-1],directR)
        nextPosB = moveComp(posB[-1],directB)

        if collision(nextPosR,posR,posB):
            winner = 1
            scoreB+=1
            playing = False
            endGame = True

        elif collision(nextPosB,posR,posB):
            winner = 2
            scoreR+=1
            playing = False
            endGame = True

        else:
            posR.append(nextPosR)
            posB.append(nextPosB)

        ##Draw functions
        screen.fill((40,40,40))
         
        drawPlayers(posR[-1],posB[-1])
        drawLine(posR,posB)
        ##Refresh
        pygame.display.flip()
        clock.tick(20)

    if endGame:
        rounds+=1
        scoreBoard()

print"Program complete"
pygame.quit()
