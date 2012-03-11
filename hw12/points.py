#!usr/bin/env python

import math

class Point(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def move(self,x,y):
        self.x = x
        self.y =y

    def translate(self,x,y):
        self.x+=x
        self.y+=y

    def distance(self,other):
        d = math.sqrt((other.x-self.x)**2 + (other.y - self.y)**2)
        return d

    def slope(self, other):
        mTop = (other.y - self.y)
        mBottom = (other.x - self.x)
        if mBottom == 0:
            m = None
            return m
        else:
            m = mTop/mBottom
            return m
    
    def extrapolate(self, slope, distance):
        ##NOTE 1
        if slope == None:
            return "None"
        elif slope<0 or distance<0:
            u = -distance / (math.sqrt(slope**2+1))
            v = -slope*distance / (math.sqrt(slope**2+1))
        else:
            u = distance / (math.sqrt(slope**2+1))
            v = slope*distance / (math.sqrt(slope**2+1))
        x2 = self.x+u
        y2 = self.y+v
        return Point(x2,y2)
    
    def __str__(self):
        
        return "(%s,%s)"%(str(self.x),str(self.y))
    
    def __eq__(self,other):
        if isinstance(other,Point):
            if self.x == other.x and self.y == other.y:
                return True
            else:
                return False
        else:
            return False

##NOTE 1
##The formula I am using is here
#http://math.stackexchange.com/questions/25286/2d-coordinates-of-a-point-along-a-line-based-on-d-and-m-where-am-i-messing



# Point Object
# =====================================
# Create a Point point class.  Point objects, when created, look like this:
#     >>> pt = Point(3,4)
#     >>> print pt.x
#     3
#     >>> print pt.y
#     4
#
# In addition points have the following methods:
#    distance(self, other):
#        calculates the distance between this point and another
#    
#    move(self, x, y):
#        sets the points location to x,y
# 
#    translate(self, x, y):
#        offsets the point by x and y
# 
#    When all done, points should work like this:
#
#    >>> a = Point(0,0)
#    >>> b = Point(0,0)
#    >>> b.move(2, 2)
#    >>> print b.x, b.y
#    2 2
#    >>> b.translate(1,2)
#    >>> print b.x, b.y
#    3 4
#    >>> print a.distance(b)
#    5
#


# Advanced Section:
# ---------------------------------------
# Add the following function:
#     slope(self, other):
#         calculate the slope between two points
#
#     extrapolate(self, slope, distance):
#         returns a point along the line defined by slope
#         a given distance away
#
# Also, add the following special python methods:
#     __eq__(self, other):
#         checks if other is a Point and is equal to self
#
#     __str__(self):
#         returns a string representation of the point 
#     
#     >>> print Point(3,4)
#     (3,4)
#     >>> a = Point(1,2)
#     >>> b = Point(1,2)
#     >>> print a == b
#     True
