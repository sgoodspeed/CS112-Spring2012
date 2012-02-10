#!/usr/bin/env python
from hwtools import *

print "Section 1:  If Statements"
print "-----------------------------"

# 1.  Is n even or odd?
n = raw_input("Enter a number: ")
n = int(n)

if n%2==0:
    print "1. Even"
else:
    print "1. Odd"




# 2. If n is odd, double it
if n%2 !=0:
    print "2.", n*2
else:
    print "2. Not odd"


# 3. If n is evenly divisible by 3, add four
if n%3==0:
    print "3.", n+4
else:
    print "Not a multiple of 3"


# 4. What is grade's letter value (eg. 90-100)
grade = raw_input("Enter a grade [0-100]: ")
grade = int(grade)

if grade<0 or grade>100:
    print "Not a grade"
elif grade>=0 and grade<65:
    print "4. F"
elif grade>=65 and grade<70:
    print "4. D"
elif grade>=70 and grade<80:
    print "4. C"
elif grade>=80 and grade<90:
    print "4. B"
elif grade>=90 and grade<=100:
    print "4. A"

