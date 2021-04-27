import tweepy
import socket
import json
import os


class TweetListener(tweepy.StreamListener):
    def __init__(self, api, csocket):
        self.api = api
        self.me = api.me()
        self.client_socket = csocket

    def on_status(self, status):
        print(status.text)
    
    def on_data(self, data):
      try:
          msg = json.loads(data)
          encoded = msg['text'].encode('utf-8')
          self.client_socket.send(encoded)
      except BaseException as e:
          print("Error on_data: {}".format(str(e)))
      return True

    def on_error(self, status):
        print("Error detected. Status: {}".format(status))


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

def create_server_connection(host='0.0.0.0', port=5555):
  sock = socket.socket()
  sock.bind((host, port))
  sock.listen(5)
  print('Socket listening')

  c_socket, address = sock.accept()
  print('Connection accepted: {}'.format(address))
  return c_socket, address

if __name__ == "__main__":
  keywords = ['crypto', 'cryptocurrency']
  
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

  # Start server
  c_socket, address = create_server_connection()

  # Stream tweets
  tweets_listener = TweetListener(api, c_socket)
  stream = tweepy.Stream(api.auth, tweets_listener)
  stream.filter(track=keywords, languages=["en"])
