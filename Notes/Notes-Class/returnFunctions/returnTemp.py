#!usr/bin/env python

def fToC(temp):
    cent = temp-32
    cent*=5
    cent/=9
    return cent

num = int(raw_input("Enter a temperature in F: "))
print "In C that is", fToC(num)


