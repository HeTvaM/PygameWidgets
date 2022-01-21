# import basic libs
import sys
import pygame

# import user's libs
from Widgets import Font, Text, Button


#>------------SUMMARY----------------<
#
#>------------SUMMARY----------------<



class Menu():
    def __init__(self, screen, x, y, step, type=0,):
        # Экран отрисовки
        self.screen = screen

        self.x = x
        self.y = y
        self.text_x = 0
        self.text_y = 0
        self.step = step
        self.type = type

        self.btn_width = width
        self.btn_height = height

        self.btn_list = []
        self.text_list = [0]*2

    def create_buttons(self, obj_texts,
                       width=300, height=110, img_active=None, img_disactive=None, music=None,
                       functions=None):
        self.width = width
        self.height = height
        amount = len(obj_texts.list)

        if (img_active and img_disactive) is not None:
            img_active = pygame.transform.scale(img_active, (width,height))
            img_disactive = pygame.transform.scale(img_disactive, (width,height))
        else:
            img_active, img_disactive = None, None

        self.functions = [None for i in range(amount)] if function is None else functions

        for i in range(amount):
            if self.type:
                x = self.x + (width+self.step)*i
                y = self.y
            else:
                x = self.x
                y = self.y + (height+self.step)*i

            btn = Button(self.screen, x, y, obj_texts.list[i], WHITE,
                         width, height, img_active, img_disactive, music,
                         self.functions[i])
            self.btn_list.append(btn)

    def create_texts(self, text, location="C"):
        size = text.get_size()
        if location == "C":
            self.text_x = self.x + (self.width - size[0])/2
            self.text_y = self.y - size[1] - 20

    def update(self, *args):
        self.text.draw(self.text_x, self.text_y)
        for btn in self.btn_list:
            btn.update(args[0])

    def get_amount(self):
        return self.amount

    def get_list(self):
        return self.btn_list

#---------------------------------------------------------
