#!/usr/bin/env python
"""tictactoe.py

A Simple tic tac toe game
"""


# Implement a version of tic tac toe

spaces = range(1,10)


p1= "Player 1"
p2= "Player 2"
X = "X"
O = "O"

turn = 0
board = """
%s | %s | %s
-----------
%s | %s | %s
-----------
%s | %s | %s""" % (spaces[0],spaces[1],spaces[2],spaces[3],spaces[4],spaces[5],spaces[6],spaces[7],spaces[8])

print spaces[3]
spaces[3] = X
print spaces[3]
print board

"""

player1Moves = []
player2Moves = []

win = 0
print board
while win==0:
    #Player 1's turn
    if turn%2==0:
         moveX = int(raw_input("Player 1 turn. Please pick a space: "))
         ind = moveX-1
         spaces.insert(ind,X)
        # spaces[ind] = X
         print spaces[ind]
         print ind
         print spaces[3]
         print board
    """

