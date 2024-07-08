from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp


class DemoApp(MDApp):
    def build(self):
        screen = Screen()
        table = MDDataTable(pos_hint={'center_x':0.5,'center_y':0.5}, size_hint=(0.9, 0.6), check=True,
            column_data =[
                  ("No.", dp(18)),
                  ("Food", dp(30)),
                  ("Calories", dp(30))
            ],
                row_data=[
                   ("1","Burger", "300"),
                   ("2","Oats","150")
               ]
            )
        table.bind(on_check_press=self.check_press)
        table.bind(on_check_press=self.row_press)
        screen.add_widget(table)
        return screen
    
    def check_press(self,instance_table,current_row):
        print(instance_table,current_row)

    def row_press(self,instance_table,instance_row):
        print(instance_table,instance_row)
    
DemoApp().run()
