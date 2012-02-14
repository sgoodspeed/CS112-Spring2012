#!/usr/bin/env python

from random import randrange#Importing random number function

def inc(arr,idx):
    arr[idx]+=1
#This is something that makes no sense... YET


totals = [0 for i in range(6)] #Gives you an array 6 long full of 0s
rolls = [randrange(6) for _ in range(720)]
[inc(totals,r) for r in rolls]
print totals
