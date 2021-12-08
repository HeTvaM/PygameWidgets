# init basic library
import os
import pygame as pg

from abc import ABC, abstractmethod

# init user's library
from constpack import WHITE, BLACK, GRAY

#>------------SUMMARY----------------<
#
#
#
#
#
#>------------SUMMARY----------------<

# ABC class for button and label
class AbsPanel(ABC):
    def __init__(self, screen, x, y, text, color = WHITE,                                 #Основные параметры
                 width=300, height=110, img_active=None, img_disactive=None,             #Параметры для кнопки
                 function=None,                                                          #Функция кнопки
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

        # Цвет панели
        self.COLOR = color

        # Прямоугольная область если не будет изображения
        if img_disactive is None:
            self.rect = pg.Rect(x,y,width,height)

    def coords(self, *args):
        self.x, self.y = args[0], args[1]

    def click(self):
        return None

    @abstractmethod
    def update(self):
        pass
