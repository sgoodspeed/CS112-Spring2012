#!/usr/bin/env python
from hwtools import *

print "Section 4:  For Loops"
print "-----------------------------"

nums = input_nums()
# 1. What is the sum of all the numbers in nums?

    
print "1.", sum(nums[:])


# 2. Print every even number in nums


#for i in nums:
 #   if i%2==0:
  #      print i
   #     evenNums.append(i)




# 3. Does nums only contain even numbers? 
evenCheck=1
for i in nums:
    if i%2!=0:
        evenCheck=2
if evenCheck==1:
    print "3. All even."
elif evenCheck==2:
    print "3. Some odd"



# 4. Generate a list every odd number less than 100. Hint: use range()
oddHundred=[]
for i in range(1,101,2):
    oddHundred.append(i)
print
print oddHundred
print

# 5. [ADVANCED]  Multiply each element in nums by its index

numInd=[]
length=int(len(nums))
ind=0
el=0
count=0
while count<length:
    ind=nums[el]*el
    el+=1
    numInd.append(ind)
    count+=1
print numInd   
