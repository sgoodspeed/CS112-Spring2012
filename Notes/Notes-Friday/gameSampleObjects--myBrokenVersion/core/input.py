import pygame
from pygame.locals import *

class KeyListener(object):
    def on_keydown(self,event):
        pass

    def on_keyup(self,event):
        pass
    

class MouseListener(object):
    def on_buttondown(self,event): pass
    def on_buttonup(self,event): pass
    def on_motion(self,event): pass
    

    

class InputManager(object):
    def __init__(self):
        self._key = []
        self._mouse = []
    def add_mouse_listener(self,listener):
        self._mouse
        
        
    def add_listener(self,listener):
        self._key.append(listener)

    def handle_event(self,event):
        if event.type == KEYDOWN:
            for listener in self.keydown:
                listener.on_keydown(event)
