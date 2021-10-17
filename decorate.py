# import basic library
import os
import pygame

# import user's library


#>------------SUMMARY----------------<
# this module is used for custom decorators that provide
# additional functionality to the main library of the WPygame.py
#>------------SUMMARY----------------<

def tools(*args, **kwargs):
    def inside(func):
        def wrapper(*args, **kwargs):
            cls = args[0]
            obj = func(cls)

            if obj is not None:
                cls.screen.blit(obj, (cls.x,cls.y))
            else:
                pygame.draw.rect(cls.screen, cls.COLOR, cls.rect)

        return wrapper
    return inside
