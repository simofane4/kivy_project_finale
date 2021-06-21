from kivy.properties import ListProperty, StringProperty
from kivy.uix.widget import Widget

from kivymd.uix.list import (
    ILeftBody,
    IRightBodyTouch,
    OneLineAvatarListItem,
    OneLineIconListItem,
    TwoLineAvatarListItem,
)
from kivymd.uix.selectioncontrol import MDCheckbox


class MainAppOneLineLeftAvatarItem(OneLineAvatarListItem):
    divider = None
    source = StringProperty()


class MainAppTwoLineLeftAvatarItem(TwoLineAvatarListItem):
    icon = StringProperty()
    secondary_font_style = "Caption"


class MainAppTwoLineLeftIconItem(TwoLineAvatarListItem):
    icon = StringProperty()


class MainAppOneLineLeftIconItem(OneLineAvatarListItem):
    icon = StringProperty()


class MainAppOneLineIconListItem(OneLineIconListItem):
    icon = StringProperty()


class MainAppOneLineLeftWidgetItem(OneLineAvatarListItem):
    color = ListProperty()


class LeftWidget(ILeftBody, Widget):
    pass


class IconRightSampleWidget(IRightBodyTouch, MDCheckbox):
    pass
