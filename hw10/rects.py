#!/usr/bin/env python
"""
rects.py

Pygame Rectangles
=========================================================
The following section will test your knowledge of how to 
use pygame Rect, arguably pygame's best feature. Define
the following functions and test to make sure they 
work with `python run_tests.py`

Make sure to use the documentation 
http://www.pygame.org/docs/ref/rect.html


Terms:
---------------------------------------------------------
  Point:     an x,y value
               ex:  pt = 3,4

  Polygon:   a shape defined by a list of points
               ex:  poly = [ (1,2), (4,8), (0,3) ]

  Rectangle:  pygame.Rect
"""

import pygame

# 1. poly_in_rect
#      Check to see if the polygon is completely within a given 
#      rectangle.
#
#      returns:  True or False
#pygame.Rect((left, top), (width, height)): return Rect
#
#Rect.collidepoint(x, y): return bool
#Rect.collidepoint((x,y)): return bool

def poly_in_rect(poly, rect):
    "check if polygon is within rectangle"
    #Setting up some variables
    posX=rect[0]
    posY=rect[1]
    width=rect[2]
    height=rect[3]
    countPoints=0
    #Number of points in poly
    polyLen = len(poly)

    #Setting up a list o all points contained within rect
    rectCoords = [(x,y) for x in range(posX,width+posX)
                  for y in range(posY,height+posY)]
    
    #If point is in rectCoords, count+1
    for i in poly:
        if i in rectCoords:
            countPoints+=1
    #If all points inside rect, count == polyLen, return True, else False
    if countPoints == polyLen:
        return True
    else:
        return False
        
# 2. surround_poly
#      Create a rectangle which contains the given polygon.  
#      It should return the smallest possible rectangle 
#      where poly_in_rect returns True.
#
#      returns:  pygame.Rect

def surround_poly(poly):
    "create a rectangle which surounds a polygon"
    lowX = highX = poly[0][0]
    lowY = highY = poly[0][1]
    #Finding highest X value
    for i in range(1,len(poly)-1):
        if poly[i][0] > highX:
            highX = poly[i][0]
    
   

    #Finding lowest X value
    for i in range(1,len(poly)-1):
        if poly[i][0] < lowX:
            lowX = poly[i][0]
    

    #Finding highest Y value
    for i in range(1,len(poly)-1):
        if poly[i][1] > highY:
            highY = poly[i][1]
    
    #Finding lowest Y value
    for i in range(1,len(poly)-1):
        if poly[i][1] < lowY:
            lowY = poly[i][1]
    

    #Setting width and height
    width = abs(highX - lowX)+1
    height = abs(highY - lowY)+1
    return pygame.Rect((lowX,lowY),(width,height))

