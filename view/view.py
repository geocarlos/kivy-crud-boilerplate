"""
    Use this file, as well as other files you may create in this folder,
    for code directly related to the app view.
"""

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.core.window import Window

# Set window size
Window.size = (450, 750)

# Or you may prefer this way:

# from kivy.config import Config
#
# Config.set('graphics', 'width', '450')
# Config.set('graphics', 'height', '750')
# Config.write()

Builder.load_file('./view/MyApp.kv')


class AppScreenManager(ScreenManager):
    def __init__(self, *args):
        super(AppScreenManager, self).__init__(*args)

        # Set the scroll view, so it may, well, scroll
        self.ids.scroll.size = (200, Window.height)
        self.ids.list.bind(minimum_height=self.ids.list.setter('height'))

        for i in range(100):
            self.ids.list.add_widget(Button(text="Test %s" % i, id=str(i), color=(0, 0, 0, 1),
                        background_color=(.9, 9, 9, 0),
                        halign='left', size_hint_y=None, height=30))

class MyApp(App):
    def build(self):
        return AppScreenManager()
