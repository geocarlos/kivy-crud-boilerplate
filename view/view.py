"""
    Use this file, as well as other files you may create in this folder,
    for code directly related to the app view.
"""

from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        return Button(text='Hello, Kivy!')
