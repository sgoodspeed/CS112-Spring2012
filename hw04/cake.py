#!usr/bin/env python

cake = int(6)
choice = (int(0))

while choice!=2:
    choice = int(raw_input("Cake or death? 1: Cake 2: death "))
    if cake >0:
        if choice==1:
            print "Cake! It is very tasty. You feel happy to be alive."
        cake-=1
    elif cake<=0:
        print "We are all out of cake, sir or madam."
    
print "OK, you are dead. Like, you are so dead now. Like, you know what a manticore is? You are wayyy more dead than if you had tried to fight a manticore. Uhh, hmmm, you're like, 100% dead. Dude, that's as dead as you can be. Way more than you wanted to be, I bet."
    
