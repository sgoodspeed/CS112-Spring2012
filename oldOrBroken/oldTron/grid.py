#!/usr/bin/env python

import pygame
from pygame.locals import *

TILE = 10
trail = [
    (0,0),
    (1,1),
    (1,2),
    (5,10)
]


pygame.init()
screen = pygame.display.set_mode((700,700))

done = False
while not done:

    # draw
    screen.fill((80,80,80))
    for x,y in trail:
        pygame.draw.rect(screen, (0,0,0), (x*TILE, y*TILE, TILE, TILE))

    pygame.display.flip()
