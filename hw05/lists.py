#!/usr/bin/env python
"""lists.py

A bunch of excercises to see if you understand list comprehensions
"""


# Solve the following problems with one python statement.  It is fine 
# to break up the statement into multiple lines as long as it is only
# one actual command.
#
# This is fine:
#   print [ (x,y) 
#           for x in range(10)
#           for y in range(10) ]
#

# 1. Read a bunch of numbers from the input separated by spaces and 
#    convert them to ints

"""
[<op> <for -clause(s)> ... <if-clause>][:3]
"""


print "1.", [int(x) for x in raw_input().split(' ')]


#2.  Read another bunch of numbers, convert them, and return the list 
#     of only the first 3
print "2.", [int(x) for x in raw_input().split(' ')]

# 3.  Read a bunch of words separated by commas from the command line,
#     remove any excess spaces, and print a list of their lenghts
print "3.", []

# 4.  Create a list of every multiple of 3 between 1 and 100 with their 
#     index
#[[i,i*3] for i in range(33)]

#OR BETTER YET

#list(enumerate(range(3,100,3)))

#Enumerate takes a list, like [3,6,9,12,...99] and turns it into [[1,3][2,6]]

#        ex:  [ [0,3], [1,6], [2,9]...]
print "4.", []

# 5. create a list of every card in a deck of cards 
print "5.", []
suits = "hearts" "spades" "diamonds" "clubs"
#values = "A" "2"...
[(value,suit) for suit in suits for value in values]
# 6.  Create a 5 by 5 array filled with zeros
print "6.", []


# 7.  Make a list of every perfect square between 1 and 1000
print "7.", []

# 8.  Make a list of every perfect square between 1 and 1000 
#     a different way
print "8.", []

# 9.  List every python file in this directory
print "9.", []

# 10.  Print a list of every pythagorean triple with a side less than
#      or equal to 20.  Don't include duplicates ([3,4,5] == [4,3,5])
print "10.", []



# I couldn't in good concious include this, but it is fun to 
# figure out/find.

## NOT REQUIRED
# 11.  Print a list of every prime number less than 100
print "11.", []




































"""
Hey TAs

I definitely don't know how this list stuff works, I've been googling and trying
for hours, and I only got the first one with help, I think I just don't understand
the syntax of this stuff.

I'm only turning this homework in so I get at least the
half credit for the basic assignment and olympic rings I did, I'm going to get in
touch to try and clear up the issues I'm having with this stuff, but right now I feel
like I have exhausted my resources and can't get any further on my own.

The tic tac toe is giving me problems I don't think I can solve in the next 12
minutes as well, and this is probably just a result ome not starting with enough
time left.
"""
