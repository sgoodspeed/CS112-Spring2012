#!usr/bin/env python

#Conversation
name = raw_input("Enter name: ");
print "Prissybot: Hello there, %s" % name;

greeting = raw_input("Say hello: ");
print "Prissybot: That's %s, SIR" % greeting;

apology = raw_input("Apologize: ");
print "'%s', really? Never mind. Let's talk about something." % apology;


topic = raw_input("Enter a topic: ");
print "Frankly I find the idea of discussing %s trite and idiotic. Let's talk about math instead. What is 100+100?" % topic;

#Prissybot's math question
ans1 = int(raw_input("enter your answer: "));
print "Your answer is %i? I suppose it doesn't matter. OK, tell me what 10/10 is." % ans1;


ans2 = int(raw_input("Enter your answer: "));
print "Obviously, %i. Now, ask me a question" % ans2

#User-input math
print """
1 for addition
2 for subtraction
3 for multiplication
4 for division
"""

#Picks an operation depending on what the user inputs for 'op'
op = int(raw_input("Choose an operation: "));


#takes in two numbers, spits out the answer
if op == 1:
    nm1 =float(raw_input("Enter first number: "))
    nm2 = float(raw_input("Enter second number: "))
    nm3 = nm1 + nm2
    print "What an obvious question %f + %f is of course %f. You bore me. This program is over." % (nm1,nm2,nm3)

elif op == 2:
    nm1 = float(raw_input("Enter first number: "))
    nm2 = float(raw_input("Enter second number: "))
    nm3 = nm1 - nm2
    print "What an obvious question %d - %d is of course %d. You bore me. This program is over." % (nm1,nm2,nm3)
     
elif op == 3:
    nm1 = float(raw_input("Enter first number: "))
    nm2 = float(raw_input("Enter second number: "))
    nm3 = nm1 * nm2
    print "What an obvious question %f * %f is of course %f. You bore me. This program is over." % (nm1,nm2,nm3)

elif op == 4:
    nm1 = float(raw_input("Enter first number: "))
    nm2 = float(raw_input("Enter second number: "))
    nm3 = nm1 / nm2
    print "What an obvious question %f / %f is of course %f. You bore me. This program is over." % (nm1,nm2,nm3)

else:
    print "Was that really too much for you? %i clearly was not even an option. This program is over. Idiot." % op
     

