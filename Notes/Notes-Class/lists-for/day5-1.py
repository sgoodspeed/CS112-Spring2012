#!usr/bin/env python
import pygame
from pygame.locals import *
#These are just our settings
BLACK=0,0,0
RED=255,0,0
BLUE=0,0,255
GREEN=0,255,0
PUR=255,0,255
size=400,400
#Initializing stuff
pygame.init
screen=pygame.display.set_mode(size)

done=False
sep=8
pygame.key.set_repeat(100,100)
while not done:
    for event in pygame.event.get():
        if event.type==QUIT:
            done=True
        elif event.type==KEYDOWN and event.key==K_ESCAPE:
            done=True
        elif event.type==KEYDOWN and event.key==K_UP:
            sep+=1
        elif event.type==KEYDOWN and event.key==K_DOWN:
             sep-=1
    
    ##Draw
    screen.fill(BLACK)
    for i in range(0,400,sep):
       pygame.draw.line(screen,RED,(0,i),(i,399))
       pygame.draw.line(screen,BLUE,(i,399),(399,399-i))
       pygame.draw.line(screen,GREEN,(399,399-i),(399-i,0))
       pygame.draw.line(screen,PUR,(399-i,0),(0,i))
      

    pygame.display.flip()


pygame.quit()

  #pygame.draw.line(Surface,color,start_pos,end_pos,width=1)
  #(Width is defaulted to 1, if you don't put in somehting it stays 1
