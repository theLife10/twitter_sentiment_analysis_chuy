import tweepy
from textblob import TextBlob
import pandas as pd 
import matplotlib.pyplot as plt
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.tokenize import regexp_tokenize
from nltk.tokenize import TweetTokenizer

def main():
	#trend that we are searching for. 

	api = connect_to_twitter(consumer_key,consumer_secret,access_token,access_token_secrete)
	public_tweets = api.search('Trump')

	polarity = []
	status = []
	for tweet in public_tweets:
		analysis = TextBlob(tweet.text)
		polarity.append(analysis.sentiment.polarity)
		status.append(get_status(analysis.sentiment.polarity))

	df = convert_to_dataframe(polarity,status)
	print(df)
	

	
def connect_to_twitter(consumer_key,consumer_secret,access_token,access_token_secrete):
	auth = tweepy.OAuthHandler(consumer_key , consumer_secret)
	auth.set_access_token(access_token , access_token_secrete)

	api = tweepy.API(auth)
	return api


def convert_to_dataframe(polarity,status):
	data ={
	'polarity' : polarity,
	'status' : status
	}
	df = pd.DataFrame(data)
	return df	

def get_status(polarity):
	if polarity == 0.0 :
		return 'nuetral'
	elif polarity > 0.0 :
		return 'positive'
	else:
		return 'negative'


	
main()
