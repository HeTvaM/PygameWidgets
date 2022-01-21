# import basic library
import sys
import pygame
from typing import List, Optional, Tuple

# import user's library
from .abstract import AbsPanel
from .logger import terminal_print_cls, termimal_print, log_print_cls, log_print
from .constpack import WHITE, BLACK, GRAY

from decorate import tools, check_size, check_key, is_active, count


#>------------SUMMARY----------------<
# Library of widgets for the paygame library.
# The library provides extensive options for layout and customization of widgets. As well as optimized solutions for their rendering
# While available:
# -Menu( just control button and text)
# -Entry
# -Progressbar
# -Button
# -Label
# -Text
# -Font
#
# Coming soon:
# -Buttons menu
# -Panels
# -Complete menu
# -Drop-Down Button
#>------------SUMMARY----------------<


#-----------------Progressbar--------------
class Progressbar(AbsPanel):
    def __init__(self, screen, x, y, text, color = WHITE,
                 dots=[0,10], steps=10, time=60, rColor = GRAY,
                 width=500, height=70, img_active=None, img_disactive=None, music=None,
                 function=None
                 ):
        super().__init__(screen, x, y, text, color,
                         width, height, img_active, img_disactive, music,
                         function)

        self.dots = dots
        self.steps = steps
        self.time = time

        self.res = 0
        self.key = True
        self.count = 0

        self.rect_color = rColor
        self.rect_size = [(width - 20) / steps, height-10]
        self.rect_add = pygame.Rect(x,y,self.rect_size[0]*self.res, self.rect_size[1])
        self.text_pos = [self.x + width//2 - width//8, self.y + height + 10]
        self.text.change_text(f"{self.dots[0]}/{self.dots[1]}")

    def avto(cls):
        cls.res += 1
        cls.rect_add.update(cls.x+10,cls.y+5,cls.rect_size[0]*cls.res, cls.rect_size[1]) #= pg.Rect(x,y,self.rect_size[0]*self.res, self.rect_size[1])
        if cls.res > cls.steps-1:
            cls.text.change_text(f"{cls.dots[1]}\{cls.dots[1]}")
            cls.key = False
            return cls.func()

        str = f"{(cls.dots[1]//cls.steps)*cls.res}\{cls.dots[1]}"
        cls.text.change_text(str)

    @count(2, avto)
    def status(self):
        if self.key:
            return True

    @is_active
    def update(self, *args):
        self.status()
        self.out_box()

        pygame.draw.rect(self.screen, self.rect_color, self.rect_add)
        self.text.draw(*self.text_pos)

    def set_res(self, res):
        self.res = res

    def get_res(self):
        return self.res

    def func(self):
        self.function()

#------------------------------------

#------------------Entry--------------
class Entry(AbsPanel):
    def __init__(self, screen, x, y, text, color = WHITE,
                 width=300, height=110, img_active=None, img_disactive=None, music=None
                 ):
        super().__init__(screen, x, y, text, color,
                         width, height, img_active, img_disactive, music)

        self.focus = False
        self.input_text = ""
        self.text.change_text("")

        # Звук кнопки, флаг звука
        self.music = music
        self.music_key = True

        self.count = 0
        self.res= 1

    def check_add(self):
        if (self.count)// 35 % 2 == self.res and self.count != 0:
            try:
                if self.input_text[-1] == "|":
                    self.input_text = self.input_text[:-1]
            except IndexError:
                pass

            if self.res == 1:
                self.input_text += "|"
            if self.res == 0:
                self.count = 0

            self.res = 1 - self.count // 35 % 2

        self.text.change_text(self.input_text)

    @is_active
    def update(self, *args):
        if self.focus:
            self.in_box()
            self.check_add()

            self.count += 1
        else:
            self.out_box()

        self.text.draw_in_obj(self.x, self.y)

    @check_key
    def add_key(self, key):
        self.input_text += key

    @check_key
    def delete_key(self):
        self.input_text = self.input_text[:-1]

    @check_key
    def end_key(self):
        self.focus = False

    @check_key
    def get(self):
        return self.input_text

#----------------------------------------------


#----------------------BUTTON------------------------------

class Button(AbsPanel):
    """
    Класс отвечающий за создание анимированных кнопок
    """
    def __init__(self, screen, x, y, text, color=WHITE,                                  #Основные параметры
                 width=300, height=110, img_active=None, img_disactive=None, music=None, #Параметры для кнопки
                 function=None                                                           #Функция кнопки
                 ):
        #Иницилизация родительского класса
        super().__init__(screen, x, y, text, color, \
                         width, height, img_active, img_disactive, music,
                         function
                         )
        self.active = True

    @is_active
    def update(self, *args) -> any:
        """Каждый кадр

        Обновляем состояние кнопки
        """
        mouse = args[0]

        if self.x < mouse[0] < self.x + self.width and self.y < mouse[1] < self.y + self.height:
            self.in_box()
        else:
            self.out_box()

        self.text.draw_in_obj(self.x, self.y)

    def get_amount(self):
        return 1

#------------------------------------------------------------------------


#---------------------LABEL-----------------------
class Label(AbsPanel):
    def __init__(self, screen, x, y, text, color = WHITE,
                 width=300, height=110, img_disactive=None
                 ):
        super().__init__(screen, x, y, text, color, \
                         width, height, img_disactive=img_disactive
                         )

    def update(self, *args) -> any:
        self.draw_img()
        self.text.draw_in_obj(self.x, self.y)

    @tools()
    def draw_img(self) -> any:
        return self.img_active

    def change_text(self, text: str) -> any:
        pass


#------------------------TEXT------------------------------
class ObjsText():
    def __init__(self, screen, texts: List[str], font=None,
                 font_color=GRAY, font_type=None, font_size=50, text_location="C",
                 indents=None, text_indents=None
                 ):
        self.screen = screen
        self.amount = len(texts)
        self.texts = texts

        self.font = font
        self.fonts_setting = [font,
                              font_color, font_type, font_size, text_location,
                              indents
                              ]

        self.list = []
        self.coords_list = [self.font.get_size(texts[i]) for i in range(self.amount)]

        self.step = None
        self.text_indents = text_indents

        self.create_texts()

    def create_texts(self):
        for text in range(self.amount):
            obj = Text(self.screen, self.texts[text], *self.fonts_setting)
            self.list.append(obj)

    def get_texts(self):
        return self.list

    def get_coords(self):
        return self.coords_list

    def update(self, *args):
        self.draw(self.coords)

    #@check_size
    def draw(self, coords = None) -> None:
        if self.step is not None:
            for i in range(self.amount):
                if self.type:
                    x = self.x + (self.coords_list[i][0]+self.step)*i
                    y = self.y
                else:
                    x = self.x
                    y = self.y + (self.coords_list[i][1]+self.step)*i


                self.list[i].draw(x, y)
        else:
            for i in range(self.amount):
                self.list[i].draw(*coords)

    def draw_in_obj(self):
        pass

    def manual_draw(self, coords):
        self.coords = coords

    def auto_draw(self, x: int, y: int, step: int, type: int, location="C"):
        self.x, self.y = x, y
        self.step = step
        self.type = type
        self.location = location

#-----------------------------------------------------------

#--------------TEXT-----------------
class Text():
    def __init__(self, screen, text, font=None,                                             #Основные параметры
                 font_color=GRAY, font_type=None, font_size=50, text_location="C",          #Цвет, Шрифт, Размер, Выравнивание
                 indents=None                                                               #Отступы
                 ):
        # Экран отрисовки
        self.screen = screen

        # Расположение и цвет текста
        self.text_location = text_location
        self.font_color = font_color

        #Оступы
        self.activate_indent(indents)

        # Рендер текста для вывода
        self.text = text
        if font is None:
            self.font = Font(font_type, font_color, font_size)
        else:
            self.font = font

        self.text_to_render = self.font.render(text)


    def change_font(self, font: Optional[pygame.font.Font]) -> any:
        self.font = font
        self.text_to_render = self.font.render(self.text)

    def change_text(self, text:str) -> any:
        self.text = text
        self.text_to_render = self.font.render(text)


    def activate_indent(self, indents: List[int]) -> any:
        if indents is not None:
            self.indent_x, self.indent_y = indents[0], indents[1]
            self.isIndent = True
        else:
            self.indent_x, self.indent_y = 0, 0
            self.isIndent = False


    def location(self, *btn_sizes: List[int]) -> any:
        def check(x,y,curX_size):
            if x > btn_sizes[0] or y > btn_sizes[1]:
                raise ValueError(f"Font size more then button size! SIZE: Button{btn_sizes}, \
Text{x,y}. Please change button or font size.")

            if self.text_location == "C":
                indent = curX_size//2
            elif self.text_location == "R":
                indent = curX_size - 10
            elif self.text_location == "L":
                indent = 10
            else:
                raise ValueError("Font location incorrect! Please check font location!")

            return indent

        def auto_indent():
            size = self.font.get_size(self.text)
            x, y = size[0], size[1]
            curX_size = btn_sizes[0] - x

            self.indent_x += check(x,y,curX_size)
            self.indent_y += (btn_sizes[1] - y) // 2

        if self.isIndent is not True:
            auto_indent()
        else:
            pass

    def get_size(self):
        return print(self.font.get_size(self.text))


    def draw(self, x:int, y:int) -> None:
        """
        Отображает текст на экране
        """
        self.screen.blit(self.text_to_render, (x, y))

    def draw_in_obj(self, x:int, y:int) -> None:
        """
        Отображет текст на каком-то объекте с отступами
        """
        self.screen.blit(self.text_to_render, (x+self.indent_x, y+self.indent_y))


#----------------------------------------------------------


#--------------FONT-------------------------
class Font():
    def __init__(self, type, color, size,
                 *args, **kwargs
                 ):

        self.type = type
        self.color = color
        self.size = size

        self.font = pygame.font.Font(type, size, *args)

    def render(self, text: str) -> any:
        return self.font.render(text, True, self.color)

    def get_color(self):
        return self.color

    def get_size(self, text:str) -> List[int]:
        return self.font.size(text)

    def set_color(self, color):
        self.color = color

#------------------------------------------------



"""
#----------------PANEL---------------------

class ObjPanel():
    def __init__(self, screen, images, coords, texts):
        self.screen = screen
        self.images = images
        self.coords = coords
        self.texts = texts

        self.list_panel = []

    def create(self):
        for i in range(len(self.images())):
            pnl = Panel(self.screen, self.images[i], self.coords[i], self.texts[i])

            self.list_panel.append(pnl)

    def update(self):
        for pnl in self.list_panel:
            pnl.update()

"""


"""
#--------------Drop-Dowm Button-------------
class DDownButton(AbsPanel):
    @staticmethod
    def check(dict):
        try:
            return dict[0:3]
        except IndexError:
            return dict

    def __init__(self, screen, x, y, text, type_texts, color = WHITE,
                 width=300, height=110, img_active=None, img_disactive=None, music=None
                 ):
        super().__init__(screen, x, y, text, color,
                         width, height, img_active, img_disactive, music
                         )
        print(type_texts)
        self.rect_drop = pygame.Rect(x, y, width-10, height-10)
        self.type_texts = type_texts
        self.len = len(type_texts)
        self.n = 1
        self.coords = [(x+x*i, y+y*i) for i in range(1, self.len)]
        print("COORDS", self.coords)
        self.flag = False
        self.rects = [pg.Rect(i[0], i[1], width-10, height-10) for i in check(self.coords)]

    def click(self, mouse):
        if self.flag is False:
            if self.x < mouse[0] < self.x + self.width and self.y < mouse[1] < self.y + self.height:
                self.flag = True

        else:
            for coord in check(self.coords):
                x, y = self.x + coord[0], self.y + coord[1]
                if x < mouse[0] < x + (self.width-10) and x < mouse[1] < y + (self.height-10):
                    self.change_text()

            self.flag = False

    def change_text(self):
        self.text.change_text(self.type_texts[n])
        self.n += 1

        if self.n > self.len:
            self.n = 0

    @is_active
    def update(self, *args):
        mouse = args[0]

        if self.x < mouse[0] < self.x + self.width and self.y < mouse[1] < self.y + self.height:
            self.in_box()
        else:
            self.out_box()

        self.text.draw_in_obj(self.x, self.y)

        if self.flag is True:
            for num, rect in enumerate(check()):
                pygame.draw.rect(self.screen, self.rect_color, rect)
                self.texts[num+1]

"""

#---------------------PANEL-----------------------
"""
class Panel(AbsPanel):
    def __init__(self, screen, x, y,
                 width=600, height=600, image=None,
                 objs_text=None, tX = None, tY = None, step=None, type=None, location="C"
                 ):
        super().__init__(screen, x, y, None, width, height, img_disactive=image)
        self.screen = screen

        self.objs_text = objs_text
        self.objs_text.auto_draw(tX, tY, step, type, location)

    def chech_text(self):
        def check():
            coords = self.objs_text.get_size()
            indents = self.objs_text.text_indents
            x, y = self.width, self.height

            for text in range(self.objs_text.amount):
                x += indents[0]
                y += indents[1]
                if coords[text][0] > x and coords[text][1] > y:
                    raise ValueError(f"Size ERROR. Text size Text more then panel size{self.obj_texts[text].text}. \
                    Text{coords[text]} Panel{self.width, self.height}. Indents{indents}")

            pass
        pass

    #@tools
    def draw(self):
        pass

    def update(self):
        self.objs_text.draw_in_obj()
"""

#----------------------------------------------------------
