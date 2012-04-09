#!usr/bin/env python

#writes file with name, w designates right, we can also use 'r' for read, 
file_in = open("textFile.txt","w")

for line in file_in:
    print line #Prints all the lines of the file

file_in.write("stuff we are writing to file.\n")

#python documentation for file or open commands it will tell you the whole list of r, w, those things.


try:
    file_in = open("textFile.butts","r")
    for line in file_in:
        print line
    file_in.close()
except IOError:
    print "Incorrect file name"
#after except you can have text that specifies which except code to run in the case of specific errors, for instance in this case IOError for wrong file.



# the above block of code will try to pull open the file, but if it doesn't exist, has the wrong name typed (as in this example) or whatever, the code will keep running and it will run the except line.

