import openai
import config
import json
from random import sample

def getFakeTweet(friend):
    f = open("friends/{}.json".format(friend["id"]), "r")
    tweets = json.load(f)
    f.close()
    input = "{0}: " + "\n{0}: ".join(sample(tweets, k=50)) + "\n{0}: "
    print(input)
    input = input.format(*friend["name"])
 

    openai.api_key = config.openai_key

    response = openai.Completion.create(
      engine="davinci",
      prompt=input,
      temperature=0.25,
      max_tokens=42,
      top_p=1,
      frequency_penalty=1,
      presence_penalty=0
    )

    clean_response = response["choices"][0]["text"].split("\n")[0]
    return(clean_response)
