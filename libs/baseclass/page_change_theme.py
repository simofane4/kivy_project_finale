import os

from kivy.properties import StringProperty
from kivy.uix.modalview import ModalView
from kivy.utils import get_color_from_hex, get_hex_from_color

from kivymd.color_definitions import colors, palette
from kivymd.theming import ThemableBehavior


class MainAppBasePage(ThemableBehavior, ModalView):
    pass


class MainAppDialogDev(MainAppBasePage):
    pass








class MainAppPageChangeTheme(MainAppBasePage):
    def set_list_colors_themes(self):
        for name_theme in palette:
            self.ids.rv.data.append(
                {
                    "viewclass": "MainAppOneLineLeftWidgetItem",
                    "color": get_color_from_hex(colors[name_theme]["500"]),
                    "text": name_theme,
                }
            )
