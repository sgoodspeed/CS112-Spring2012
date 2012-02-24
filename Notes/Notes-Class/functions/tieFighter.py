#!usr/bin/env python
import random
import pygame
from pygame import draw
from pygame.locals import *


def drawTie(surf, color,pos,size=40):
    x,y = pos
    width = size/8
     #Drawing Tie Fighter here
    draw.rect(surf, color, (x,y,width,size))
    draw.rect(surf, color, (x+size-width,y,width,size))
    draw.rect(surf, color, (x,y+(size-width)/2,size,width))
    draw.circle(surf, color, (x+size/2,y+size/2), size/4)
col=200
dir=1
color=[]
pos=[]
size=[]
pygame.init()
screen = pygame.display.set_mode((800,600))

screen.fill((0,0,15))
done = False
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            done = True
        elif event.type == MOUSEBUTTONDOWN:
            color.append((col,0,col))
            pos.append(pygame.mouse.get_pos())
            size.append(random.randint(20,80))
            
    col+=dir
    if col>255 or col<100:
        dir*=-1
        col+=dir


    screen.fill((0,0,0))
    for i in range(len(color)-1,-1,-1):
        size[i]-=1
        if size[i]<=0:
            size.pop(i)
            color.pop(i)
            pos.pop(i)
        else:
            drawTie(screen, color[i], pos[i], size[i])
    pygame.display.flip()
    clock.tick(10)




pygame.quit()
