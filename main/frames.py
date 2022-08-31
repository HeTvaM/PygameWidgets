# import basic libs
import sys
import pygame

# import user's libs
from .Widgets import Font, Text, Button


#>------------SUMMARY----------------<

#>------------SUMMARY----------------<


class Frame:
    def __init__(self, screen, clock,
                 FPS=30, img_fon=None, sound=None
                 ):
        self.screen = screen
        self.clock = clock

        self.FPS = FPS
        self.img_fon = img_fon
        self.sound = sound

        self.list = {}

    def init_text(self, texts, coords, is_auto = False,
                  step=None, type=None, location="C",
                  font=None, font_color=GRAY, font_type=None, font_size=50, text_location="C",
                  indents=None, text_indents=None
                  ):
        obj = ObjsText(self.screen, texts, font,
                       font_color=GRAY, font_type=None, font_size=50, text_location="C",
                       indents=None, text_indents=None )
        if is_auto is True:
            try:
                obj.auto_draw(coords[0], coords[1], step, type, location)
            except:
                raise ValueError(f"Something wrong with coords. Please be confirmed that you\
                give only x and y coords. YOUR COORDS {coords}")
        else:
            obj.manual_draw(coords)

        self.list["TEXT"] = obj

    def init_button(self, amount, x, y, step, obj_texts, type=0,
                    width=300, height=110, img_active=None, img_disactive=None, music=None,
                    functions=[]
                    ):
        obj = Menu(self.screen, amount, x, y, step, obj_texts, type,
                   width, height, img_active, img_disactive,  music,
                   functions)

        self.list["BUTTON"] = obj

    def init_label(self):
        pass
    def init_panel(self):
        pass

    def update(self, mouse):
        for obj in self.list.values():
            obj.update(mouse)

    def start(self):
        try:
            clickable = [self.list.get("BUTTON")]
        except:
            pass

        cursor = pygame.mouse.set_cursor(*pygame.cursors.arrow)

        play = True
        while play:

            self.clock.tick(self.FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    #Проверка нажатия ЛКМ
                    if event.button == 1 and clickable[0] is not None:
                        #Проверят в списке кнопок, на какую из них нажали
                        for objs in clickable:
                            for obj in objs.get_list():
                                func = obj.click()
                                #Запоминает функцию кнопки и останавливает цикл
                                if func is not False:
                                    play = False
                                    next_func = func


            if self.img_fon is None:
                self.screen.fill(BLACK)
            elif key:
                self.screen.blit(self.img_fon,(0,0))

            mouse = pygame.mouse.get_pos()
            self.update(mouse)

            pygame.display.flip()

        #Проверяет существует ли функция запомненая при нажатии на кнопку
        try:
            #Запускает следующую функцию
            next_func()
        except TypeError:
            pass
