from sklearn.preprocessing import Normalizer
from joblib import load
import pandas as pd
import numpy as np
from services.AMS import embedding
from PIL import Image
from mtcnn import MTCNN
from keras.models import load_model

facenet_model = load_model('services/AMS/facenet_keras.h5')

def extract_face(image, required_size=(160, 160), detector = MTCNN() ):
    image = Image.open(image)
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

def predict(img, subjName, loginUser):

    face = extract_face(img)
    embed = embedding.get_embedding(facenet_model, face)

    # normalize input vectors
    normer = Normalizer()
    embedding_norm = normer.transform([embed])

    #Loading the model file
    m = load('services/AMS/predictor.joblib')

    name_key = m.predict(embedding_norm)
    # print(name_key[0])

    #To mark the attendance of student
    std_DB = pd.read_csv('services/AMS/std_DB.csv')
    subjectList = std_DB.columns

    for s in subjectList:
        if subjName in s:
            subjName = s
            break
    
    print(subjName)
    print(type(subjName))

    rollno = std_DB[std_DB['Key'] == name_key[0] ]["Rollno"].values

    if rollno[0] == loginUser:
        try:
            att_cnt = std_DB.loc[std_DB["Rollno"] == rollno[0], [subjName] ].values
            std_DB.loc[std_DB["Rollno"] == rollno[0], [subjName] ] = att_cnt[0][0] + 1

            std_DB.to_csv('services/AMS/std_DB.csv', index=False)
            print("Attendance Marked Successfully in CSV File")
        except:
            print("Attendance is not marked, please provide correct Subject Code")
    else:
        return False
    return rollno
