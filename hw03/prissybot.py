#!usr/bin/env python

name = raw_input("Enter name: ");
print "Prissybot: Hello there, %s" % name;

greeting = raw_input("Say hello: ");
print "Prissybot: That's %s, SIR" % greeting;

apology = raw_input("Apologize: ");
print "'%s', really? Never mind. Let's talk about something." % apology;

topic = raw_input("Enter a topic: ");
print "Frankly I find the idea of discussing %s trite and idiotic. Let's talk about math instead. What is 100+100?" % topic;


numIn = raw_input("enter your answer: ");
num = int(numIn)
print "Your answer is %i? I suppose it doesn't matter. OK, tell me what 10/10 is." % num;


numIn2 = raw_input("Enter your answer: ");
num2 = int(numIn2);
print "Obviously, %i. Now, ask me a question" % num2

print """
1 for addition
2 for subtraction
3 for multiplication
4 for division
"""
numIn3 = raw_input("Choose an operation: ");
num3 = int(numIn3);

if num3 == 1:
    nmIn1 = raw_input("Enter first number: ")
    nm1 = float(nmIn1)
    nmIn2 = raw_input("Enter second number: ")
    nm2 = float(nmIn2)
    nm3 = nm1 + nm2
    print "What an obvious question %f + %f is of course %f. You bore me. This program is over." % (nm1,nm2,nm3)

elif num3==2:
    nmIn1 = raw_input("Enter first number: ")
    nm1 = double(nmIn1)
    nmIn2 = raw_input("Enter second number: ")
    nm2 = double(nmIn2)
    nm3 = nm1 - nm2
    print "What an obvious question %d - %d is of course %d. You bore me. This program is over." % (nm1,nm2,nm3)
     
elif num3==3:
    nmIn1 = raw_input("Enter first number: ")
    nm1 = float(nmIn1)
    nmIn2 = raw_input("Enter second number: ")
    nm2 = float(nmIn2)
    nm3 = nm1 * nm2
    print "What an obvious question %f * %f is of course %f. You bore me. This program is over." % (nm1,nm2,nm3)

elif num3==4:
    nmIn1 = raw_input("Enter first number: ")
    nm1 = float(nmIn1)
    nmIn2 = raw_input("Enter second number: ")
    nm2 = float(nmIn2)
    nm3 = nm1 / nm2
    print "What an obvious question %f / %f is of course %f. You bore me. This program is over." % (nm1,nm2,nm3)

else:
    print "Was that really too much for you? %i clearly was not even an option. This program is over. Idiot." % num3
     
"""
prissybot.py

CS112 Homework 3:   PrissyBot

Prissy bot, the rude chat bot, is just mean!  It does not listen, asks obnoxious questions, and says anything it likes.
"""

# Step 1:
# -----------------------
# Program the following.
# 
#    $ python prissybot.py
#    Enter your name:  Paul
#   
#    PrissyBot: Hello there, Paul
#    Paul: hi bot
#    PrissyBot: You mean, "hi bot, sir!"
# 
# Make sure the user inputs their own name and responses.



# Step 2:
# -----------------------
# Keep adding to the conversation. Make sure that your program 
# includes the following:
# 
#  * get and use input from the user
#  * 3 math problems
#     * at least one should get numbers from the user
#  * at least 3 insults


# Advanced
# -------------------------
# Make sure your prissy bot uses string formatting throughout.  
# Also, create new programs for the following:
#  
#  1. draw some kind of ascii art based on user input
#  2. print a decimal/binary/hexidecimal conversion table 
#     * well formated and labeled
#     * reads 5 numbers from the input (all less than 256)
#  3. reduce a fraction
#     * read a numerator and denominator from the user
#     * ex.  6/4 = 1 2/4

