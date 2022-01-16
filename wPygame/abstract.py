# init basic library
import os
import sys
import pygame as pg

from abc import ABC, abstractmethod

# init user's library
from constpack import WHITE, BLACK, GRAY
from .decorate import tools

#>------------SUMMARY----------------<
# This module contains asbractic classes that simplify code relationships.
# AbsPanel - an asbstrack class that is used as the basis for a widget
# that can contain a rectangle, text, image, click, update
#>------------SUMMARY----------------<

# ABC class for button and label
class AbsPanel(ABC):
    def __init__(self, screen, x, y, text, color = WHITE,                                    #Основные параметры
                 width=300, height=110, img_active=None, img_disactive=None, music = None,   #Параметры для кнопки
                 function=None,                                                              #Функция кнопки
                 ):
        # Экран отрисовки
        self.screen = screen

        # Координаты кнопки на экране
        self.coords(x,y)

        # Текст кнопки
        self.text = text
        self.text.location(width, height)

        # Ширина и высота кнопки
        self.width = width
        self.height = height

        # Изображение кнопки (При наведении и обычная)
        self.img_active = img_active
        self.img_disactive = img_disactive

        # Звук и функция виджета
        self.music = music
        self.music_key = True
        self.function = function

        # Счётчик времени исполнения какой-то функции
        self.count = 0

        # Цвет панели
        self.COLOR = color

        # Флаг, что панель можно наблюдать
        self.active = True

        # Прямоугольная область если не будет изображения
        if img_disactive is None:
            self.rect = pg.Rect(x,y,width,height)

    def coords(self, *args):
        self.x, self.y = args[0], args[1]

    def click(self, mouse):
        if self.x < mouse[0] < self.x + self.width and self.y < mouse[1] < self.y + self.height:
            return True if self.function is None else self.function

        return False

    @tools()
    def in_box(self):
        if self.music_key and self.music:
            self.music.play()
            self.music_key = False

        return self.img_active

    @tools()
    def out_box(self):
        self.music_key = True

        return self.img_disactive

    def activate(self):
        self.active = True

    def disactivate(self):
        self.active = False

    @abstractmethod
    def update(self):
        pass



class Scene(ABC):
    def __init__(self, screen, time):
        self.sc = screen
        self.clock = pg.time.Clock()
        self.time = time

    def check_event(self, widgets):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            self.check(event, widgets)

    def check_time(self, time):
        if time//30 > self.time:
            pg.quit()
            sys.exit()

    def start(self):
        play = True
        time = 0
        widget = self.create_widget()
        cursor = pg.mouse.set_cursor(*pg.cursors.arrow)
        while play:
            self.check_time(time)
            self.clock.tick(60)
            self.check_event(widget)
            time += 1

            mouse = pg.mouse.get_pos()

            self.sc.fill((0,0,0))
            self.update(widget, mouse)
            pg.display.flip()

    @abstractmethod
    def check(self, *args):
        pass

    @abstractmethod
    def create_widget(self):
        pass

    @abstractmethod
    def update(self, *args):
        pass
