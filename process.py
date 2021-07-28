import tweepy

def processTweet(tweet, friend):
    #Get info from tweet

    friend_score = friend["score"]
    if friend_score >= 1:
        like(tweet)
        retweet(tweet)

def like(tweet):
    if not tweet.favorited:
        # Mark it as Liked, since we have not done it yet
        try:
            tweet.favorite()
        except Exception as e:
            print("Error on fav")

def retweet(tweet):
    if not tweet.retweeted:
        # Retweet, since we have not retweeted it yet
        try:
            tweet.retweet()
        except Exception as e:
            print("Error on fav and retweet")
