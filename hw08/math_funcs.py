#!/usr/bin/env python

import math

# Distance formula
#   calculate a function called "distance" to calculate the distance between two points.
#   http://www.purplemath.com/modules/distform.htm
#   ex: 
#      >>> distance((0,0), (3,4))
#      5

def distance(a, b):
    ax,ay = a
    bx,by = b

    return math.sqrt((bx-ax)**2 + (by-ay)**2)
    


# ADVANCED
# Normalizing Vectors
#   normalize a vector of length N.  If given all zeros, just spit back the same vector
#   http://www.fundza.com/vectors/normalize/index.html

#   ex:
#     >>> normalize((1,1))
#     [0.70710678118654746, 0.70710678118654746]
#     >>> normalize([0,0,0])
#     [0,0,0]
#     >>> normalize([1,1,1,1])
#     [0.25, 0.25, 0.25, 0.25]

def normalize(vec):
    if vec[0]==0 and vec[1]==0 or vec[0]==0 and vec[1]==0 and vec[2]==0:
        print vec
    elif len(vec)==3:
        lX=float(vec[0]*vec[0])
        lY=float(vec[1]*vec[1])
        lZ=float(vec[2]*vec[2])
        length = float(math.sqrt(lX+lY+lZ))
        
        norm = []
        
        normX = float(vec[0]/length)
        norm.append(normX)
        normY = float(vec[1]/length)
        norm.append(normY)
        normZ = float(vec[2]/length)
        norm.append(normZ)
        print norm
    elif len(vec)==2:
        lX=float(vec[0]*vec[0])
        lY=float(vec[1]*vec[1])
        length=float(math.sqrt(lX+lY))
        
        norm =[]
        
        normX = float(vec[0]/length)
        norm.append(normX)
        normY = float(vec[1]/length)
        norm.append(normY)
        print norm

