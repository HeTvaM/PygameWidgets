#import main library
import pygame
#from Player import Figure

"""
class Stat():
    def __init__(self,colors, text):
        self.text = text

        self.colors = colors
        self.figures = []

    def create():
        for i in range(1,8):
            fig  = figure(self.colors, i)
            self.figures.append(fig)
"""

# Проиницилизируем несколько базовых цветов
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)

# Константы



class objMenu():
    def __init__(self, screen, clock, posX, posY, step, width, height,                                      #Основные параметры
                 type=0, text=[], functions=[], fon=None, img_active=None, img_disactive=None, sound=None): #Дополнительные параметры
        #Иницилизая экрана и таймера
        self.screen = screen
        self.clock = clock

        #Тип разположения кнопок меню
        self.type = type

        #Текст кнопок и их функционал
        self.text = text
        self.functions = functions

        #Ширина и длина кнопок
        self.w = width
        self.h = height

        #Расположение меню и отступы между кнопками
        self.x = posX
        self.y = posY
        self.step = step

        #Изображение кнопок и звук
        self.img_active = img_active
        self.img_disactive = img_disactive
        self.sound = sound

        #Задний фон для меню
        self.fon = fon

        #Параметры для работы алгоритма
        self.xlist = []
        self.ylist = []
        self.txtlist = []


    def InitText(self, text, x, y):
        """
        Выводит текст меню
        """
        #Добавлет координаты текст в общий массив координат
        self.xlist.append(x)
        self.ylist.append(y)

        #Cоздаёт текст на экране и добавляет его в общий массив текста
        new = Text(text, self.screen)
        self.txtlist.append(new)

    def update(self):
        """
        Обновляет меню для отрисовки
        """
        k = 0
        #Отрисовывает текст из массива текста
        for i in self.txtlist:
            i.draw(self.xlist[k],self.ylist[k])
            k += 1


    def start(self, fon_img=None, key=1):
        """
        Запускает меню, реализовывает расположение, нажатие кнопок, апдейт и прорисовку
        """
        #Класс меню для настроек кнопок
        menu = Menu(self.screen, len(self.functions), self.type, self.x, self.y, self.step,
                    self.w, self.h, self.sound, self.img_active, self.img_disactive,
                    self.functions, self.text)

        play = True
        while play:

            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    #Проверка нажатия ЛКМ
                    if event.button == 1:
                        #Проверят в списке кнопок, на какую из них нажали
                        for i in range(menu.n):
                            k = menu.btn_list[i].start()
                            #Запоминает функцию кнопки и останавливает цикл
                            if k != False:
                                play = False
                                next_function = k


            if fon_img != None:
                self.screen.blit(fon_img,(0,0))
            elif key:
                self.screen.fill((0,0,0))

            menu.update()
            self.update()

            pygame.display.flip()

        #Проверяет существует ли функция запомненая при нажатии на кнопку
        try:
            #Запускает следующую функцию
            next_function()
        except TypeError:
            pass


class Menu():
    def __init__(self, screen, texts,                                                     #Экран и текст
                 amount, x, y, distance, type=0,                                          #Параметры меню
                 width=300, height=110, img_active=None, img_disactive=None, music=None,  #Параметры кнопки
                 functions=[],                                                            #Параметры кнопки                                                         #Текст
                 ):
        # Экран отрисовки
        self.screen = screen

        self.amount = amount
        self.type = type

        self.x = x
        self.y = y
        self.step = distance

        self.btn_width = width
        self.btn_height = height

        if self.img_active:
            self.img_active = pygame.transform.scale(img_active, (width,height))
            self.img_disactive = pygame.transform.scale(img_disactive, (width,height))

        self.music = music

        self.texts = texts
        if not functions:
            self.functions = [None for i in range(amount)]
        else:
            self.functions = functions


        self.btn_list = []
        self.coords_list = []

        self.create()

    def create(self):
        for i in range(self.amount):
            if self.type:
                x =self.x + (self.x+self.step)*i
            else:
                y =self.y + (self.y+self.step)*i

            btn = Button(self.screen, x, y, self.texts[i],
                         self.btn_width, self.btn_height, self.img_active, self.img_disactive, self.music,
                         self.functions[i]
            )
            self.btn_list.append(btn)

    def update(self):
        for btn in self.btn_list:
            btn.update()


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


class Panel(pygame.sprite.Sprite):
    def __init__(self, screen, image, x, y, text=None):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y

        self.screen = screen
        self.text = text

    def update(self):
        if self.text != None:
            self.text.draw(self.rect.left, self.rect.top)

#-------------------------------------------------------


#--------------------BUTTON-----------------------------

class Button:
    """
    Класс отвечающий за создание анимированных кнопок
    """
    def __init__(self, screen, x, y, text,                                               #Основные параметры
                 width=300, height=110, img_active=None, img_disactive=None, music=None, #Параметры для кнопки
                 function=None,                                                          #Функция кнопки
                 ):
        # Экран отрисовки
        self.screen = screen

        # Координаты кнопки на экране
        self.Coords(x,y)

        # Текст кнопки
        self.text = text
        self.text.loacation(width, height)

        # Ширина и высота кнопки
        self.width = width
        self.height = height

        # Изображение кнопки (При наведении и обычная)
        self.img_active = img_active
        self.img_disactive = img_disactive

        # Звук кнопки, флаг звука
        self.music = music
        self.music_key = True

        # Функцию кнопки
        self.function = function

        # Флаг нажатия кнопки
        self.key = False

    @coords.setter
    def coords(self, *coords):
        self.x = coords[0]
        self.y = coords[1]

    def update(self):
        """Каждый кадр

        Обновляем состояние кнопки

        """
        mouse = pygame.mouse.get_pos()
        #click = pygame.mouse.get_pressed()

        if self.x < mouse[0] < self.x + self.width and self.y < mouse[1] < self.y + self.height:
            in_box()
        else:
            out_box()

        self.text.draw(self.x, self.y)

    def is_click(self):
        """На клик

        Определение нажимал ли пользователь на кнопку

        """
        if self.key:
            return self.function

        return False

    def tools(self,func):
        def wrapper():
            obj = func()

            if obj:
                self.screen.blit(obj, (self.x,self.y))
            else:
                rect = pygame.Rect(self.x, self.x+self.width, self.y, self.y + self.height)
                pygame.draw.Rect(self.screen, GRAY, rect)
        return wrapper

    @tools
    def in_box(self):
        if self.music_key and self.music != None:
           self.music.play()
           self.music_key = False

        self.key = True

        return self.img_active

    @tools
    def out_box(self):
        self.music_key = True
        self.key = False

        return self.img_disactive

#------------------------------------------------------------------------


#------------------------TEXT------------------------------

class ObjText():
    def __init__(self, screen, amount, texts,
                 *fonts_setting
                 ):
        self.screen = screen
        self.amount = amount
        self.texts = texts

        self.font_setting

        self.list = []

    def create_texts(self):
        for text in range(amount):
            obj = Text(self.screen, self.texts[i], *self.font_setting)
            self.list.append(obj)

    def get_texts(self):
        return self.list


class Text():
    def __init__(self, screen, text,                                                          #Основные параметры
                 font_color=GRAY, font_type=None, font_type = 50, font_location="C",          #Цвет, Шрифт, Размер, Выравнивание
                 indents = None                                                               #Отступы
                 ):
        # Экран отрисовки
        self.screen = screen

        # Расположение и цвет текста
        self.font_location = font_location
        self.font_color = font_color

        #Оступ
        self.indents = indents

        # Рендер текста для вывода
        self.font = pygame.font.Font(font_type, font_size)
        self.text_to_render = self.font.render(text, True, font_color)

    def activate_indent(self):
        self.indent_x = self.indents[0]
        self.indent_y = self.indents[1]

    def location(self, *sizes):
        def check():
            if x > sizes[0] and y > size[1]:
                raise ValueError("Font size more then button size! Please check font size")

            if self.font_location == "C":
                indent = curX_size//2
            elif self.font_location == "R":
                indent = 10
            elif self.font_location == "L":
                indent= curX_size  - 10
            else:
                raise ValueError("Font location incorrect! Please check font location!")

            return indent

        size = self.font.size()
        x = size[0]
        y = size[1]
        curX_size = sizes[0] - x

        self.indent_x = check()
        self.indent_y = (sizes[1] - y) // 2

    def draw(self, x, y):
        """
        Отображет текст на экране
        """
        self.screen.blit(self.text_to_render, (x+self.indent_x, y+self.indent_y))

#----------------------------------------------------------
