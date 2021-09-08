import pygame


#------------------Menu----------------------------

class MenuManager():
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




#-----------------------Buttons---------------------------

class Button:
    """
    Класс отвечающий за создание анимированных кнопок
    """
    def __init__(self,screen,                                                                                        #Основные параметры
                 width=300, height=110, img_active=None, img_disactive=None, music=None, function=None, text=None):  #Дополнительные параметры
        #Иницилизируем экран
        self.screen = screen

        #Опредяем ширину и высоту кнопок
        self.width = width
        self.height = height

        #Опредяем изображение кнопок
        self.active = img_active
        self.disactive = img_disactive

        #Опредяем звук выбраной кнопки, иницилизируем ключ для звука
        self.music = music
        self.music_key = True

        #Опредяем текст и функцию кнопки
        self.text = text
        self.function = function

        #Опредяем нажатие кнопки
        self.key = False


    def update(self, x, y, text="!"):
        """
        Обновляем состояние кнопки
        """
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
            if self.music_key and self.music != None:
               self.music.play()
               self.music_key = False

            self.screen.blit(self.active, (x,y))
            self.key = True
        else:
            self.screen.blit(self.disactive, (x,y))
            self.music_key = True
            self.key = False


        self.render_text(text, x+35,y+35)

    def start(self):
        """
        Определение нажимал ли пользователь на кнопку
        """
        if self.key == True:
            return self.function
        else:
            return False


    def draw(self, x, y, font_color = (0,0,0), font_type=None, font_size=55):
        """
        Прорисовка текста
        """
        #Иницилизация объкта
        self.x = x
        self.y = y

        self.f_c = font_color
        self.f_t = font_type
        self.f_s = font_size

        self.render_text("!",x+5,y+25)


    def render_text(self,text,x,y):
        """
        Вывод текст на экран
        """
        if text != "!":
            self.text = text

        font_type = pygame.font.Font(self.f_t, self.f_s)
        text = font_type.render(self.text, True, self.f_c)
        self.screen.blit(text, (x, y))




#-------------------Text-----------------

class Text():
    def __init__(self, text, screen,                                       #Основные параметры
                 color_font=(230,230,0), type_font=None, size_font = 60):  #Дополнительные параметры
        #Иницилизация текста и экрана
        self.text = text
        self.screen = screen

        #Иницилизируем параметры текст цвет, шрифт, размер
        self.font_color = color_font
        self.font_type = type_font
        self.font_size = size_font

    def draw(self, x, y, text=None):
        """
        Отображет текст на экране
        """
        #Если текст передаётся пустой, то пишётся старый
        if text != None:
            self.text = text

        font = pygame.font.Font(self.font_type, self.font_size)
        text = font.render(self.text, True, self.font_color)
        self.screen.blit(text, (x,y))


if __name__=="__main__":
    pass