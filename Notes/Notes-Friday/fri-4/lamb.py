#!usr/bin/env python

#lambda is for unnamed functions. check this out dude


def mymap(fn,seq):
    return [fn(i) for i in seq]

def myReduce(fn,seq):
    result = seq[0]
    for v in seq[1:]:
        result = fn(result, v)
    print result
    return result

def add(x,y):
    return x+y

def mult(x,y):
    return x*y

ll=range(1,10)

#IF I call

myReduce(add,ll)
myReduce(mult,ll)
#It will take these functions as arguments and apply them to every element in the list, which is now range (1,10)!!
