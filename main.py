from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout

class layout(FloatLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.b1 = Button(
            text="Option 1",
            size_hint=(1, .3),
            background_color=(10, 10, 35, 1),
            color=(0, 0, 0, 1),
            pos_hint={"x":0.3, "y":0.6}

        )
        self.b2 = Button(
            text="Option 2",
            size_hint=(1, .3),
            background_color=(10, 10, 35, 1),
            color=(0, 0, 0, 1),
            pos_hint = {"x":0.3, "y":0.3}


        )
        self.b3 = Button(
            text="Option 3",
            size_hint=(1, .3),
            background_color=(10, 10, 35, 1),
            color=(0, 0, 0, 1),
            pos_hint = {"x":0.3, "y":0}


        )
        self.add_widget(self.b1)
        self.add_widget(self.b2)
        self.add_widget(self.b3)

class appl(App):

    def build(self):


        return layout()

appl().run()
