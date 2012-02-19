#!usr/bin/env python
#NOTE 1



import pygame#NOTE 2
from pygame import gfxdraw
from pygame.locals import *#NOTE 3

#FUNCTIONS FUNCTIONS AHHH FUNCTION HAPPENING RIGHT HERE
SCREEN_SIZE = 640,480 #
FPS = 30

#player = Rect(0,0,16,16)

def draw(surf):
    surf.fill((80,80,80))
    
    x,y = pygame.mouse.get_pos()
    gfxdraw.filled_circle(surf, x, y, 8, (0,0,0))
    gfxdraw.filled_circle(surf, x, y, 5, (0,0,255))

#NOTE 4
def run():
    pygame.init()
#NOTE 5
    screen =  pygame.display.set_mode(SCREEN_SIZE, DOUBLEBUF|HWSURFACE)
    pygame.mouse.set_visible(False)
    #NOTE 6
    clock = pygame.time.Clock()#NOTE 7

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == QUIT:
                done = True
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                done = True
        
        draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":#NOTE 8
    run()
    print "Byebye"

pygame.quit()


#NOTE 1
#This thing up here is a fancy unix/linux thing that says if this file is executable, run it with this program. It has to be the first line.

#NOTE 2
#Loads the pygame module

#NOTE 3
#Loads in all those nice ittle like, all caps words we use a lot

#NOTE 4
#Creates a main function that runs our game, that lets us make more functions

#NOTE 5
#If you don't put tis in pygame won't work. it initializes pygame

#NOTE 6
#You have a few more choices than this, but eh, sets the screen up and all

#NOTE 7
#Allows you to track how much time has passed in the game, allows you to pause/resume and things like that. Most important function is tick, which automatically makes the loop 'sleep', which keeps the program from running faster than the fps

#NOTE 8
#whichever python game you are running, it gets the name "__main__". this allows you to run a single module of pygame as a single little entity.
