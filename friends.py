import json

def readFriends():
    f = open("friends.json", "r")
    friend_list = json.load(f)
    f.close()
    return friend_list

def updateFriends(api, friend_list):
    for friend in api.friends():
        print(friend_list.keys())
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
