import tensorflow as tf
from tensorflow import keras
import numpy as np
from keras.models import load_model
import io
from PIL import Image
from keras.utils import img_to_array, load_img

pne_model = load_model("pneumonia.h5")
cat_model = load_model("cateract.h5")


class DetectAI:
    def __init__(self, image_data):
        image = Image.open(io.BytesIO(image_data))
        target_size = (224, 224)
        image = image.convert("RGB").resize(target_size)
        image_array = img_to_array(image)
        self.parsed_image = image_array[np.newaxis]

    def detect_pneumonia(self):
        class_indices = {0: 'NORMAL', 1: 'PNEUMONIA'}
        preds = pne_model.predict(self.parsed_image)
        prob = round(preds.flatten()[tf.argmax(preds, axis=1).numpy()[0]] * 100, 3)
        result = class_indices.get(tf.argmax(preds, axis=1).numpy()[0])
        return f"The result of detection is : {result} with a probability of {prob} %."

    def detect_cateract(self):
        class_indices = {0: 'CATARACT', 1: 'NORMAL'}
        image = self.parsed_image / 255.0
        preds = cat_model.predict(image)
        prob = round(preds.flatten()[tf.argmax(preds, axis=1).numpy()[0]] * 100, 3)
        result = class_indices.get(tf.argmax(preds, axis=1).numpy()[0])
        return f"The result of detection is : {result} with a probability of {prob} %."
