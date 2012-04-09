#!usr/bin/env python


class InputManager(object):
    _instance = None
    
    def__new__(cls, *args, **kwargs):
        if cls.instance is not None:
            cls._instance = super(InputManager, cls).__new__(cls, *args, **kwargs)
        return cls._instance

#__new__ is anything you want to call before the init function, you can do it in any object

#First we have an instance, which is none. cls stands for class.

#SO if instance is none, meaning there is no instance of this class yet, we call this and it spawns a thing of it. And so hey, OK, you can understand this.

#super(etc.) is the part where like, if it was tie fighter you would have super(Tie, cls)

#
#Talking about observers here
#



#OK now we are talking about managers, from here until we talk about something else


