# Imports "source.py" file
import source

# Imports `inspect` module
import inspect

# Imports `os` module
import os

# Imports `sys` module
import sys

# Imports `time` module
import time

# Imports `nltk` module
import nltk

nltk.download("stopwords")
nltk.download("wordnet")
nltk.download('vader_lexicon')

from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer

stop_words = stopwords.words("english")
stemmer = SnowballStemmer("english", ignore_stopwords=True)
lemmatizer = WordNetLemmatizer()

# Get current directory path
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

# Get parent directory from current directory path
parent_dir = os.path.dirname(current_dir)

# Insert `parent_dir` value into "SYS_PATH"
sys.path.insert(0, parent_dir)

# Imports variables from "config.py" file
import config

# Imports the `tweepy` module
import tweepy as tw

# Imports the `json` module
import json

# Imports Regex module
import re

class TwitterClient(object):
    '''
    Generic Twitter Class for sentiment analysis.
    '''
    def __init__(self):
        '''
        Class constructor or initialization method.
        '''
        try:
            # Import 'twitter' object from source
            twitter_source = source.twitter()
            
            # create twitter API object
            auth = tw.OAuthHandler(twitter_source[0][2], twitter_source[1][2])
            auth.set_access_token(twitter_source[2][2], twitter_source[3][2])
            self.api = tw.API(auth, wait_on_rate_limit=True)
        except:
            print("Error: Authentication Failed")

    def clean_tweet(self, tweet):
        '''
        Utility function to clean tweet text by removing links, special characters
        using simple regex statements.
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    def get_tweet_sentiment(self, tweet):
        '''
        Utility function to classify sentiment of passed tweet
        using textblob's sentiment method
        '''
        c_tweet = self.clean_tweet(tweet.lower())
        
        tokenized_text = word_tokenize(c_tweet)
        
        words = [lemmatizer.lemmatize(w) for w in tokenized_text if w not in stop_words]
        
        stem_text = " ".join([stemmer.stem(i) for i in words])
        
        sid = SentimentIntensityAnalyzer()
        
        # create TextBlob object of passed tweet text
        analysis = sid.polarity_scores(stem_text)
        
        # set sentiment
        return analysis

    def get_tweets(self, symbol, count):
        '''
        Utility function to fetch tweets
        '''
        # Search for hash tag with symbol and base_symbol, and fetch tweets
        tweets = tw.Cursor(self.api.search_tweets,
              q=f'#{symbol} AND #news',
              lang="en",
              result_type='recent').items(count)
        
        # Return results
        return tweets
    