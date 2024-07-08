from kivymd.app import MDApp
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.button import MDRoundFlatButton
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.core.window import Window
import tensorflow as tf
from keras.preprocessing import image
from kivy.lang import Builder
import numpy as np

KV = '''
<UserPage>:
    orientation: 'vertical'

    Image:
        id: image_widget
        size: 224, 224
        size_hint: None, None

    MDRoundFlatButton:
        text: "Upload Image"
        halign: 'center'
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        on_release: app.open_file_manager()
'''

Builder.load_string(KV)

class MyBoxLayout(BoxLayout):
    pass

class ImageUploaderApp(MDApp):
    def build(self):
        self.layout = MyBoxLayout()
        return self.layout

    def open_file_manager(self):
        file_manager = MDFileManager(
            exit_manager=self.exit_file_manager,
            select_path=self.select_path,
        )
        file_manager.show('D:/Documents/ICS Project II')

    def exit_file_manager(self, *args):
        self.file_manager.close()

    def select_path(self, path):
        print(f"Selected path: {path}")
        self.display_selected_image(path)
        self.predict_image(path)

    def display_selected_image(self, path):
        self.root.ids.image_widget.source = path

    def preprocess_image(self, image_path):
        img = image.load_img(image_path, target_size=(224, 224))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        return img_array

    def load_model(self):
        model = tf.keras.models.load_model('capsule_model.h5')
        return model

    def predict_image(self, image_path):
        model = self.load_model()
        img_array = self.preprocess_image(image_path)
        predictions = model.predict(img_array)
        print("Predictions:", predictions)

if __name__ == '__main__':
    ImageUploaderApp().run()