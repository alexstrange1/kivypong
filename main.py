from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.textinput import TextInput

class ScrButton(Button):
    def __init__(self, screen, direction, goal, **kwargs):
        super().__init__(**kwargs)

        self.screen = screen 
        self.direction = direction
        self.goal = goal

    def on_press(self):
        self.screen.manager.transition.direction = self.direction
        self.screen.manager.current = self.goal 

class MainScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        layout = BoxLayout(orientation="vertical")
        layout.add_widget(ScrButton(self, "up", "first", text = "1"))
        layout.add_widget(ScrButton(self, "up", "second", text = "2"))
        layout.add_widget(ScrButton(self, "up", "third", text = "3"))
        layout.add_widget(ScrButton(self, "up", "fourth", text = "4"))
        self.add_widget(layout)

class FirstScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        layout = BoxLayout()
        lb = Label(text="first screen")
        back = ScrButton(self, "down", "main", text="back")
        layout.add_widget(lb)
        layout.add_widget(back)
        self.add_widget(layout)

class SecondScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        layout = BoxLayout()
        lb = Label()
        field = TextInput()
        btn_ok = Button(text="OK")
        btn_back = ScrButton(self, "right", "main", text="back")
        layout.add_widget(self.lb)
        layout.add_widget(field)
        layout.add_widget(btn_ok)
        layout.add_widget(btn_back)
        self.add_widget(layout)
        btn_ok.on_press = self.change_text
    def change_text(self):
        new_text = self.field.text
        self.lb.text = new_text

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        main_scr = MainScreen(name="main")
        sm.add_widget(main_scr)
        sm.add_widget(FirstScreen(name="first"))
        sm.add_widget(FirstScreen(name="second"))

        return sm

MyApp().run()