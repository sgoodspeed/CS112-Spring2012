#!/usr/bin/env python
"""
Binary Search

This was supposed to be a binary search algorithm but it isn't working...
I used the Iterative implementation from here:
    http://en.wikipedia.org/wiki/Binary_search_algorithm
"""
from hwtools import input_nums

nums=input_nums()
nums.sort()


print "I have sorted your numbers"
in1=int(raw_input("Which number should I find: "))

#min is 0 pos, max is the last position of the list
min=0
max=len(nums)-1

#Searches by checking the middle value of a sorted list for the requested number, and then narrows its search parameter either up or down depending on whether the middle int is bigger or smaller than the one that's being searched for
while max>=min:
    
    mid=max+min/2
    
    if nums[mid]==in1:
        break
    elif in1>nums[mid]:
        min=mid+1
    else:
        max=mid-1

        
if nums[mid]==in1:
    print "Found %s at %s"%(in1,mid)
else:
    print "Could not find", in1
