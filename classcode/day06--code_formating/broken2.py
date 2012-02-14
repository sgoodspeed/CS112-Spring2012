#!usr/bin/env python



#importing random integer function
from random import randint
s=1
input=int(raw_input())
randList=[]

#Making a list of random integers between 0 and 20, total number of random numbers equal to input
for _ in range(input):
    randList.append(randint(0,20))


print randList


#Sorting numbers into lowest-highest
while s:
    s=0
    for i in range(1,input):
        if list1[i-1]>list1[i]:
            t1=randList[i-1]
            t2=randList[i]
            randList[i-1]=t2
            randList[i]=t1
            s=1

            
print randList
