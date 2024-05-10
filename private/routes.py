from flask import Flask, render_template, request, redirect,  flash, abort, url_for,send_file
from private import app
import os
from flask_login import login_user,current_user
from private.models import *
from datetime import date

import cv2
import numpy as np
from tensorflow import keras
from PIL import Image
from random import randint



@app.route('/',methods=['GET', 'POST'])
def index():
    if request.method == "POST":

        file = request.files["image"]
        print(file)
        print("__________")
        print(file.filename)

        pic_file = save_pictures(file)
        view = pic_file
        print(view)

        model_1 = keras.models.load_model('private/model')
        print("Loaded model from disk")

        image_type_labels = {
            0 :'public',
            1 : 'private'}


        images = "private/static/uploads/" + view
        print("--------------------------------")
        print(images)
        img_pred = cv2.imread(images)
        input_array = []
        resized_img_pred = cv2.resize(img_pred, (224, 224)) # Resizing the images to be able to pass on MobileNetv2 model
        input_array.append(resized_img_pred)

        input_array = np.array(input_array)
        input_array= input_array/255

        y_pred_img = model_1.predict(input_array, batch_size=64, verbose=1)
        y_pred_bool_img = np.argmax(y_pred_img, axis=1)
        prediction = image_type_labels[y_pred_bool_img[0]]
        print(prediction)
        output=prediction


        return render_template("index.html",output=output)
    return render_template("index.html")



def save_pictures(form_picture):
    random_hex = random_with_N_digits(14)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = str(random_hex) + f_ext
    picture_path = os.path.join(app.root_path, 'static/uploads', picture_fn)
    output_size = (500, 500)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn


def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)