#!/usr/bin/env python 

titles=["Hitchikers guide to the galaxy",
        "Resteraunt at the end of the universe",
        "Life the unierse and everthing"]


titles.append("So Long and Thanks for all the fish")
titles.append("Mostly Harmless")

#So, the for loop sets the variable (in this case title) and then give it your list, (titles) and then it runs through the loop for each element, in this case printing title 
for title in titles[0:3]:#This prints elements 0,1 and 2. The last number referenced is 'non-inclusive' so we don't get three, in this case
    print title

for i in range(10):
    print i

#The above for loop prints 0-9, so this range command creates a list of 10 elements, 0-9, and then i is each of them, iterating up and counting

for i in range(1,11):
    print i
    #This prints 1-10

#For counting by a multiple of something
for i in range(1,11,2):
    print i
    #Now it counts 1-10 by twos

#numbers is a list, 0-99
numbers=range(100)

#The following counts by .2 UHHHHH
for i,n in enumerate(numbers):
    numbers[i]=n*.2
print numbers
    

