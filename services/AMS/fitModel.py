import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import Normalizer
from sklearn.svm import SVC
from joblib import dump, load
import pandas as pd

from login.models import Subject

def main():
    data = np.load('services/AMS/dataset_embeddings.npz')
    X, y = data['arr_0'], data['arr_1']
    y = y.ravel() # To convert it into (val, ) shape then being (val, 1)

    # Splitting of data and Storage
    trainX, testX, trainy, testy = train_test_split(X, y, test_size=0.2, random_state=4)

    #Training the model and calculating it accuracy
    # print("Dataset: train=%d, test=%d" % (trainX.shape[0], testX.shape[0]))
    # normalize input vectors
    in_encoder = Normalizer()
    emdTrainX_norm = in_encoder.transform(trainX)
    emdTestX_norm = in_encoder.transform(testX)

    # label encode targets
    out_encoder = LabelEncoder()
    out_encoder.fit(trainy)
    trainy_enc = out_encoder.transform(trainy)
    testy_enc = out_encoder.transform(testy)

    # Storing corresponding label in the settings file
    # Creating a csv file which will be further used to keep the record of attendance
    key = np.unique(trainy_enc)
    student_Record = {}
    student_Record['Key'] = key
    student_Record['Rollno'] = out_encoder.inverse_transform(key)
    
    subjects = Subject.objects.all()
    for sub in subjects:
        student_Record[sub.subjectName] = 0
    std_DB = pd.DataFrame(student_Record)
    std_DB.to_csv('services/AMS/std_DB.csv', index=False)

    # fit model
    model = SVC(kernel='linear', probability=True)
    model.fit(emdTrainX_norm, trainy_enc)
    # predict
    yhat_train = model.predict(emdTrainX_norm)
    yhat_test = model.predict(emdTestX_norm)
    # score
    score_train = accuracy_score(trainy_enc, yhat_train)
    score_test = accuracy_score(testy_enc, yhat_test)
    print('Accuracy: train=%.3f, test=%.3f' % (score_train*100, score_test*100))

    ## Saving the above fited SVC model to classify the Student for future use
    dump(model, 'services/AMS/predictor.joblib')

    return score_train*100, score_test*100