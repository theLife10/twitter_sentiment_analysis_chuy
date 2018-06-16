import tweepy
from textblob import TextBlob
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np 

def main():
	#conecting to the twitter api
	

	auth = tweepy.OAuthHandler(consumer_key , consumer_secret)
	auth.set_access_token(access_token , access_token_secrete)

	api = tweepy.API(auth)
	#trend that we are searching for. 
	public_tweets = api.search('Trump')

	polarity = []
	status = []
	for tweet in public_tweets:
		analysis = TextBlob(tweet.text)
		polarity.append(analysis.sentiment.polarity)
		status.append(get_status(analysis.sentiment.polarity))

	df = convert_to_dataframe(polarity,status)
	

	
	

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