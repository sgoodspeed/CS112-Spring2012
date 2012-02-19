#!/usr/bin/env python
"""
Selection sort

This is my selection sort, it's not working right!!!
I used this:
    http://en.wikipedia.org/wiki/Selection_sort
"""
from hwtools import input_nums

nums = input_nums()

print "Before sort:"
print nums

max=len(nums)#End of list
for x in range(0,max):
    test=x
    for i in range(x+1, max):
        if nums[i]<nums[test]:
            test=i
    nums[x],nums[test]=nums[test],nums[x]

print "After sort:"
print nums
