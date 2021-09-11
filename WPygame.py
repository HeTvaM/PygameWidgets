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
    def __init__(self, screen, count, typeMenu, posX_first, posY_first, step, width, height, music, img_active, img_disactive, functions, list_text, typeBtn=0):
        self.screen = screen

        self.n = count
        self.typeMenu = typeMenu
        self.typeBtn = typeBtn

        self.x = posX_first
        self.y = posY_first
        self.step = step

        self.btn_w = width
        self.btn_h = height

        self.music = music
        self.img_active = pygame.transform.scale(img_active, (width,height))
        self.img_disactive = pygame.transform.scale(img_disactive, (width,height))

        self.list_function = functions
        self.list_text = list_text

        self.btn_list = []
        self.label_list = []

        self.create()

    def create(self):
        if self.typeBtn == 0:
            for i in range(self.n):
                i = Button(self.screen,
                           self.btn_w, self.btn_h, self.img_active, self.img_disactive, self.music,
                           self.list_function[i], self.list_text[i])
                self.btn_list.append(i)
        else:
            for i in range(self.n):
                i = Button_multi(self.screen,
                                 self.btn_w, self.btn_h, self.img_active, self.img_disactive, self.music,
                                 self.list_function[i], self.list_text[i])
                self.btn_list.append(i)

        self.draw()

    def draw(self):
        if self.typeMenu == 1:
            x = self.x
        else:
            y = self.y

        for i in range(self.n):
            if self.typeMenu == 1:
                y = self.y + (self.btn_h+self.step)*i
            else:
                x = self.x + (self.btn_w+self.step)*i

            self.btn_list[i].draw(x,y)

    def update(self):
        if self.typeMenu == 1:
            x = self.x
        else:
            y = self.y

        for i in range(self.n):
            if self.typeMenu == 1:
                y = self.y + (self.btn_h+self.step)*i
            else:
                x = self.x + (self.btn_w+self.step)*i

            self.btn_list[i].update(x,y,"!")


    def create_text(self, text):
        new = Text(text, self.screen)
        self.label_list.append(new)

    def draw_text(self, x, y):
        for i in range(len(self.label_list)):
            self.label_list[i].draw(x[i],y[i])


class Panel(pygame.sprite.Sprite):
    def __init__(self, image, posX, posY, number, text=None, screen=None, font_type=None, font_color = (255,255,255), font_size = 35):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.left = posX
        self.rect.top = posY

        self.screen = screen
        self.num = number
        self.text = text

        self.font_type = font_type
        self.font_color = font_color
        self.font_size = font_size

    def render_text(self,x,y,stepX, stepY,text):
        font = pygame.font.Font(self.font_type, self.font_size)
        text = font.render(text, True, self.font_color)
        self.screen.blit(text, (x+stepX,y-stepY))

    def update(self,text=None,stepX=15, stepY=50):
        if self.text != None:
            self.render_text(self.rect.left, self.rect.bottom, stepX, stepY, text[self.num])


class Button:
    """
    Класс отвечающий за создание анимированных кнопок
    """
    def __init__(self, screen, x, y,                                                     #Основные параметры
                 width=300, height=110, img_active=None, img_disactive=None, music=None, #Параметры для кнопки
                 text_obj=None, font_location = "C",                                     #Параметры для текста
                 function=None, text=None,                                               #Параметры для функицонала
                 ):
        # Экран отрисовки
        self.screen = screen

        #Расположение кнопки на экране
        self.Coords(x,y)

        # Ширина и высота кнопки
        self.width = width
        self.height = height

        # Изображение кнопки (При наведении и обычная)
        self.img_active = img_active
        self.img_disactive = img_disactive

        # Звук кнопки, ключ звука
        self.music = music
        self.music_key = True

        # Текст и положение на кнопке
        self.text_obj = text_obj

        # Текст и функцию кнопки
        self.text = text
        self.function = function

        # Ключ нажатия кнопки
        self.key = False

        self.location(font_location)

    @coords.setter
    def coords(self, *coords):
        self.x = coords[0]
        self.y = coords[1]

    def location(self, indent):
        size = self.font.size()
        x = size[0]
        y = size[1]
        curX_size = self.width - x

        if x > self.width and y > self.height:
            raise ValueError("Font more then button! Chech value pleas")

        if indent == "C":
            index_x = curX_size//2
        elif indent == "R":
            index_x = 10
        elif indent == "L":
            index_x = curX_size  - 10

        self.x_text = self.x + index_x
        self.y_text = self.y + (self.height - y) // 2

    def tools(self,func):
        def wrapper(x,y):
            obj = func(x,y)

            if obj:
                self.screen.blit(obj, (x,y))
            else:
                pygame.draw.Rect(self.screen, GRAY, (x, x + self.width, y, y + self.height))
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

    def update(self, x, y, text="!"):
        """Каждый кадр

        Обновляем состояние кнопки

        """
        mouse = pygame.mouse.get_pos()
        #click = pygame.mouse.get_pressed()

        if self.x < mouse[0] < self.x + self.width and self.y < mouse[1] < self.y + self.height:
            in_box()
        else:
            out_box()

        self.text_obj.draw(self.x_text, self.y_text)


    def is_click(self):
        """На клик

        Определение нажимал ли пользователь на кнопку

        """
        if self.key:
            return self.function

        return False


class Button_multi(Button):
    def __init__(self, screen, width, height, img_active, img_disactive, music, function, texts):
        Button.__init__(self, screen, width, height, img_active, img_disactive, music, function)

        self.n = 0
        self.texts = texts

        self.text = texts[0]

    def check(self):
        if self.key == True:
            self.n += 1
            if self.n == 4:
                self.n = 0

            self.text = self.texts[self.n]


class Text():
    def __init__(self, screen, text,                                       #Основные параметры
                 font_color=(230,230,0), font_type=None, font_type = 60):  #Дополнительные параметры
        # Экран отрисовки
        self.screen = screen

        # Рендер текста для вывода
        self.font_color = font_color
        self.font = pygame.font.Font(font_type, font_size)
        self.text_to_render = self.font.render(text, True, font_color)


    def draw(self, x, y):
        """
        Отображет текст на экране
        """
        self.screen.blit(self.text_to_render, (x,y))

"""
class MultiText(Text):
    def __init__(self, *data):    #data - information to main class
        super().__init__(*data)

    def update_text(self, text):
        self.text_to_render = self.font.render(text, True, self.font_color)
"""


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
