import tweepy
import config
from process import processTweet
from friends import readFriends, updateFriends, getTweets
from ai import getFakeTweet

auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

class FavRetweetListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        print(f"Processing tweet id {tweet.id}")
        friend = friend_list[tweet.user.id]
        processTweet(tweet, friend)

    def on_error(self, status):
        print(status)

friend_list = readFriends()
friend_list = updateFriends(api, friend_list)
for friend in friend_list:
    getTweets(api, friend_list[friend])

tweets_listener = FavRetweetListener(api)
stream = tweepy.Stream(api.auth, tweets_listener)
stream.filter(follow=[str(user) for user in friend_list], is_async = True)
