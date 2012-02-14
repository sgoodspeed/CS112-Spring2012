#!usr/bin/env python

#and, or, and not are all functions in python to be used in while and if statements

count=0
while count<=0:
    count=raw_input("Countdown from what number?  ")
    count=int(count)

while count>0:
    print count
    count-=1

print "Brastoff"
