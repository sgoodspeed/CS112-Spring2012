#!usr/bin/env python

grid = []
for i in range(10):   #<----- number of rows
    row =[]
    for j in range(10):   #<------ number of cols
        row.append(j)
    grid.append(row)


for i,row in enumerate(grid):
    for j,val in enumerate(row):
        print "[",i,j,"]:",val
    print ""
