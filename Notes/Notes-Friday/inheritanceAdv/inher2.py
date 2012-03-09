#!usr/bin/env python

class Animal(object):
    def __init__(self,name):
        self.name = name
    
    def canEat(self,food):
        pass
    
    def eat(self,food):
        pass
    
    def speak(self):
        pass
    def die(self):
        print self.name,"lived a good life"
    def __str__(self):
        return self.__class__.__name__ +": " + self.name
##This iteration of inheritance notes also added a function, the one in the Animal class that returned a string!

class Dog(Animal):
    def canEat(self,food):
        return True
    def eat(self,food):
        print self.name, "Gobbles", food
    def speak(self):
        print self.name + ": woof"

class Cat(Animal):
    def __init__(self,name):
        Animal.__init__(self, "Mrs. "+name)
    def canEat(self,food):
        return food.lower() == "fish"
    def eat(self,food):
        print self.name, "sniffs", food
    def speak(self):
        print self.name,"walks away"

dog = Dog("Rover")
cat = Cat("Audrey")

print isinstance(dog,Dog)
print isinstance(dog,Animal)
print isinstance(cat,Dog)
print dog
##Will return true for the first two because dog is an instance of those, third is false because cat is not dog

class Robot(object):
    battery = 0
    def charge(self,amnt):
        self.battery+=amnt
    def die(self):
        print self.name, "cannot die"
    
class RobotDog(Robot, Dog):
    def die(self, typ=Dog):
        typ.die(self)
#multiple inheritance, otherwise known as polymorphism! You can have an instance that is of TWO different objects. There is a lot of stuff going on here, but first and foremost what matters is that the order that you put the objects in. Here, Robot is first, so if I call the die function it will default to the robot iteration of it, EXCEPT HERE because in RobotDog we pass it the defaulr argument of typ = Dog. Also, just for good measure, randomly, **kwarg (or anything after the '**') makes a default dictionary, just like * makes a list.append
charlie = RobotDog("Charlie")
charlie.eat("stuff")
charlie.charge(3)
print charlie.battery
charlie.die()

