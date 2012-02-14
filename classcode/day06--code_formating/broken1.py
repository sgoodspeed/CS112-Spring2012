#!/usr/bin/env python


total=0
inputList=[]
inputNumber = None

#Getting a list of numbers
while inputNumber != "":
    inputNumber = raw_input()
    if inputNumber.isdigit():
        inputList.append(float(inputNumber))


for var in inputList:
    total += num

print total/len(inputList)
