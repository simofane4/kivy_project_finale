import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout

from kivymd.uix.floatlayout import MDFloatLayout


from kivy.lang import Builder
from kivymd.app import MDApp


class MainAppRegister(MDScreen):

    def back_to_login_screen(self):
        self.root.ids.screen_manager.current = "login"