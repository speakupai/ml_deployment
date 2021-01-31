#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 1. Library imports
import tensorflow as tf
from pydantic import BaseModel

# Returns the predicted classes with its respective probability
def predict_type(image):
    model = tf.keras.models.load_model(
        '/home/taimur/Documents/Online Courses/Fourth Brain/Projects/Audio_super_res/ml_deployment/saved_model/10l-3c_zca.h5')
    img = tf.io.decode_jpeg(image.read())
    img = tf.image.resize(img, (224,224))
    img = tf.expand_dims(img, axis=0)
    prediction = model.predict(img)
    #return img.shape
    return prediction[0]

# 1. Class for loading model and making predictions
'''class LoadModel(tf.keras.models.Model):
    # Class constructor that loads the model
    def __init__(self, model_path):
        super(tf.keras.models.Model)
        self.model = tf.keras.models.load_model(model_path)

    # Returns the predicted classes with its respective probability
    def predict_type(self, image):
        prediction = self.model.predict(image)
        
        return prediction[0]'''