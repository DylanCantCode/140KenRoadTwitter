import tweepy
import json
import config
from process import processTweet

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

friend_list = {} #TODO: Gives all following as well

#f = open("friends.json", "r")
#friend_list = json.load(f.readline())
#f.close()

if friend_list == {}:
    for friend in api.friends():#TODO: Gives all following as well
        friend_list[friend.id] = {
            "id" : friend.id,
            "name" : friend.name,
            "screen_name" : friend.screen_name,
            "score": 1
            }
    f = open("friends.json", "w")
    f.write(json.dumps(friend_list))
    f.close()

tweets_listener = FavRetweetListener(api)
stream = tweepy.Stream(api.auth, tweets_listener)
stream.filter(follow=[str(user) for user in friend_list], is_async = True)
