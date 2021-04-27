import tweepy
import socket
import json
import os


class TweetListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)


def get_credentials():
  return {
    'consumer_key' : os.getenv("CONSUMER_KEY"),
    'consumer_secret' : os.getenv("CONSUMER_SECRET"),
    'access_token' : os.getenv("ACCESS_TOKEN"),
    'access_token_secret' : os.getenv("ACCESS_TOKEN_SECRET"),
  }

def test_authentication(consumer_key, consumer_secret, access_token, access_token_secret):
  # Authenticate to Twitter
  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_token_secret)

  api = tweepy.API(auth)

  try:
      api.verify_credentials()
      print("Authentication OK")
  except:
      print("Athentication Error")

def create_api(consumer_key, consumer_secret, access_token, access_token_secret):
  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_token_secret)
  api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
  try:
      api.verify_credentials()
  except Exception as e:
      raise e
  
  print("API Created")
  return api

if __name__ == "__main__":
  credentials = get_credentials()
  test_authentication(
    credentials['consumer_key'], 
    credentials['consumer_secret'], 
    credentials['access_token'], 
    credentials['access_token_secret']
  )

  api = create_api(
    credentials['consumer_key'], 
    credentials['consumer_secret'], 
    credentials['access_token'], 
    credentials['access_token_secret']
  )

  myTweetListener = TweetListener()

