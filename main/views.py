from django.shortcuts import render
import os
import numpy as np
from django.core.files.storage import default_storage
import tensorflow as tf
from .helper_function import load_and_pred

cur_dir = os.path.dirname(__file__)
model = tf.keras.models.load_model(os.path.join(cur_dir, 'model', 'model.h5'))

# Create your views here.

class_names = ['abacha', 'akara', 'jellof_rice', 'moin_moin', 'pounded_yam', 'suya']
food_names = {
    'abacha': 'abacha',
    'akara': 'akara',
    'jellof_rice': 'jellof rice',
    'moin_moin': 'moin moin',
    'pounded_yam': 'pounded yam',
    'suya': 'suya',
}


def index(request):
    if request.method == 'POST':        
        file = request.FILES["image"]
        file_name = default_storage.save(file.name, file)
        file_url = default_storage.path(file_name)       
        try:
            pred, prob = load_and_pred(model, file_url, class_names)             
        except ValueError as e:
            prediction = 'An error occured, try again!'
        else:
             prediction, probability = pred, prob
        context = {
            'prediction': food_names[prediction].title(),
            'probability': probability,        
        }
        return render(request, 'index.html', context)
    else:
        return render(request, 'index.html')


def camera(request):
    return render(request, 'camera.html')
