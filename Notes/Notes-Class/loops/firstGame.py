#!usr/bin/env python
import pygame


#defining a scren size
screen_size = 640,480
#defining a black background
background = 0,0,0

#initiating pygame
pygame.init()
screen = pygame.display.set_mode(screen_size)


#This is a never-ending loop
while True:
    screen.fill(background)
    pygame.display.flip()
    
