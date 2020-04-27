from app import main
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

Builder.load_string("""
<MainScreen>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            color: 0,0,0,1
    FloatLayout:
        Label:
            text: 'Roll Dice'
            pos: -10, 200
        Button:
            background_color: 0, 0, 0, 0
            size_hint: 0.1,0.1
            pos_hint: {'center_x': .5, 'center_y': .5}             
            text: 'Play Now!'
            on_press: root.run_script
            on_release: print("Done")

""")

class MainScreen(Screen):
    def run_script():
        return app.main()


sm = ScreenManager(transition=FadeTransition())
sm.add_widget(MainScreen(name='main'))

class TestApp(App):
    def build(self):
        return sm

if __name__ == '__main__':
    TestApp().run()

            #source: '/home/jrob/Wallpapers/karersee_lake_dolomites_mountains_italy-wallpaper-1280x1024.jpg'