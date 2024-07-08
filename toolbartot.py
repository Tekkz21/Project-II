from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.toolbar import MDTopAppBar,MDBottomAppBar
from kivy.core.window import Window

Window.size = (400, 600)


screen_helper = """
Screen:
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            pos_hint: {'top':0.8}
            title: 'Demo Application'
            left_action_items: [["menu", lambda x: app.navigation_draw()]]
        MDLabel:
            text: 'Hello World'
            halign: 'center'
"""

class DemoApp(MDApp):
    
    def build(self):
        
        screen = Builder.load_string(screen_helper)
        return screen
    
    def navigation_draw(self):
        print("Navigation")
    
DemoApp().run()