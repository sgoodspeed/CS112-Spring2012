import pygame
from pygame import draw
from random import randrange
from pygame.locals import *
import math

tie_x, tie_y = 400,300
tie_dx = 1
tie_dy = 1

def draw_tie(surf, pos, color=(255,0,0), size=40):
    "Draws a tie fighter"
    x,y = pos
    
    width = size/8

    draw.rect(surf, color, (x, y, width, size))
    draw.rect(surf, color, (x+(size-width), y, width, size))
    draw.rect(surf, color, (x, y+(size-width)/2, size, width))
    draw.circle(surf, color, (x+size/2, y+size/2), size/4)


def move(x,y,dx,dy,bounds):
    x+=dx
    y+=dy
    if x<bounds.left or x>bounds.right-40:
        dx = -dx
        x+=dx*2
        dx += int(math.copysign(2, dx))
    if y<bounds.top or y>bounds.bottom-40:
        dy= -dy
        y+=dy*2
        dy += int(math.copysign(2,dy))
    return x,y,dx,dy
        
   


pygame.init()
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
done = False
screen_bounds = screen.get_rect()
ties = []
color = []
while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            done = True

    screen.fill((0,0,0))
    tie_x,tie_y,tie_dx,tie_dy=move(tie_x,tie_y,tie_dx,tie_dy,screen_bounds)
    ties.append([tie_x, tie_y])
    color.append(255);
        
    if len(ties) >255:
        ties.pop(0)
        color.pop(0)
    for i in range(len(ties)):
        color[i]-=1
        draw_tie(screen, ties[i],(0,color[i],color[i]))
    
    pygame.display.flip()
    clock.tick(240)
    
print "ByeBye"
pygame.quit()
