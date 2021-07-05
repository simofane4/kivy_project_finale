import ast

import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
import sys
from pathlib import Path
from kivy.core.window import Window
from kivy.factory import Factory  
from kivy.lang import Builder
from kivy.loader import Loader
from libs.baseclass.login import MainAppLogin
from libs.baseclass.page_change_theme import (
    MainAppPageChangeTheme,
   
)
from libs.baseclass.list_items import (  # NOQA: F401
    MainAppOneLineLeftIconItem,
)


from kivymd.app import MDApp

from kivymd import images_path


os.environ["KIVY_PROFILE_LANG"] = "1"



# hna der variable  path bach nkhdem fra7ti min nbda  ntesti

if getattr(sys, "frozen", False):  # bundle mode with PyInstaller
    os.environ["MAINAPP_ROOT"] = sys._MEIPASS
else:
    sys.path.append(os.path.abspath(__file__).split("demos")[0])
    os.environ["MAINAPP_ROOT"] = str(Path(__file__).parent)
    # os.environ["MAINAPP_ROOT"] = os.path.dirname(os.path.abspath(__file__))

os.environ["MAINAPP_ASSETS"] = os.path.join(
    os.environ["MAINAPP_ROOT"], f"assets{os.sep}"
)


Window.softinput_mode = "below_target"




# hadi lmaine  app dyali 

class MainApp(MDApp):
    

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.primary_palette = "Teal"
        self.page_change_theme = None
        self.toolbar = None
        self.data_screens = {}
        # to add image  i think  for icon  app 
        Loader.loading_image = f"{images_path}transparent.png"


    def build(self):
        # hna  7eded les  file  kv hadi la list des page 
        Builder.load_file(
            os.path.join(
                os.environ["MAINAPP_ROOT"], "libs", "kv", "list_items.kv"
            )
        )
        # hna  3tito la  page  min ybda  
        return Builder.load_file(
            os.path.join(
                os.environ["MAINAPP_ROOT"], "libs", "kv", "start_screen.kv"
            )
        )

    

    def show_page_change_theme(self):
        if not self.page_change_theme:
            self.page_change_theme = MainAppPageChangeTheme()
            self.page_change_theme.set_list_colors_themes()
        self.page_change_theme.open()

    def on_start(self):

        """Creates a list of page on start screen."""

        Builder.load_file(
            os.path.join(
                os.environ["MAINAPP_ROOT"],
                "libs",
                "kv",
                "page_change_theme.kv",
            )
        )
# 3aytlna hna les file t3na
        with open(
            os.path.join(os.environ["MAINAPP_ROOT"], "screens_data.json")
        ) as read_file:
            self.data_screens = ast.literal_eval(read_file.read())
            data_screens = list(self.data_screens.keys())
            data_screens.sort()
        for name_item_example in data_screens:
            self.root.ids.backdrop_front_layer.data.append(
                {
                    "viewclass": "MainAppOneLineLeftIconItem",
                    "text": name_item_example,
                    "icon": self.data_screens[name_item_example]["icon"],
                    "on_release": lambda x=name_item_example: self.set_example_screen(
                        x
                    ),
                }
            )
        
        self.root.ids.screen_manager.current = "login"


    def set_example_screen(self, name_screen):
        manager = self.root.ids.screen_manager
        if not manager.has_screen(
            self.data_screens[name_screen]["name_screen"]
        ):
            name_kv_file = self.data_screens[name_screen]["kv_string"]
            Builder.load_file(
                os.path.join(
                    os.environ["MAINAPP_ROOT"],
                    "libs",
                    "kv",
                    f"{name_kv_file}.kv",
                )
            )
            if "Import" in self.data_screens[name_screen]:
                exec(self.data_screens[name_screen]["Import"])
            screen_object = eval(self.data_screens[name_screen]["Factory"])
            self.data_screens[name_screen]["object"] = screen_object
            if "toolbar" in screen_object.ids:
                screen_object.ids.toolbar.title = name_screen
            manager.add_widget(screen_object)
        manager.current = self.data_screens[name_screen]["name_screen"]
    
        



        
    def back_to_home_screen(self):
        self.root.ids.screen_manager.current = "home"

    def switch_theme_style(self):
        self.theme_cls.theme_style = (
            "Light" if self.theme_cls.theme_style == "Dark" else "Dark"
        )
        self.root.ids.backdrop.ids._front_layer.md_bg_color = [0, 0, 0, 0]
        
 # hado homa les button li fl

 
    def open_home_screen(self):
        self.root.ids.screen_manager.current = "home"

    def open_register_screen(self):
        self.root.ids.screen_manager.current = "register"

    def back_to_login_screen(self):
        self.root.ids.screen_manager.current = "login"


MainApp().run()