from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from User import ImageUploaderApp
from registration import RegistrationPage
import mysql.connector

login_kv = '''
<LoginPage>:
    MDTextField:
        id: username_field
        hint_text: "Username"
        pos_hint: {"center_x": 0.5, "center_y": 0.7}
        size_hint_x: 0.5
        icon_right: 'heart-pulse'

    MDTextField:
        id: password_field
        hint_text: "Password"
        password: True
        pos_hint: {"center_x": 0.5, "center_y": 0.6}
        size_hint_x: 0.5
        icon_right: 'heart-pulse'

    MDRectangleFlatButton:
        text: "Login"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        on_press: root.login_handler()

    MDLabel:
        text: "Don't have an account? Register here"
        halign: "center"
        pos_hint: {"center_x": 0.5, "center_y": 0.35}
        on_ref_press: root.go_to_registration()
'''

# Load the KV string
Builder.load_string(login_kv)

# Define the LoginPage class
class LoginPage(Screen):
    def login_handler(self):
        username = self.ids.username_field.text
        password = self.ids.password_field.text
        print("Username:", username)
        print("Password:", password)
        
        try:
            database = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database="skindiseasesystem"
            )
            cursor = database.cursor()

            # Executing SQL query to fetch user from database
            query = "SELECT * FROM register WHERE username = %s AND password = %s"
            cursor.execute(query, (username, password))
            result = cursor.fetchone()

            if result:
                print("Login successful")
                self.goto_main_page()
            else:
                print("Invalid username or password")

        except mysql.connector.Error as error:
            print("Error while connecting to MySQL:", error)

        finally:
            # Closing the database connection
            if 'database' in locals():
                database.close()
                print("MySQL connection closed")
                
    def goto_main_page(self):
        app = MDApp.get_running_app()
        app.root.current = "image_uploader_page"       

    def go_to_registration(self):
        # Switch to the registration page
        app = MDApp.get_running_app()
        app.root.current = "registration_page"  


class SkinDiseaseDetectionApp(MDApp):
    def build(self):      
        self.theme_cls.primary_palette = "Blue"
        self.screens = {
            "login_page": LoginPage(),
            "registration_page": RegistrationPage(),
            "image_uploader_page": ImageUploaderApp()
        }
        return self.screens["login_page"]

if __name__ == "__main__":
    SkinDiseaseDetectionApp().run()
