# import basic library
import pygame as pg
import sys

# import user library
from WPygame import Font, Text, Progressbar, Button
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

    def create_btn(self):
        font = Font(comicsansms, EMERALD, 40)
        text = Text(self.sc, "Finish", font=font)
        btn = Button(self.sc, 250, 400, text, color=GRAY, function=sys.exit)

        return btn

    def create_progressbar(self, func):
        font = Font(comicsansms, EMERALD, 40)
        text = Text(self.sc, "", font=font)
        progressbar = Progressbar(self.sc, 100, 200, text, width = 600, function=func)

        return progressbar

    def create_widget(self):
        btn = self.create_btn()
        btn.disactivate()
        progressbar = self.create_progressbar(btn.activate)

        return [btn, progressbar]

    def check(self, event, obj):
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse = pg.mouse.get_pos()
                evt = obj[0].click(mouse)
                try:
                    evt()
                except TypeError:
                    print(evt)

    def update(self, widgets, mouse):
        widgets[1].update()
        widgets[0].update(mouse)


def play(time):
    pg.init()
    screen = pg.display.set_mode((800,800))
    pg.display.set_caption("WPython Demo")

    sceneDemo = Frame(screen, time)
    sceneDemo.start()


if __name__ == "__main__":
    play(10)
