#!usr/bin/env python


#Pythagorean triples from 1-20, no duplicates, where a pythagorean triple is a number set within whihc a**2 + b**2 = c**2

pythag = [[x,y,z]
 for x in range(1,21)
 for y in range(x,21)
 for z in range(y,21)#NOTE 1
 if x**2+y**2==z**2 and x<=y]


print pythag


#NOTE 1
#Range piggybacking off of range before, saves computation time
