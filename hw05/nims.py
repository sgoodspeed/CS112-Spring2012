#!/usr/bin/env python
"""nims.py

A simple competitive game where players take stones from stone piles.
"""

stones = int(40)
print "Number of stones left: %i" % stones
print "Max number of stones per turn: 5"
turn = 1
move = 0


while stones>0:
    #Player 1 turn
    if turn%2!=0:
        move = int(raw_input("%0i stones left. Player 1 [1-5]: " % stones))
        while move <=0 or move>5:
             move = int(raw_input("%i stones left. Please enter a number 1-5: " % stones))
        while stones<move:
             move = int(raw_input("Not enough stones. %i stones left. Please enter a number 1-5: " % stones))
        stones -=move

    #Player 2 turn
    elif turn%2==0:
        move = int(raw_input("%0i stones left. Player 2 [1-5]: " % stones))
        while move <=0 or move>5:
             move = int(raw_input("%i stones left. Please enter a number 1-5: " % stones))
        while stones<move:
             move = int(raw_input("Not enough stones. %i stones left. Please enter a number 1-5: " % stones))
        stones -=move
        
    turn+=1

        
if turn%2==0:
    print "Player 2 wins!"
elif turn%2!=0:
    print "Player 1 wins!"
