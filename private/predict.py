import cv2
import numpy as np
from tensorflow import keras

model_1 = keras.models.load_model('model')
print("Loaded model from disk")

image_type_labels = {
    0 :'public',
    1 : 'private'}

img_pred = cv2.imread("sample.jpg")
input_array = []
resized_img_pred = cv2.resize(img_pred, (224, 224)) # Resizing the images to be able to pass on MobileNetv2 model
input_array.append(resized_img_pred)

input_array = np.array(input_array)
input_array= input_array/255

y_pred_img = model_1.predict(input_array, batch_size=64, verbose=1)
y_pred_bool_img = np.argmax(y_pred_img, axis=1)
prediction = image_type_labels[y_pred_bool_img[0]]
print(prediction)
