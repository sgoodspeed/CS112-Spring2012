#!usr/bin/env python



print """

Conversion table: 1
Fractional reduction: 2
"""
selIn=raw_input("Choose a procedure: ")
selIn1=int(selIn)

if selIn1==1:
    numIn1=raw_input("Enter numbers you would like to convert: 1: ")
    num1=int(numIn1)
    numIn2=raw_input("2: ")
    num2=int(numIn2)
    numIn3=raw_input("3: ")
    num3=int(numIn3)
    numIn4=raw_input("4: ")
    num4=int(numIn4)
    numIn5=raw_input("5: ")
    num5=int(numIn5)
    print
    print "Numbers"
    print num1,num2,num3,num4,num5
    print "Hexadecimal"
    numH1=hex(num1)
    numH2=hex(num2)
    numH3=hex(num3)
    numH4=hex(num4)
    numH5=hex(num5)
    print numH1,numH2,numH3,numH4,numH5
    print "Binary"
    numB1=bin(num1)
    numB2=bin(num2)
    numB3=bin(num3)
    numB4=bin(num4)
    numB5=bin(num5)
    print numB1,numB2,numB3,numB4,numB5

elif selIn1==2:
    numIn1=raw_input("Enter fraction you would like to reduce: Numerator: ")
    num1=float(numIn1)
    numIn2=raw_input("Denominator: ")
    num2=float(numIn2)
    num3=num1/num2
    print """
    %f / %f = %f
    """ % (num1,num2,num3)
