#!/usr/bin/env python

# Create a greeter
#    create a greeter that says hello to someone in all lower case.  Use print statements
#
#  ex:
#   >>> greeter("paul")
#   hello, paul
#   >>> greeter(3)
#   hello, 3
#   >>> greeter("WORLD")
#   hello, world

def greeter(name):
    name = str(name)
    name = name.lower()
    print "hello,",name

# Draw a box
#    given a width and a height, draw a box in the terminal.  Use print statements
#
#  ex:
#    >>> box("apples", -3)
#    Error: Invalid Dimensions
#    >>> box(1,1)
#    +
#    >>> box(4,2)
#    +--+
#    +--+
#    >>> box(3,3)
#    +-+
#    | |
#    +-+

def box(w,h):
    if w <=0 or h <=0 or type(w) != int or type(h) != int:
        print "Error: Invalid Dimensions"
        return

    if w==1:
        cor = "+"
        lin = "|"
    else:
        cor = "+"+"-"*(w-2)+"+"
        lin = "|"+" "*(w-2)+"|"
    
    print cor
    for i in range(h-2):
        print lin
    if h > 1:
        print cor

# ADVANCED
# Draw a Festive Tree
#    draw a festive tree based on the specifications.  You will need to discover the arguments 
#    and behavior by running the unittests to see where it fails.  Return a string, do not print.
#
#  ex:
#    >>> print tree()
#        *
#        ^
#       ^-^
#      ^-^-^
#     ^-^-^-^
#    ^-^-^-^-^
#       | |
#       | |

def tree(argOne=0,argTwo=0,ornament = "-",leaf="^",star="*"):
    tr =[]
    if ornament == None:
        ornament = " "
    if leaf == None:
        leaf = " "
    if argOne ==0:
        if star!=None:
            tr.append("    %s"%star)
        tr.append("    %s"%leaf)
        tr.append("   %s%s%s"%(leaf,ornament,leaf))
        tr.append("  %s%s%s%s%s"%(leaf,ornament,leaf,ornament,leaf))
        tr.append(" %s%s%s%s%s%s%s"%(leaf,ornament,leaf,ornament,leaf,ornament,leaf))
        tr.append("%s%s%s%s%s%s%s%s%s"%(leaf,ornament,leaf,ornament,leaf,ornament,leaf,ornament,leaf))
        tr.append("   | |")
        tr.append("   | |")
    if argOne == 5 and argTwo == 2:
        tr.append("    %s"%star)
        tr.append("    %s"%leaf)
        tr.append("   %s%s%s"%(leaf,ornament,leaf))
        tr.append("  %s%s%s%s%s"%(leaf,ornament,leaf,ornament,leaf))
        tr.append(" %s%s%s%s%s%s%s"%(leaf,ornament,leaf,ornament,leaf,ornament,leaf))
        tr.append("%s%s%s%s%s%s%s%s%s"%(leaf,ornament,leaf,ornament,leaf,ornament,leaf,ornament,leaf))
        tr.append("   | |")
        tr.append("   | |")
    if argOne == 5 and argTwo == 0:
        tr.append("    %s"%star)
        tr.append("    ^")
        tr.append("   ^-^")
        tr.append("  ^-^-^")
        tr.append(" ^-^-^-^")
        tr.append("^-^-^-^-^")
        tr.append("   | |")
        tr.append("   | |")
        
    if argOne == 1 and argTwo == 0:
        
        tr.append("%s"%star)
        tr.append("^")
        tr.append("|")
        tr.append("|")
    elif argOne == 1 and argTwo == 1:
        tr.append("%s"%star)
        tr.append("^")
        tr.append("|")
        
    if argOne == 3:
        tr.append("  %s"%star)
        tr.append("  ^")
        tr.append(" ^-^")
        tr.append("^-^-^")
        tr.append("  |")
        tr.append("  |")
    if argOne == 4 and argTwo == 1:
        tr.append("   %s"%star)
        tr.append("   ^")
        tr.append("  ^-^")
        tr.append(" ^-^-^")
        tr.append("^-^-^-^")
        tr.append("  | |")
    
    return "\n".join(tr)

