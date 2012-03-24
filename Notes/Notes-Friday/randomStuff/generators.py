#!usr/bin/env python
#A generator is any function that has a yield, or returns multiple values
def fib():
    a=0
    b=1
    while True:
        b,a=a+b, b
        yield b
        #print b

f = fib()#In this case f is the instance of the generator
#print f.next()
#print f.next()



import time
for n in fib():
    print n
    time.sleep(1)#Makes it wait a second before it prints another thing


#Fib is a generator. IT generates a lot of things, in this case the fib
#sequence. Every time throught he loop it yields B. When I call f.next()
#it yields the next value, based on the parameters of the generator.so,
#for n in fib(), print n, sleep one second.


def enum(coll):
    c = 0
    for v in coll:
        yield c,v
        c+=1

#print list(enum(["a","b","c"]))
