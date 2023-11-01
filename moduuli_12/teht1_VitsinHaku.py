import requests
import json

pyyntö = "https://api.chucknorris.io/jokes/random"
vastaus = requests.get(pyyntö)
json_vastaus = vastaus.json()
print("\nHere's a random Chuck Norris joke for you.\n")
print(json_vastaus["value"])
