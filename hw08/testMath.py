#!usr/bin/env python

import math


def normalize(vec):
    if vec[0]==0 and vec[1]==0 and vec[2]==0:
        print vec
    else:
        for i in range(0,len(vec)-1):
            newVec=[]
            vec[i]=vec[i]+1
            newVec.append(vec[i])
        print newvec

vec1=(0,0,0)
vec2=(1,2,3,4,5)
normalize(vec1)
normalize(vec2)
