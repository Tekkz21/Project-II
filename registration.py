from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivy.uix.screenmanager import ScreenManager
import mysql.connector

# Load the kv file containing the widget tree
"""
Builder.load_string('''
<RegistrationPage>:
    MDTextField:
        hint_text: "Name"
        pos_hint: {"center_x": 0.5, "center_y": 0.8}
        size_hint_x: 0.5
        icon_right: 'heart-pulse'

    MDTextField:
        hint_text: "Age"
        pos_hint: {"center_x": 0.5, "center_y": 0.7}
        size_hint_x: 0.5
        icon_right: 'heart-pulse'

    MDTextField:
        hint_text: "Username"
        pos_hint: {"center_x": 0.5, "center_y": 0.6}
        size_hint_x: 0.5
        icon_right: 'heart-pulse'

    MDTextField:
        hint_text: "County"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        size_hint_x: 0.5
        icon_right: 'heart-pulse'

    MDTextField:
        hint_text: "Password"
        password: True
        pos_hint: {"center_x": 0.5, "center_y": 0.4}
        size_hint_x: 0.5
        icon_right: 'heart-pulse'

    MDRectangleFlatButton:
        text: "Register"
        pos_hint: {"center_x": 0.5, "center_y": 0.3}
        on_press: root.register_handler()

    MDLabel:
        text: "Already have an account? Login here"
        halign: "center"
        pos_hint: {"center_x": 0.5, "center_y": 0.20}
        on_ref_press: root.go_to_login()
''')



class RegistrationPage(Screen):
    def register_handler(self):
        # Handle registration logic here
        name = self.children[0].text
        age = self.children[1].text
        username = self.children[2].text
        county = self.children[3].text
        password = self.children[4].text
        print("Registration details:", name, age, username, county, password)

        # connection to MySQL database
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database="skindiseasesystem"
            )

            cursor = connection.cursor()

            # executing SQL query to insert data
            insert_query = "INSERT INTO register (name, age, username, county, password) VALUES (%s, %s, %s, %s, %s)"
            insert_values = (name, age, username, county, password)
            cursor.execute(insert_query, insert_values)

            # commit changes to the database
            connection.commit()
            print("Registration successful")

        except mysql.connector.Error as error:
            print("Error while connecting to MySQL:", error)

        finally:
            # closing db connection
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MYSQL connection closed")

    def go_to_login(self):
        app = MDApp.get_running_app()
        app.root.current = "login_page"


class SkinDiseaseDetectionApp(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(RegistrationPage(name ='registration'))
        
        return sm

if __name__ == "__main__":
    SkinDiseaseDetectionApp().run()
"""