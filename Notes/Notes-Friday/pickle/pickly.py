#!usr/bin/env python

import os
import pickle

class Level(object):
    def__init__(self):
        self.enemies = 20
        self.powerups = 10

    @classmethod
    def load(self,name):
        path = os.path.join("saves",name+".sav")
        level = cls()
        
        if os.path.exists(path):
            with open(path "r") as f:
                return pickle.load(f)
        else:
            return cls()
            
        return level
    
    def save(self,name):
        path = os.path.join("saves", name+".sav")

        with open(path, "w")as f:
            pickle.dump(self,f)
        
    def collect(self):
        self.powerups -=1

    def kill(Self):
        self.enemies-=1

##def loadLevel(name):
##    path = os.path.join("saves",name+".sav")

##    if os.path.exists(path):
##        with open(path,"r") as f:
##            return pickle.load(f)
##    else:
##        return Level()

##def saveLevel(name,level):
##    path os.path.join("saves",name+".sav")
##    #with opens a file on a path, reads it, and then closes it, like, "with this open file as f, do the following, close it after! Can't do this with any object, though.
##    with open(path,"w") as f:
##        pickle.dump(f,level)
                      
