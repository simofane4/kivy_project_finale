from kivy.metrics import dp
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.screen import MDScreen
from kivy.properties import ObjectProperty
from kivymd.uix.button import MDFlatButton
from kivymd.app import MDApp
from kivy.lang import builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from kivy.animation import Animation
from kivy.metrics import dp
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.screen import MDScreen
from kivy.properties import ObjectProperty
from kivymd.uix.button import MDFlatButton


from kivymd.uix.dialog import MDDialog
class MainAppLogi(MDScreen):
    def anim(self, widget):
        anim = Animation( pos_hint={"centery": 1.16} )
        anim.start( widget )

    def anim1(self, widget):
        anim = Animation( pos_hint={"centery": .85} )
        anim.start( widget )