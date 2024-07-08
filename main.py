from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFloatingActionButton
from registration import RegistrationPage
from kivy.uix.screenmanager import Screen, ScreenManager
from User import ImageUploaderApp

# Load the kv file containing the widget tree
main_kv ='''
<RootWidget>:
    MDFloatingActionButton:
        icon: 'heart-pulse'
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        on_press: root.manager.current ='registartion'
'''

Builder.load_string(main_kv)

class RootWidget(Screen):
    def go_to_registration_page(self):
        app = MDApp.get_running_app()
        app.root.current = "registartion_page"

class SkinDiseaseDetectionApp(MDApp):
   
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        
        sm = ScreenManager()
        sm.add_widget(RootWidget(name='splash'))
        
        return sm


        
if __name__ == '__main__':
    SkinDiseaseDetectionApp().run()
