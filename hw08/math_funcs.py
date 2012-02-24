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
    check = 0
    for i in vec:
        check+=i
    if check == 0:
        print vec
        return vec
    leng1 = [i**2 for i in vec]
    leng2 = 0
    for i in leng1:
        leng2+=i
    leng3 = float(math.sqrt(leng2))
    norms = [i/leng3 for i in vec]
    print norms
    return norms


