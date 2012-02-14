#!/usr/bin/env python

import pygame
from pygame.locals import *


## COLORS
BLUE = 0, 133, 199
RED = 223, 0, 36
YELLOW = 244, 195, 0
GREEN = 0, 159, 61
BLACK = 0, 0, 0
WHITE = 255, 255, 255

THICKNESS = 20


## MAIN
pygame.init()
screen = pygame.display.set_mode((800, 388))
pygame.display.set_caption("Olympic Rings   [press ESC to quit]")

## Draw
screen.fill(WHITE)

#################################
##  DRAW OLYPIC RINGS HERE

#Black arcs
pygame.draw.arc(screen,BLACK,(290,5,220,220),-1.15,3,THICKNESS)
pygame.draw.arc(screen,BLACK,(290,5,220,220),3.33,4.83,THICKNESS)

#Blue arc
pygame.draw.arc(screen,BLUE,(45,5,220,220),-1.1,4.8,THICKNESS)

#Red arc
pygame.draw.arc(screen,RED,(535,5,220,220),3.33,9.27,THICKNESS)

#Yellow arcs
pygame.draw.arc(screen,YELLOW,(170,105,220,220),2.02,6.15,THICKNESS)
pygame.draw.arc(screen,YELLOW,(170,105,220,220),.17,1.7,THICKNESS)

#Green arcs
pygame.draw.arc(screen,GREEN,(415,105,220,220),2.02,6.16,THICKNESS)
pygame.draw.arc(screen,GREEN,(415,105,220,220),.2,1.7,THICKNESS)

#################################

## Loop
clock = pygame.time.Clock()
done = False
while not done:
    event = pygame.event.poll()
    if event.type == QUIT:
        done = True
    elif event.type == KEYDOWN and event.key == K_ESCAPE:
        done = True

    pygame.display.flip()
    clock.tick(30)

print "ByeBye"
pygame.quit()
