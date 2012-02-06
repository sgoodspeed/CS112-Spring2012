#!usr/bin/env python

s=" "
s2="  "
s3="   "


print """
Hourglass: 1
Square:2
Block:3
Checked:4
"""

in1=raw_input("Choose a shape: ")
inp = int(in1)


if inp==1:
    c=raw_input("Choose character for art: ")
    print
    print 1*s,9*c
    print 2*s,7*c
    print 3*s,5*c
    print 4*s,3*c
    print 5*s,1*c
    print 4*s,3*c
    print 3*s,5*c
    print 2*s,7*c
    print 1*s,9*c

    
elif inp==2:
    c=raw_input("Choose character for art: ")
    print
    print 1*s,9*c
    print 1*s,1*c,5*s,1*c
    print 1*s,1*c,5*s,1*c
    print 1*s,1*c,5*s,1*c
    print 1*s,1*c,5*s,1*c
    print 1*s,1*c,5*s,1*c
    print 1*s,1*c,5*s,1*c
    print 1*s,9*c


elif inp==3:
    c=raw_input("Choose character for art: ")
    print
    print 1*s,9*c
    print 1*s,9*c
    print 1*s,9*c
    print 1*s,9*c
    print 1*s,9*c
    print 1*s,9*c
    print 1*s,9*c
    print 1*s,9*c
    print 1*s,9*c

elif inp==4:
    c=raw_input("Choose character for art: ")
    print
    print 1*s,2*c,1*s,2*c,1*s,2*c,1*s,2*c,1*s,2*c
    print 1*s,2*c,1*s,2*c,1*s,2*c,1*s,2*c,1*s,2*c
    print 1*s,1*s,2*c,1*s,2*c,1*s,2*c,1*s,2*c,1*s
    print 1*s,1*s,2*c,1*s,2*c,1*s,2*c,1*s,2*c,1*s
    print 1*s,2*c,1*s,2*c,1*s,2*c,1*s,2*c,1*s,2*c
    print 1*s,2*c,1*s,2*c,1*s,2*c,1*s,2*c,1*s,2*c
    print 1*s,1*s,2*c,1*s,2*c,1*s,2*c,1*s,2*c,1*s
    print 1*s,1*s,2*c,1*s,2*c,1*s,2*c,1*s,2*c,1*s
    print 1*s,2*c,1*s,2*c,1*s,2*c,1*s,2*c,1*s,2*c
    print 1*s,2*c,1*s,2*c,1*s,2*c,1*s,2*c,1*s,2*c
    print 1*s,1*s,2*c,1*s,2*c,1*s,2*c,1*s,2*c,1*s
    print 1*s,1*s,2*c,1*s,2*c,1*s,2*c,1*s,2*c,1*s
    print 1*s,2*c,1*s,2*c,1*s,2*c,1*s,2*c,1*s,2*c
    print 1*s,2*c,1*s,2*c,1*s,2*c,1*s,2*c,1*s,2*c
    print 1*s,1*s,2*c,1*s,2*c,1*s,2*c,1*s,2*c,1*s
    print 1*s,1*s,2*c,1*s,2*c,1*s,2*c,1*s,2*c,1*s
    
