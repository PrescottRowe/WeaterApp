import kivy
kivy.require('1.1.3')

from kivy.properties import NumericProperty
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.scatter import Scatter
from kivy.uix.treeview import TreeView, TreeViewLabel
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty
from kivy.clock import Clock
import random


class SearchScreen(Screen):
    def __init__(self, **kwargs):
        super(SearchScreen, self).__init__(**kwargs)


    def debug(self, val):
        if val:
            try:
                enterd = str(val)
                popup = Popup(title='Test popup',
                              content=Label(text=str(enterd)),
                              size_hint=(None, None), size=(150, 150))
                popup.open()
            except Exception:
                entered="error"
                popup = Popup(title='Test popup',
                              content=Label(text=str(entered)),
                              size_hint=(None, None), size=(100, 100))
                popup.open()

class ForecastScreen(Screen):
    def __init__(self, **kwargs):
        super(ForecastScreen, self).__init__(**kwargs)
    def getForecast(self,location):
        self.location=location

class ScreenManagement(ScreenManager):
    pass

pressentation = Builder.load_file("Weather.kv")
class WeatherApp(App):#app class must match kv file minus "app"
    def build(self):#pass the instance of the class to the function so it knows it parent.
        return pressentation


if __name__ == "__main__":#only autorun the code if the file is being run as main.
    WeatherApp().run()