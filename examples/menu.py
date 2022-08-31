# import basic library
import pygame as pg
import sys

# import user library
from WPygame.menu import Menu
from WPygame.Widgets import Font, Text
from WPygame.logger import log, log_with_return
from WPygame.constpack import GRAY, BLACK, EMERALD
from WPygame.constpack import arial, vivaldi, comicsansms

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

    def create_text():
        font = Font(comicsansms, EMERALD, 40)
        text = Text(self.sc, "Menu", font=font)

        return text

    def create_objText():
        texts = ["Начать", "Настройки", "Выйти"]
        font = Font(comicsansms, EMERALD, 40)
        objtext = objText(self.sc, texts, font=font)

        return objText

    def create_widget(self):
        menu = Menu(self.sc, 100, 50)
        menu.create_btn(create_objText())
        menu.create_text(create_text())


    def check_event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

    def start(self):
        play = True
        time = 0
        cursor = pg.mouse.set_cursor(*pg.cursors.arrow)
        while play:
            self.check_time(time)
            self.clock.tick(60)
            time += 1

            mouse = pg.mouse.get_pos()

            self.sc.fill((0,0,0))

            pg.display.flip()


def play(time):
    pg.init()
    screen = pg.display.set_mode((800,800))
    pg.display.set_caption("WPython Demo")

    sceneDemo = Scene(screen, time)
    sceneDemo.start()


if __name__ == "__main__":
    play(10)
