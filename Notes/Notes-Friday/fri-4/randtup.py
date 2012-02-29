#!usr/bin/env python

def randTuple3(*bounds):
    "Returns a random n=.-tuple"
    for i,bound in enumerate(bounds):
        if type(bound) == int:
            bounds[i] = [bound]
        return tuple(randrange(*arg) for arg in bounds)

#bounds comes in as a tuple
#Because we're changing things in it we turn it into a list
#if theyre ints
#we return randrange list of random ints, I think???
