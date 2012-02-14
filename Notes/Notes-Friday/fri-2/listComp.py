#!usr/bin/env python

from random import randrange#Importing random number function

powers=[x**2 for x in range(11)]#Returns a list of square numbers 1-10

#Called mapping, or list comprehension

fourAdd=[x+4 for x in range (11)]

#Filters get applied to a list and return only the elements for which the filter is true, or w/e

#randrange(x,x,x) takes arguments in the same way as a range anywhere else


dice = [randrange(1,7) for _ in range(20)]
#would give us the random roll of 6-sided dice 20 times
print [d for d in dice if d>=4]#prints all the dice rlls that ed up 4 or above

#[person for person in people if person .lower().find("ste")]
#This is a hypothetical function that would run through a list called 'people' (that we don't have) and return everyperson with 'ste' in their name

#to count up coordinates in a list (basically doin' stuff that has multiple variables I want to iterate up:

coords=[[x,y] for x in range(11) for y in range (11) if x!=y]
print coords

allDice = [[x,y,x+y]
 for x in range (1,7)
 for y in range (1,7)
 if x>=y]
print allDice
#This one gives you every possible roll of two six sided dice, and also prevents duplicates, with the if x>=y command line


