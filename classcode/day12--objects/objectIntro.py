#!usr/bin/env python

class Student(object):
    def __init__(self,name="No name"):
        self.name = name #NOTE 1
        
    def say(self,message):
        print self.name+": "+message#NOTE 2

    def say_to(self,other,message):
        self.say(message+", "+other.name)

    def printStudent(self):
        print self.name

class Course(object):
    def __init__(self,name):
        self.name = name
        self.enrolled = []

    def enroll(self, student):
        self.enrolled.append(student)#Classes can interact!!!!!!!!!!!!!ahhh

    def printCourse(self):
        for student in self.enrolled:
            student.printStudent()

        
bob = Student("Bob")
fred = Student("Fred")
cs112 = Course("CS112")
cs112.enroll(bob)
cs112.enroll(fred)

cs112.printCourse()

bob2 = bob #setting another name to be equal to instance of bob
print bob2 is bob #will print 'True'





###NOTE 1
##This is the constructor, basically. Whatever arguments I put in here will be
##put in the parenthesis down below, and then I set them in this init function.
##If you set up a default value like above with 'No name' it won't barf if you
##don't pass a value, and instead will  set it to whatever the default is.
##Think tree function!


##NOTE 2
##self allows access to all the data of a specific instance. Self is wichever
##instance we call the function 'say' on. By saying 'self' we are saying it is
##part of this object. Whenever we write a function we have to pass it 'self'
##as an argument or else we get an ugly error
