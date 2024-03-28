import numpy as np
import pandas as pd
import librosa
import librosa.display
import os
from tensorflow.keras.utils import to_categorical
from sklearn.preprocessing import LabelEncoder
import pickle

def feature_extract(file):
    audio, sample_rate = librosa.load(file, res_type = "kyser_fast")
    mfccs_features = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc = 40)
    mfccs_features_scaled = np.mean(mfccs_features.T, axis=0)
    return mfccs_features_scaled


df = pd.read_csv("C:/Users/nadua/OneDrive/Desktop/folders/mlp/musicgenre/myapp/learning/extracted.csv")
print(df.head())
X = np.array(df["feature"].tolist())
y = np.array(df["class"].tolist())

labelenc = LabelEncoder()
y = to_categorical(labelenc.fit_transform(y))

def classifier(aud_path):
    newm = pickle.load(open("C:/Users/nadua/OneDrive/Desktop/folders/mlp/musicgenre/myapp/learning/models/pic", "rb"))
    aud = aud_path
    scaled = feature_extract(aud)
    scaled = scaled.reshape(1, -1)

    predict=newm.predict(scaled)
    pred_class = np.argmax(predict,axis=1)
    pred_class = labelenc.inverse_transform(pred_class)
    return pred_class