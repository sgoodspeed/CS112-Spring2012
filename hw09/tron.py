#!/usr/bin/env python




"""
tron.py

The simple game of tron with two players.  Press the space bar to start the
game.  Player 1 (red) is controlled with WSAD and player 2 (blue) is
controlled with the arrow keys.  Once the game is over, press space to reset
and then again to restart.  Escape quits the program.
"""

import pygame
from pygame.locals import *
from pygame import draw
import random


def drawSplode(x,y):
    pygame.draw.circle(screen,(255,0,0),(x,y),10,0)
                

def drawLine(posX,posY,color):
    for pos in zip(posX,posY):
        pygame.draw.circle(screen,color,pos,3,0)
    
def checkFuncs(cX,cY,posRX,posRY,posBX,posBY):
    pRTrail = zip(posRX,posRY)
    pBTrail = zip(posBX,posBY)
    if (cX,cY) in pRTrail:
        drawSplode(cX,cY)
    if (cX,cY) in pBTrail:
        drawSplode(cX,cY)
    
w = h =700
rX = rY = 250
bX = bY = 450

north = (0,-1)
east = (1,0)
south = (0,1)
west = (-1,0)

pygame.init()
screen = pygame.display.set_mode((w,h))

playerPosRX = []
playerPosRY = []
playerPosBX = []
playerPosBY = []

orange = (245,184,0)
blue = (0,46,184)

done = False
win = 0
##1 for Red win, 2 for blue win
clock = pygame.time.Clock()
playing = False
while not done:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            done = True
        if event.type == KEYDOWN and event.key == K_SPACE:
            playing = True
            playerPosRX.insert(0,rX)
            playerPosRY.insert(0,rY)
            directR = east
            playerPosBX.insert(0,bX)
            playerPosBY.insert(0,bY)
            directB = west
    if playing:
        if win == 0:
        ##Player Red controls
            if event.type == KEYDOWN and event.key == K_DOWN:
                directR = south
            elif event.type == KEYDOWN and event.key ==K_LEFT:
                directR = west
            elif event.type == KEYDOWN and event.key == K_RIGHT:
                directR = east
            elif event.type == KEYDOWN and event.key == K_UP:
                directR = north
        ##Player Blue controls
            if event.type == KEYDOWN and event.key == K_s:
                    directB = south
            elif event.type == KEYDOWN and event.key ==K_a:
                    directB = west
            elif event.type == KEYDOWN and event.key == K_d:
                    directB = east
            elif event.type == KEYDOWN and event.key == K_w:
                    directB = north
       
            
        
        ##Draw bike
        pygame.draw.circle(screen,orange,(playerPosRX[0],playerPosRY[0]),5,0)
        pygame.draw.circle(screen,blue,(playerPosBX[0],playerPosBY[0]),5,0)

        ##Drawing line behind bike
        drawLine(playerPosRX,playerPosRY,orange)
        drawLine(playerPosBX,playerPosBY,blue)

        ##Checking for collisions
        checkFuncs(playerPosRX[0],playerPosRY[0],playerPosRX[1:],playerPosRY[1:],playerPosBX[1:],playerPosBY[1:])
        checkFuncs(playerPosBX[0],playerPosBY[0],playerPosRX[:1],playerPosRY[1:],playerPosBX[1:],playerPosBY[1:])
        
        changeRX,changeRY = directR
        changeBX,changeBY = directB
    ##Change in Red X
        newPosRX = playerPosRX[0]+changeRX
        playerPosRX.insert(0,newPosRX)
        
    ##Change in Red Y
        newPosRY = playerPosRY[0]+changeRY
        playerPosRY.insert(0,newPosRY)
        
        ##Change in Blue X
        newPosBX = playerPosBX[0]+changeBX
        playerPosBX.insert(0,newPosBX)
        
        ##Change in Blue Y
        newPosBY = playerPosBY[0]+changeBY
        playerPosBY.insert(0,newPosBY)
        
        
        
        
        


        pygame.display.flip()
        clock.tick(100)



print "Program Complete"
pygame.quit()

