#!usr/bin/env python

letters=['a','d','f']

letters[1:1] = ['b','c']#[1:1] puts it in that location in the list
print letters

letters+=['g','h']
print letters

print letters[-1]#Prints the last element in the list, because it sort of loops back once



letters2=letters[:]#This makes it equal to all the elements of the list,so if I go and change the original list the new letters2 won't change
letters[0] = 'huh'
print letters2

