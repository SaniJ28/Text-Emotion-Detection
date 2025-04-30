# model_script.py
import re
from collections import Counter
import joblib
from sklearn.feature_extraction import DictVectorizer

# Load saved model and vectorizer
clf = joblib.load("emotion_clf.pkl")
vectorizer = joblib.load("vectorizer.pkl")

def ngram(token, n): 
    return [' '.join(token[i-n+1:i+1]) for i in range(n-1, len(token))]

def create_feature(text, nrange=(1, 4)):
    text_features = [] 
    text = text.lower() 
    text_alphanum = re.sub('[^a-z0-9#]', ' ', text)
    for n in range(nrange[0], nrange[1]+1): 
        text_features += ngram(text_alphanum.split(), n)    
    text_punc = re.sub('[a-z0-9]', ' ', text)
    text_features += ngram(text_punc.split(), 1)
    return Counter(text_features)

def predict_emotion(text):
    features = create_feature(text)
    features_vectorized = vectorizer.transform(features)
    return clf.predict(features_vectorized)[0]
