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

animals = [Dog("Rover"),Cat("Audrey")]

for animal in animals:
    if animal.canEat("garbage"):
        animal.eat("garbage")
    if animal.canEat("fish"):
        animal.eat("fish")
    animal.speak()
