#!usr/bin/env python

import pygame

from core.input import InputManager, KeydownListener
from pygame.locals import *

#If this wasn't hypothetical we would put these in sperate files maybe called:

#world/player.py
class Player(object):
    def move(self,direction):
        print "player moves %d, %d" % direction
    def jump(self):
        print "Player jumps"

# core/sound.py
class SoundManager(object):
    def play(self,which):
        print "playing %s sound" % which

#controls/player.py
class PlayerController(KeydownListener):
    def __init__(self,player):
        self.player = player
    def on_keydown(self,event):
        if event.key == K_SPACE:
            self.player.jump()


#Alec said he broke it so he couldn't do this thing so NEVER MIND THEN
#class SoundController(KeydownListener):
#    def on_keydown(self,event):

        

#Make sure you do the:
#mkdir core
#cd core
#touch __init__.py
#touch just creates an empty file, then we make inputmanager inside the core
#directory

class Game(object):
    size = 800,600
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)


        self.input = InputManager()

        self.player = Player()

        self.input.add_listener(PlayerController(self.player))
        
    def quit(self):
        self._done = True
        
    def run(self):
        self._done = False
        
        while not self._done:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.quit()
                else:
                    self.input.handle_event(event)

        #update

        #draw

        self.screen.fill((0,0,0))
        pygame.display.flip()

if __name__ == "__main__":
    game = Game()
    game.run()
    pygame.quit()
