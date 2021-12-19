# import basic library
import pygame as pg
import sys

# import user library
from WPygame import Font, Text, Button, Label, Menu, ObjsText, ObjsMenu, Entry
from logger import log, log_with_return
from constpack import GRAY, BLACK, EMERALD
from constpack import arial, vivaldi, comicsansms

#>------------SUMMARY----------------<
# this module is used to test and provide a demo of how the library works.
# Soon there will be a flexible system of settings and full-fledged demo scenes.
# Wait!
#>------------SUMMARY----------------<

# const
KEYS = ["right shift", "left shift", "right alt", "left alt",
        "right ctrl", "left ctrl", "num lock", "caps lock"]

# Main class
class Scene:
    def __init__(self, screen, time):
        self.sc = screen
        self.clock = pg.time.Clock()
        self.time = time

    def create_btn(self, func):
        font = Font(comicsansms, EMERALD, 40)
        text = Text(self.sc, "IT's WORK", font=font)
        btn = Button(self.sc, 100, 400, text, color=GRAY, function=func)

        return btn

    def create_entry(self):
        font = Font(comicsansms, EMERALD, 40)
        text = Text(self.sc, "", font=font, text_location="L")
        btn = Entry(self.sc, 100, 200, text, color=GRAY)

        return btn

    def create_text(self):
        text_list = ["IT's WORK",
                     "Hello WORLD!",
                     "My name is Danila"
                     ]
        font = Font(comicsansms, EMERALD, 25)
        text = ObjsText(self.sc, text_list, font=font)
        text.auto_draw(x=500, y=250, step=10, type=0)
        return text

    def create_menu(self):
        text_list = ["IT's WORK",
                     "Hello WORLD!",
                     "My name is Danila"
                     ]
        font = Font(comicsansms, EMERALD, 25)
        text = ObjsText(self.sc, text_list, font=font)
        menu = Menu(self.sc, 3, 25, 200, 25, text, type=1,
                    width=300, height=110
                    )

        return menu

    def full_menu(self):
        text_text = ["MENU"]
        text_btn = ["Play",
                    "Setting",
                    "Exit"]
        font = Font(comicsansms, EMERALD, 50)
        font_btn = Font(arial, GRAY, 40)

        objs_text = ObjsText(self.sc, text_btn, font=font)

        objs_menu = ObjsMenu(self.sc, self.clock)
        objs_menu.init_text(text_text, [300, 150], font=font)
        objs_menu.init_button(3, 250, 250, 50, objs_text)

        return objs_menu

    def check_event_entry(self, obj, btn, id):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse = pg.mouse.get_pos()
                    res = obj.click(mouse)
                    obj.focus = res
                    if res:
                        id = obj
                        break
                    else:
                        obj.end_key()

                    res = btn.click(mouse)
                    if res is not False:
                        res()


            if event.type == pg.KEYDOWN:
                if id.focus:
                    if event.key == pg.K_BACKSPACE:
                        id.delete_key()
                    elif event.key == pg.K_RETURN:
                        id.end_key()
                        id.focus = False
                    else:
                        if event.key == pg.K_SPACE:
                            key = " "
                        elif event.key == pg.K_TAB:
                            key = "   "
                        else:
                            key = pg.key.name(event.key)
                            if key in KEYS: key = ""
                        id.add_key(key)
        return id


    def check_event_obj(self, obj):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse = pg.mouse.get_pos()
                    for i in range(obj.get_amount()):
                        try:
                            evt = obj.btn_list[i].click(mouse)
                        except AttributeError:
                            evt = obj.click(mouse)
                        print(evt)

    def check_event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

    def check_time(self, time):
        if time//30 > self.time:
            pg.quit()
            sys.exit()

    def start(self):
        def btn():
            text_ = text.text[0:3] +" "+ input_btn.get()
            text.change_text(text_)
        #menu = self.full_menu()

        #menu.start()

        play = True
        time = 0
        input_btn = self.create_entry()
        id = None
        text = Text(self.sc, "Hi!")
        btn = self.create_btn(btn)
        #text = self.create_text()
        #menu = self.create_menu()
        cursor = pg.mouse.set_cursor(*pg.cursors.arrow)
        while play:
            self.check_time(time)
            self.clock.tick(60)
            time += 1

            mouse = pg.mouse.get_pos()
            id = self.check_event_entry(input_btn, btn, id)
            #self.check_event_obj(btn)
            #self.check_event_obj(menu)

            self.sc.fill((0,0,0))

            input_btn.update()

            text.draw(450, 300)
            #text.draw()
            btn.update(mouse)
            #menu.update(mouse)
            pg.display.flip()



def play(time):
    pg.init()
    screen = pg.display.set_mode((800,800))
    pg.display.set_caption("WPython Demo")

    sceneDemo = Scene(screen, time)
    sceneDemo.start()


if __name__ == "__main__":
    play(10)
