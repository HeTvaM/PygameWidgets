# import basic library
import pygame as pg
import sys

# import user library
from WPygame import Font, Text, Toolbar, Button
from logger import log, log_with_return
from constpack import GRAY, BLACK, EMERALD
from constpack import arial, vivaldi, comicsansms

#>------------SUMMARY----------------<
# this module is used to test and provide a demo of how the library works.
# Soon there will be a flexible system of settings and full-fledged demo scenes.
# Wait!
#>------------SUMMARY----------------<

# const


# Main class
class Scene:
    def __init__(self, screen, time):
        self.sc = screen
        self.clock = pg.time.Clock()
        self.time = time

    def create_btn(self):
        font = Font(comicsansms, EMERALD, 40)
        text = Text(self.sc, "Finish", font=font)
        btn = Button(self.sc, 250, 400, text, color=GRAY, function=sys.exit)

        return btn

    def create_toolbar(self, func):
        font = Font(comicsansms, EMERALD, 40)
        text = Text(self.sc, "", font=font)
        toolbar = Toolbar(self.sc, 100, 200, text, width = 600, function=func)

        return toolbar

    def check_event(self, obj):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse = pg.mouse.get_pos()
                    evt = obj.click(mouse)
                    evt()

    def check_time(self, time):
        if time//30 > self.time:
            pg.quit()
            sys.exit()

    def start(self):
        play = True
        time = 0
        btn = self.create_btn()
        btn.disactivate()
        tlb = self.create_toolbar(btn.activate)
        cursor = pg.mouse.set_cursor(*pg.cursors.arrow)
        while play:
            self.check_time(time)
            self.clock.tick(60)
            time += 1

            self.check_event(btn)

            self.sc.fill((0,0,0))

            mouse = pg.mouse.get_pos()
            tlb.update()
            btn.update(mouse)

            pg.display.flip()


def play(time):
    pg.init()
    screen = pg.display.set_mode((800,800))
    pg.display.set_caption("WPython Demo")

    sceneDemo = Scene(screen, time)
    sceneDemo.start()


if __name__ == "__main__":
    play(10)
