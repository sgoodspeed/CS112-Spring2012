#!usr/bin/env python

class Enemy(object):

    _objects = []#_ in front makes it private

    def __init__(self,name):
        Enemy.objects.append(self)
        self.name = name


    def update(self):
        print self.name,"is in your base"

    def kill(self):
        print self.name,"is dead"
        Enemy._objects.remove(self)


    @classmethod
    def all(cls):
        return cls._objects[:]# Note 1

    @classmethod
    def all(cls):
        x,y = 0,0
        vx,vy = 0,0
        color = 255,0,100
        return Enemy(x,y,vx,vy,color,bounds)
        #Note 2

class Vector:
    @staticmethod#NOTE 3
    def dot(a,b):
        print "no"
        


Enemy.spawn(screen.get_rect())
#the variables in the example are all zeros, in real life we would use
#randrange or something to set up some parameters.

Vector.dot(a,b)


a = Enemy ("A")
b = Enemy("B")
c = Enemy("C")
for enemy in Enemy.objects:
    enemy.update()


c.kill()

for enemy in Enemy.objects:
    enemy.update()


#NOTE 1
#this makes a COPY of a list of all the things in objects[], so that you can
#fuck around with that list that w made without accidentally changing values
#that live in Enemy. Basically what Object oriented programming is all about,
#in that it is keeping different methods objects and functions seperate and
#unable to change each other's data unwittingly.


#NOTE 2
#So, it'd be nice if we had a thing that could create a random tie fighter in random bounds, which is what this stuff does. Instead of spawning them we can just call this function, (WHICH THOUGH IT IS CLASS SPECIFIC DOES NOT REQUIRE AN INSTANCE OF ENEMY TO EXIST TO CALL IT CREATES ONE.) we call this and it makes one. This example does NOT work though hahahaha.

#Note 3
#this lets you define a method of a class that does not need self. This means
#you can call this method without initializing Vector. This is good for a code
#clarity thin, and little else, because now our call of the function clearly
#says 'vector' which is better than a.dot(a,b) or whatever if it wasnt in a
#class Vector.




#######################################
#class Enemy(Sprite):
#    _all_bullets = Group()

#    def shoot(self):
#        Bullet(Enemy._all_bullets, self.bullets)

#Let's us track bullets as a group of all bullets, and ALSO as the bullets belonging to a single enemy class.
