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



