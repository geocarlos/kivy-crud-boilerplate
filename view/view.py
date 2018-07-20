"""
    Use this file, as well as other files you may create in this folder,
    for code directly related to the app view.
"""

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

Builder.load_file('./view/MyApp.kv')

class AppScreenManager(ScreenManager):
    pass

class MyApp(App):
    def build(self):
        return AppScreenManager()
