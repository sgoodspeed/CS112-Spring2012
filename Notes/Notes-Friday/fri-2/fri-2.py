#!urs/env/python

rr=range(10)#Setting a list

rr[2]#3rd element in the list

rr[-2]#Second to last element in the list

rr[:]#Makes a copy, becomes useful when you do things like a=rr[:] and now have the copy stored under a!

rr[:-1] #Whole list omitting the last element

rr[3:]#whole list omitting the first 3

rr[3:-1]#whole list omitting first three AND last

rr[::-1]#Whole list backwards (Even though there is a reverse function)



#'Chaining' is when you put in like ten functions in a row, chained together

#Like:
   #raw_input().lower().strip()


"""
#This should help explain some junk about chaining slice commands
#Tabbed over stuff is what the interpreter spit out
range(20)[::4]
    [0, 4, 8, 12, 16]
range(20)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
rr=range(20)
rr[::4]
    [0, 4, 8, 12, 16]
rr[::4][1:]
    [4, 8, 12, 16]
"""
