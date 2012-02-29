#!/usr/bin/env python
"""
tron.py

The simple game of tron with two players.  Press the space bar to start the game.  Player 1 (red) is controlled with WSAD and player 2 (blue) is controlled with the arrow keys.  Once the game is over, press space to reset and then again to restart.  Escape quits the program.
"""

import pygame
from pygame import draw
from pygame.locals import *

# globals
yellow = (255, 255, 0)
purple = (0, 255, 255)

north = (0, -1) 
east = (1, 0)
west = (-1, 0)
south = (0, 1)

tile = 10
width = 80
height = 60

# players
direct1 = east
direct2 = west

pos1 = [(20, 15)]
pos2 = [(60, 40)]


#/bin/bash: :wq: command not found

def move_player(pos, direct):
    newPos = (pos[0] + direct[0], pos[1] + direct[1])
    return newPos

def collision(next_pos, pos1, pos2):
    x,y = next_pos

    if x >= width or x < 0 or y >= height or y < 0:
        return True
    elif next_pos in pos1:
        return True
    elif next_pos in pos2:
        return True
    else:
        return False

# initialze pygame
pygame.init()
screen = pygame.display.set_mode((width * tile, height * tile)) #Voodoo.

done = False
game = False
clock = pygame.time.Clock()
while not done:
    #  input
    for event in pygame.event.get():#more quitting rules.
       if event.type == QUIT:
           done = True
       elif event.type == KEYDOWN and event.key == K_ESCAPE:
           done = True
       elif event.type == KEYDOWN and event.key == K_SPACE:
           game = True

       # Player 1 
       elif event.type == KEYDOWN and event.key == K_w:
           direct1 = north
       elif event.type == KEYDOWN and event.key == K_a:
           direct1 = west
       elif event.type == KEYDOWN and event.key == K_s:
           direct1 = south
       elif event.type == KEYDOWN and event.key == K_d:
           direct1 = east

       # Player 2
       elif event.type == KEYDOWN and event.key == K_UP:
           direct2 = north    
       elif event.type == KEYDOWN and event.key == K_LEFT:
           direct2 = west
       elif event.type == KEYDOWN and event.key == K_DOWN:
           direct2 = south
       elif event.type == KEYDOWN and event.key == K_RIGHT:
           direct2 = east   


    # update
    if game:
       next_pos1 = move_player(pos1[-1], direct1)
       next_pos2 = move_player(pos2[-1], direct2)

       collision1 = collision(next_pos1, pos1, pos2)
       collision2 = collision(next_pos2, pos1, pos2)

       if collision1 or collision2:
            game = False
            if collision1 and collision2:
                print "Both lose"
            elif collision1:
                print "player 2 wins"
            else:
                print "player 1 wins"
       else:
           pos1.append(next_pos1)
           pos2.append(next_pos2)
        
    # draw
    screen.fill((0,0,0))
    for x,y in pos1:
        pygame.draw.rect(screen, purple, (x*tile, y*tile, tile, tile))
    for x,y in pos2:
        pygame.draw.rect(screen, yellow, (x*tile, y*tile, tile, tile))
        
    # refresh
    pygame.display.flip()
    clock.tick(30)
