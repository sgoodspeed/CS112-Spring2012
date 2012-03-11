#!usr/bin/env python
import math
class Shape(object):
    def area(self):
        pass
    def perimeter(self):
        pass

class Rect(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def area(self):
        temp = self.width*self.height
        return temp
    def perimeter(self):
        return (self.width+self.height)*2
    
        
class Square(Rect):
    def __init__(self,side):
        self.width = side
        self.height = side
    def area(self):
        temp = self.width*self.height
        return temp
    def perimeter(self):
        return (self.width+self.height)*2


class Circle(Shape):
    def __init__(self,radius):
        self.diameter = radius*2
        self.radius = radius
    def area(self):
        return math.pi*self.radius**2
    def perimeter(self):
        return math.pi*self.diameter

class Polygon(Shape):
    def __init__(self, *points):
        self.points = [points]
    
    def Perimeter(self):
        sumPer = 0
        for i in range(0,len(points)):
            sumPer += (points(i)+points(i+1))
        sumPer +=(points(0) + points(-1))
        return sumPer
    def Area(self):
        
                      
    












# Shapes
# =========================================================
# 
# Define a shape object.  This object has abstract (empty) 
# methods for calculating the area and perimeter of the 
# shape.
#
# After that, create classes for Rectangles, Squares, 
# and Circles.
# 
# When done, the code should work like this.
#     >>> r = Rect(3,4)
#     >>> print r.area()
#     12
#     >>> sq = Square(5)
#     >>> print sq.perimeter()
#     20
#     >>> print isinstance(sq, Rectangle)
#     True
#     >>> c = Circle(3)
#     >>> print c.area()
#     28.274333882308138
#     

# Advanced Section
# ---------------------------------------------------------
# Add one more shape type: a polygon.  Polygons are created
# from a list of at least 3 points.
#
# >>> Polygon((0,0), (3,4), (0,4))
# >>> Polygon((0,0), (2,0), (2,2), (0,2))
#
# Perimeter should be easy to calculate, for area, use 
# method 1 on this site for finding the area of an irregular 
# polygon:
#   http://www.mathopenref.com/polygonirregulararea.html
# 
# You can find the area of a triangle with Heron's formula:
#   http://www.mathopenref.com/heronsformula.html


##BROKEN
##        tempX = 0
##        tempY = 0
##        length = len(self.points)
##        for i in range(0,):
##            count = i+1
            
##            tempX += abs(self.points(i)(0)-self.points(count)(0))
##            tempY += abs(self.points(i)(1)-self.points(count)(1))
##        return tempX+tempY
