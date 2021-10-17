# import basic library
import pygame as pg
import sys

# import user library
from WPygame import Font, Text, Button, Label
from logger import log, log_with_return
from constpack import GRAY, BLACK, EMERALD
from constpack import arial, vivaldi, comicsansms

#>------------SUMMARY----------------<
# this module is used to test and provide a demo of how the library works.
# Soon there will be a flexible system of settings and full-fledged demo scenes.
# Wait!
#>------------SUMMARY----------------<

# Main class
class Scene:
    def __init__(self, screen, time):
        self.sc = screen
        self.clock = pg.time.Clock()
        self.time = time

    def create_btn(self):
        font = Font(comicsansms, EMERALD, 40)
        text = Text(self.sc, "IT's WORK", font=font)
        btn = Button(self.sc, 200, 200, text, color=GRAY)

        return btn

    def check_event(self, obj):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                print("quit")
                pg.quit()
                sys.exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    evt = obj.click()
                    print(evt)

    def check_time(self, time):
        if time//30 > self.time:
            pg.quit()
            sys.exit()

    def start(self):
        play = True
        time = 0
        #text = Text(self.sc, "DEMO")
        btn = self.create_btn()
        cursor = pg.mouse.set_cursor(*pg.cursors.arrow)
        while play:
            self.check_time(time)
            self.clock.tick(60)
            time += 1
            mouse = pg.mouse.get_pos()
            self.check_event(btn)

            self.sc.fill((0,0,0))

            #text.draw(200, 200)
            btn.update(mouse)
            pg.display.flip()


def play(time):
    pg.init()
    screen = pg.display.set_mode((800,800))
    pg.display.set_caption("WPython Demo")

    sceneDemo = Scene(screen, time)
    sceneDemo.start()


if __name__ == "__main__":
    play()
