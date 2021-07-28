import json
import tweepy

def readFriends():
    f = open("friends.json", "r")
    friend_list = json.load(f)
    f.close()
    return friend_list

def updateFriends(api, friend_list):
    for friend in api.friends():
        if str(friend.id) not in friend_list.keys():
            print(f"adding friend {friend.name}")
            friend_list[friend.id] = {
                "id" : friend.id,
                "name" : friend.name,
                "screen_name" : friend.screen_name,
                "score": 1
                }
    f = open("friends.json", "w")
    f.write(json.dumps(friend_list))
    f.close()

    return friend_list

def getTweets(api, friend):
    tweet_list = []
    for tweet in tweepy.Cursor(api.user_timeline, id=friend["id"]).items():
        if tweet.in_reply_to_status_id is None:
            try:
                tweet.retweeted_status
            except AttributeError:
                tweet_list.append(tweet.text)
    f = open("friends/{}.json".format(friend["name"]), "w")
    f.write(json.dumps(tweet_list))
    f.close()
