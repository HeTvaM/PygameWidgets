# import basic library
import pygame as pg
import sys

# import user library
from WPygame import Font, Text, DDownButton
from logger import log, log_with_return
from constpack import GRAY, BLACK, EMERALD
from constpack import arial, vivaldi, comicsansms

from abstract import Scene

#>------------SUMMARY----------------<
# this module is used to test and provide a demo of how the library works.
# Soon there will be a flexible system of settings and full-fledged demo scenes.
# Wait!
#>------------SUMMARY----------------<

# const

# Main class
class Frame(Scene):
    def __init__(self, screen, time):
        super().__init__(screen, time)

    def create_dropdown(self):
        texts = ["Аркада", "Платформер", "Экшен", "Симулятор"]
        font = Font(comicsansms, EMERALD, 40)
        text = Text(self.sc, "Аркада", font=font)
        btn = DDownButton(self.sc, 250, 400, text, texts, color=GRAY)

        return btn

    def create_widget(self):
        btn = self.create_dropdown()

        return btn

    def check(self, event, obj):
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse = pg.mouse.get_pos()
                evt = obj.click(mouse)
                try:
                    evt()
                except TypeError:
                    print(evt)

    def update(self, widget, mouse):
        widget.update(mouse)



def play(time):
    pg.init()
    screen = pg.display.set_mode((800,800))
    pg.display.set_caption("WPython Demo")

    sceneDemo = Frame(screen, time)
    sceneDemo.start()


if __name__ == "__main__":
    play(10)
