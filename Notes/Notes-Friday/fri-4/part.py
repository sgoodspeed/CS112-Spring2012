#!usr/bin/env python



#We are going to have partial return a new function
def partial(fn, *part_args):
    def result(*args):
        a = part_args + args
        return fn(*a)
    return result


#OK now we are doing a decorater, jack called them cute!

def logger(fn):
    def wrap(*a):
        print fn.__name__,a#We are referencing the name of our function here
        return fn(*a)
    return wrap
