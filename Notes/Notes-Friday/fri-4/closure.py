#!usr/bin/env python

import math
from random import randrange


#n is your number OF random numbers, lo and hi is your range. but we are
#UNHAPPY WITH THIS. randTuple2 will fix all our problems

def randTuple(n, lo, hi):
    "Returns a random tuple"
    return tuple (randrange(lo,hi)) for i in range (n)

#This can now take any number of arguments. That is what the asterisk is for.
#If you want to take other specific arguments first, this one with the asterisk has to go at the end

#The asterisk puts all the arguments you pass it into a list, that you call
#the name you give it
def randTuple2(*hi):
    "Returns a random n-tuple"
    return tuple(randrange(i) for i i n (hi)

#If I pass it a tuple with an asterisk in front of it, it automatically
#unpacks it for me. like, randTuple2(*screen_size) where screen_size = (600,800)


#def distance(a,b):
def distance((x1,y1), (x2,y2)):
    x1,y1 = a
    x2,y2 = b
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

#Here we go! you can unpack a list in the argument taking part,
#Rather than assigning your values inside the function once you start. You
#only do this when you sort of know how many elements of a list you will have
