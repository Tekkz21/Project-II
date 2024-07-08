from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFloatingActionButton
from kivy.uix.screenmanager import Screen, ScreenManager
from User import ImageUploaderApp
from kivymd.uix.filemanager import MDFileManager
from keras.preprocessing import image
from kivymd.toast import toast 
import tensorflow as tf
import numpy as np
import mysql.connector


main_kv = '''   
<SplashScreen>:
    MDFloatingActionButton:
        icon: 'heart-pulse'
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        on_press:
            root.manager.transition.direction = 'left'
            root.manager.current = 'registration'       
<RegistrationScreen>:
    MDTextField:
        id: name_field
        hint_text: "name" 
        pos_hint: {"center_x": 0.5, "center_y": 0.8}
        size_hint_x: 0.5
        icon_right: 'heart-pulse'

    MDTextField:
        id: age_field
        hint_text: "age"
        pos_hint: {"center_x": 0.5, "center_y": 0.7}
        size_hint_x: 0.5
        icon_right: 'heart-pulse'

    MDTextField:
        id: username_field
        hint_text: "username"
        pos_hint: {"center_x": 0.5, "center_y": 0.6}
        size_hint_x: 0.5
        icon_right: 'heart-pulse'

    MDTextField:
        id: county_field
        hint_text: "county"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        size_hint_x: 0.5
        icon_right: 'heart-pulse'

    MDTextField:
        id: password_field
        hint_text: "password"
        password: True
        pos_hint: {"center_x": 0.5, "center_y": 0.4}
        size_hint_x: 0.5
        icon_right: 'heart-pulse'

    MDRectangleFlatButton:
        text: "Register"
        pos_hint: {"center_x": 0.5, "center_y": 0.3}
        on_press:
            root.manager.transition.direction = 'left'
            root.manager.current = 'login'
            root.register_handler()

    MDRectangleFlatButton:
        text: "Already have an account? Login here"
        halign: "center"
        pos_hint: {"center_x": 0.5, "center_y": 0.20}
        on_press:
            root.manager.transition.direction = 'left'
            root.manager.current = 'login'
        
<LoginPage>:
    MDTextField:
        id: username_field
        hint_text: "username"
        pos_hint: {"center_x": 0.5, "center_y": 0.7}
        size_hint_x: 0.5
        icon_right: 'heart-pulse'

    MDTextField:
        id: password_field
        hint_text: "password"
        password: True
        pos_hint: {"center_x": 0.5, "center_y": 0.6}
        size_hint_x: 0.5
        icon_right: 'heart-pulse'

    MDRectangleFlatButton:
        text: "Login"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        on_press:
            root.manager.transition.direction = 'left'
            root.login_handler()

    MDRectangleFlatButton:
        text: "Don't have an account? Register here"
        halign: "center"
        pos_hint: {"center_x": 0.5, "center_y": 0.35}
        on_press:
            root.manager.transition.direction = 'left'
            root.manager.current = 'registration'
                
<UserScreen>:
    orientation: 'vertical'
    MDLabel:
        text: "This page requires you to upload your image using the 'upload image' button"
        halign: "center"
        pos_hint: {"center_x": 0.5, "center_y": 0.75}
    Image:
        id: image_widget
        size: 224, 224
        size_hint: None, None

    MDRectangleFlatButton:
        text: "Upload Image"
        icon: "folder"
        halign: 'center'
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        on_press: root.open_file_manager()
'''


Builder.load_string(main_kv)



class SplashScreen(Screen):
    pass
    '''def go_to_registration_page(self):
        app = MDApp.get_running_app()
        app.root.current = "registration_page" '''


class RegistrationScreen(Screen):
    def register_handler(self):
        # Handle registration logic here
        name = self.ids.name_field.text
        age = self.ids.age_field.text
        username = self.ids.username_field.text
        county = self.ids.county_field.text
        password = self.ids.password_field.text
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
            app.root.current = "login"
            
class LoginPage(Screen):
    pass
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
        app.root.current = "user"       

    def go_to_registration(self):
        # Switch to the registration page
        app = MDApp.get_running_app()
        app.root.current = "registration"  

class UserScreen(Screen):
    pass
    def open_file_manager(self):
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_file_manager,
            select_path=self.select_path
         
        )
        self.file_manager.show('C:/Users/Tekkz/Pictures')
        self.manager_open = True

    def exit_file_manager(self, *args):
        self.file_manager.close()

    def select_path(self, path):
        print(f"Selected path: {path}")
        self.display_selected_image(path)
        self.predict_image(path)
        toast(path)

    def display_selected_image(self, path):
        screen_manager = self.parent
        image_widget = screen_manager.get_screen('user').ids.image_widget
        
        image_widget.source = path

    def preprocess_image(self, image_path):
        img = image.load_img(image_path, target_size=(224, 224))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array /= 255.0
        return img_array

    def load_model(self):
        model = tf.keras.models.load_model('capsule_model.h5')
        return model

    def predict_image(self, image_path):
        model = self.load_model()
        img_array = self.preprocess_image(image_path)
        predictions = model.predict(img_array)
        print("Predictions:", predictions)



class SkinDiseaseDetectionApp(MDApp):
    
    def build(self):
        sm = ScreenManager()
        sm.add_widget(SplashScreen(name='splash'))
        sm.add_widget(RegistrationScreen(name='registration'))
        sm.add_widget(LoginPage(name='login'))
        sm.add_widget(UserScreen(name='user'))
        
        
        return sm

if __name__ == '__main__':
    SkinDiseaseDetectionApp().run()