"""
    Use this file, as well as other files you may create in this folder,
    for code directly related to the app view.
"""

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
# from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from controller import controller

# Set window size
Window.size = (450, 750)

# Or you may prefer this way:

# from kivy.config import Config
#
# Config.set('graphics', 'width', '450')
# Config.set('graphics', 'height', '750')
# Config.write()

# Builder.load_file('./view/my.kv')


class AppScreenManager(ScreenManager):

    categories = ObjectProperty(None, allownone=True)
    category_form = ObjectProperty(None, allownone=True)

    """
        Get the items from the database and display them on the ScrollView
    """
    def set_item_list(self):

        items = controller.get_items()

        for item in items:
            self.ids.list.add_widget(Button(text=item.name, id=str(item.id), color=(0, 0, 0, 1),
                        background_color=(.9, 9, 9, 0), font_size=30,
                        halign='left', size_hint_y=None, height=30))

    """
        Set the values for the Category spinner
    """
    def set_categories(self):
        self.categories = controller.get_categories()
        for cat in self.categories:
            self.ids.categories.values.append(cat.name)

    def add_category(*args):
        print(args)
        root = args[0]
        if not root.category_form.name.text:
            return

        controller.add_category({
            'name': root.category_form.name.text,
        })

        root.ids.categories.values = []
        root.set_categories()
        root.cancel_category()

    def cancel_category(self, *args):
        self.ids.input_area.remove_widget(self.category_form)
        self.category_form = None

    def open_category_form(self, *args):
        self.category_form = CategoryForm(self)
        self.ids.input_area.add_widget(self.category_form)

    def add_item(self):
        if not self.ids.item.text:
            return
        cat = [c for c in self.categories if c.name == self.ids.categories.text][0]
        controller.add_item({"name": self.ids.item.text, "cat_id": cat.id})
        self.ids.item.text = ''
        self.ids.list.clear_widgets()
        self.set_item_list()

    def __init__(self, *args):
        super(AppScreenManager, self).__init__(*args)

        self.ids.scroll.size = (200, Window.height)
        self.ids.list.bind(minimum_height=self.ids.list.setter('height'))

        self.set_categories()
        self.set_item_list()

class CategoryForm(GridLayout):
    def __init__(self, root, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        self.name = TextInput(hint_text='Name of category')
        self.add_widget(self.name)
        self.add_widget(Button(text='Add', on_press=root.add_category))
        self.add_widget(
            Button(text='Cancel', on_press=root.cancel_category))
        self.cols = 1
        self.spacing = 5
        self.size_hint = (0.9, 0.3)
        self.pos_hint = {'x': .05, 'y': .5}

class MyApp(App):
    def build(self):
        return AppScreenManager()
