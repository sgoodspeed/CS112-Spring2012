#!usr/bin/env python
#voodoo
import pygame
from pygame.locals import *

#defining a scren size
screen_size = 640,480
#defining a black background
background = 0,0,0

#initiating pygame
pygame.init()
screen = pygame.display.set_mode(screen_size)

done=False
while not done:
    #This is looking to see ifyou click or do something, any input
    event=pygame.event.poll()
#Looks for the quit button to be clicked
    if event.type == QUIT:
        done=True
    #Looks for the escape key to be clicked
    elif event.type == KEYDOWN and event.key == K_ESCAPE:
        done = True
    elif event.type == KEYDOWN and event.key == K_w:
        background=255,255,255
    elif event.type ==  MOUSEBUTTONDOWN:
        #Prints the mouse position
        print "Mouse",pygame.mouse.get_pos()
    
    screen.fill(background)
    pygame.display.flip()

print "Bye bye!"
pygame.quit()
