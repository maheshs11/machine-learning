import joblib
import pandas
import numpy
from sklearn import *

model=joblib.load(r'C:\Users\Admin\Desktop\pyqt5\model.pkl')


def classify_tweet(tweet):
    input_tweets = [str(x) for x in tweet.split("," and '.', -1)]
    score=model.predict(input_tweets)
    return score,'not depressed' if score.any() < 1 else 'depressed'

