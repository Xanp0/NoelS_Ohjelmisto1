import requests
import json

vitsi = requests.get("https://api.chucknorris.io/jokes/random").json()
print("\nHere's a random Chuck Norris joke for you.\n")
print(vitsi["value"])

# pyynto = "https://api.chucknorris.io/jokes/random"
# vitsi = requests.get(pyynto)
# jsonVitsi = vitsi.json()
# print("\nHere's a random Chuck Norris joke for you.\n")
# print(jsonVitsi["value"])
