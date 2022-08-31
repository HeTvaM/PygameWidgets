# init basic library
import pygame as pg

#>------------SUMMARY----------------<
# this module for constants used in the pygame engine
# there are colors, font and ...
#>------------SUMMARY----------------<
pg.init()

# init some basic colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)

YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
RED = (255, 0, 0)

EMERALD = (80, 200, 120)
GREEN = (0, 255, 0)

LIGHT_BLUE =(0, 0, 128)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
DARK_CYAN = (0, 128, 128)
DUSTY_BLUE = (176, 224, 230)

LIGHT_PURPLE = (238, 190, 241)
PURPLE = (128, 0, 128)


# init color's packs
RAINBOW = {"RED": (255, 0, 0),
           "ORANGE": (255, 165, 0),
           "YELLOW": (255, 255, 0),
           "GREEN": (0, 255, 0),
           "LIGHT_BLUE": (0, 0, 128),
           "BLUE": (0, 0, 255),
           "PURPLE": (128, 0, 128)}


# init some basic fonts
arial = pg.font.match_font("arial")
vivaldi = pg.font.match_font("vivaldi")
comicsansms = pg.font.match_font("comicsansms")
calibri = pg.font.match_font("calibri")
terminal = pg.font.match_font("terminal")
georgia = pg.font.match_font("georgia")
