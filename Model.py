#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 1. Library imports
import tensorflow as tf
from pydantic import BaseModel

# 1. Class for loading model and making predictions
class LoadModel(tf.keras.models.Model):
    # Class constructor that loads the model
    def __init__(self, model_path):
        super(tf.keras.models.Model)
        self.model = tf.keras.models.load_model(model_path)

    # Returns the predicted classes with its respective probability
    def predict_species(self, image):
        prediction = self.model.predict(image)
        
        return prediction[0]