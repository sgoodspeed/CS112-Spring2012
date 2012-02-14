#!usr/bin/env python


print """
These triple-quotes let me...
Do all the formatting within it!
Cool.
"""

#to find and print the binary of a number, type
bin(11)

#and for the hexadecimal use:
hex(357)
#This is the format for all functions like these



# int sets an integer, float sets a float, raw_input sets a string (I THINK!!)
#int(a) is the format for this


#SAMPLE UH SORT OF
#print n = int(raw_input("Enter a number: "))
#This takes a number from user and sets n to that number
#abs is for absolute value, str is for string.
#min, max. The function min(2,3,4,1) will return you the lowest number you put in

#Shit what does this do we don't REALLY need it but it's some sort of conversion thing...
#int("0xff",16)

#OK next section is about string formatting. Diffuculut QUESTION MARK???

#Say you wanted to print "Hi Jim, thanks for the bear."
#But what if name is just:
#name='Jim'
#And pear is
#item='pear'
#Well, you need to...
#"Hi "tname", thanks for the "titemt"."


#But that is really ugly. Try this:
#msg = Hi %s, thanks for the %s."%(name,item)
#print msg
#Wooooo old school
name="Jim"
item="bear"

msg = "Hi %s, thanks for the %s."%(name,item)
print msg

#alternatively:
msg2="Hi %s, thanks for the %s."
print msg2 %(name,item)

#%s    string
#%d    decimal
#%f    float

#You will notice if you try to do
print 3
print 100
print 11
#It comes out all ugly in spacing


print "%4d" % 6
#though, will give you a number of spaces equivalent hereto the numbr, in this case 4

#And here
print "%04d" % 16
#fills in the spaces with zeroes

#Taking user input:

#to take input
name3 = raw_input("Enter your name: ")
inp = raw_input("%s: " % name3)
print "input was: %s" % inp

#assigning multiple variables at once
x,y = 3,4
print x
print y
print x, y
