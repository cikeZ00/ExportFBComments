import urllib3, requests, facebook, json, os
from os import path

# CONFIG
if not path.exists("config.json"):
    with open('config.json', 'w') as configout:
        json.dump({
            "Facebook":{
                "Token": "Here",
                "ID": "PageID_PostID"
            }
        }, configout, indent=4)
    print("[INFO] config.json generated!")
    quit()

else:
    with open("config.json") as f:
        config = json.load(f)

token = config["Facebook"].get("Token")


graph = facebook.GraphAPI(access_token=token, version = 8.0)
post = graph.get_object(id=config["Facebook"].get("ID"), fields='comments')

data = post["comments"]

with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)

