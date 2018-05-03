import tweepy
from textblob import TextBlob

consumer_key = 'mMnlsPXCB8nKrgrZE2HGanNYU'
consumer_secret = 'MLHVUz6i3vyeXUlavZGwbWX5c8HmTDR7YuOs9dGVqaOZDElyrp'
 
access_token = '991989089791508480-Xn0Zn3Lsscnk1KhFLpOIeghUeJ0FJcY' 
access_token_secret = 'BsWV268Kdjwf30x4XiauKTqvrhkw2QjnKltN9qJH7vumV'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Liverpool')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
