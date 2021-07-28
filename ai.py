import openai
import config
import json

def getFakeTweet(friend):
    f = open("friends/{}.json".format(friend["id"]), "r")
    tweets = json.load(f)
    f.close()
    input = "User: " + "\nUser: ".join(tweets[0:50]) + "\nUser: "

    openai.api_key = config.openai_key

    response = openai.Completion.create(
      engine="davinci",
      prompt=input,
      temperature=0.75,
      max_tokens=42,
      top_p=1,
      frequency_penalty=1,
      presence_penalty=0
    )

    clean_response = response["choices"][0]["text"].split("\n")[0]
    return(clean_response)
