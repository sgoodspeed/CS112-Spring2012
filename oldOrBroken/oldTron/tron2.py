#!usr/bin/env python

import pygame
from pygame.locals import *
from pygame import draw
import random
pygame.font.init()

#Player attributes
red = (255,0,0)
orange = (245,184,0)
blue = (0,46,184)
black = (0,0,0)
backg = (0,14,138)

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
TILE = 10
WIDTH = 80
HEIGHT = 60
startR = (20,15)
startB = (60,40)
scoreR = 0
scoreB = 0
again = False
stillGoing = True
winner = 0


def drawPlayers(posR,posB):
    pygame.draw.rect(screen,orange,(posR[0]*TILE,posR[1]*TILE, TILE,TILE))
    pygame.draw.rect(screen,blue,(posB[0]*TILE,posB[1]*TILE,TILE,TILE))

def drawLine(posR,posB):
    for r in posR:
        pygame.draw.rect(screen,orange,(r[0]*TILE,r[1]*TILE,TILE,TILE))
        
    for b in posB:
        pygame.draw.rect(screen,blue,(b[0]*TILE,b[1]*TILE,TILE,TILE))
        


def collision(pos,posR,posB):
    if pos in posR:
        return True
    elif pos in posB:
        return True
    elif pos[0]<0 or pos[0]>=WIDTH:
        return True
    elif pos[1]>=HEIGHT or pos[1]<0:
        return True
    

def movePlayer(pos,dir):
    newPos = (pos[0]+dir[0],pos[1]+dir[1])
    return newPos



def endGame(win,scoreR,scoreB):
    if win == 1:
        print "Made it here 1"
        
        text = scoreFont.render(scoreboard, True, (255,255,255))
        loc = text.get_rect()
        loc.center = (40*TILE, 30*TILE)
        screen.blit(text,loc)
        
        win = 0
    if win == 2:
        print "Made it here 2"
        scoreboard = "Red player score: %i  Blue player score: %i"%(scoreR,scoreB)
        text = scoreFont.render(scoreboard, True, (0,0,0), backg)
        loc = text.get_rect()
        loc.center = bounds.center
        screen.blit(text,loc)
        
        win = 0
    return True



pygame.init()
screen = pygame.display.set_mode((WIDTH*TILE,HEIGHT*TILE))
bounds = screen.get_rect
clock = pygame.time.Clock()

while not done:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            done = True
        elif event.type ==KEYDOWN and event.key == K_SPACE:
            
            directR = east
            directB = west
            posR.append(startR)
            posB.append(startB)
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

        ##Player Blue controls
        if event.type == KEYDOWN and event.key == K_s and directB != north:
            directB = south
        elif event.type == KEYDOWN and event.key ==K_a and directB != east:
            directB = west
        elif event.type == KEYDOWN and event.key == K_d and directB != west:
            directB = east
        elif event.type == KEYDOWN and event.key == K_w and directB != south:
            directB = north
        if event.type ==KEYDOWN and event.key == K_RETURN:
            if again:
        
                del posR[:]
                del posB[:]
                directR = east
                directB = west
                posR.append(startR)
                print scoreR,scoreB
                posB.append(startB)
                stillGoing = True
                playing = True

    
    if playing:
    

        # update
        nextPosR = movePlayer(posR[-1],directR)
        nextPosB = movePlayer(posB[-1],directB)
        if collision(nextPosR,posR,posB):
            
            winner = 1
            scoreB+=1
            stillGoing = False
            
        elif collision(nextPosB,posR,posB):
            ##PROBLEM 2
            
            winner = 2
            scoreR+=1
            stillGoing = False
        else:
            posR.append(nextPosR)
            posB.append(nextPosB)
                
        # draw
        screen.fill((40,40,40))
        
        drawPlayers(posR[-1],posB[-1])
        drawLine(posR,posB)
        elif winner == 1:
            drawPlayers(posR[-1],posB[-1])
            drawLine(posR,posB)
            pygame.draw.ellipse(screen,red,(nextPosR[0]*TILE,nextPosR[1]*TILE,TILE*4,TILE*4))
            
            playing = False
        elif winner == 2:
            drawPlayers(posR[-1],posB[-1])
            drawLine(posR,posB)
            pygame.draw.ellipse(screen,red,(nextPosB[0]*TILE,nextPosB[1]*TILE,TILE*4,TILE*4))
            
            playing = False
        ##Refresh
        pygame.display.flip()
        clock.tick(20)
    
    again = endGame(winner,scoreR,scoreB)
        
    
        
        

print"Program complete"
pygame.quit()
