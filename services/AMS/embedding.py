# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 19:05:26 2022

@author: laksh
"""
"""
References:
1. https://machinelearningmastery.com/how-to-develop-a-face-recognition-system-using-facenet-in-keras-and-an-svm-classifier/
2. https://www.kaggle.com/yhuan95/face-recognition-with-facenet
3. https://github.com/nyoki-mtl/keras-facenet - facenet_keras.h5 code DNN
"""

# import mtcnn
# # print version
# print(mtcnn.__version__)

import numpy as np
import os
# import pandas as pd
from mtcnn import MTCNN
from PIL import Image
# from tensorflow import keras
# facenet_model = keras.models.load_model('services/AMS/facenet_keras.h5')
from keras.models import load_model

facenet_model = load_model('services/AMS/facenet_keras.h5')

# extract a single face from a given photograph
def extract_face(filename, required_size=(160, 160), detector = MTCNN() ):
    image = Image.open(filename)
    image = image.convert('RGB')
    pixels = np.asarray(image)
    # Detecting face
    results = detector.detect_faces(pixels)
    # extract the bounding box from the first face
    x1, y1, width, height = results[0]['box']
    # deal with negative pixel index
    x1, y1 = abs(x1), abs(y1)
    x2, y2 = x1 + width, y1 + height
    # extract the face
    face = pixels[y1:y2, x1:x2]
    # resize pixels to the model size
    image = Image.fromarray(face)
    image = image.resize(required_size)
    face_array = np.asarray(image)
    return face_array

# Transfer learning to find a embedding for the uploaded image

def get_embedding(model, face):
    face = face.astype('float32')
    # standardization
    mean, std = face.mean(), face.std()
    face = (face-mean)/std
    # transfer face into one sample (3 dimension to 4 dimension)
    sample = np.expand_dims(face, axis=0)
    # make prediction to get embedding
    yhat = model.predict(sample)
    return yhat[0]


#Variables

def face_embedding(face_array, name):
    data = np.load('services/AMS/dataset_embeddings.npz')
    X, y = data['arr_0'], data['arr_1']
    # face = extract_face(filename)
    face = face_array
    emd = get_embedding(facenet_model, face)
    X = np.vstack( (X,emd) )
    y = np.vstack( (y, name) )
    np.savez_compressed('services/AMS/dataset_embeddings.npz', X, y)
    return emd

    
   
            