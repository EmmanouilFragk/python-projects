import tweepy
import time 

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
user = api.me()


search_string = 'python'
number = 2

for tweet in tweepy.Cursor(api.search, search_string).items(number):
    try:
        tweet.favorite()
        print('i liked it')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
def limit_handler(cursor):
   try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)
#follow back
for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    print(follower.name)