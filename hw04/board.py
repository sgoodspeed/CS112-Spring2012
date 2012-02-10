#!usr/bin/env python

width=1
height=1
loo=0
brd="#-"

width=int(raw_input("Input a width: "))
height=int(raw_input("Input a height: "))


while loo<=height:
    print brd*width
    loo+=1
    
    
