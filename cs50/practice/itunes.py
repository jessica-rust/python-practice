import json
import requests
import sys

if len(sys.argv) != 3 :
    sys.exit("name of artist and number of songs required")


response = requests.get(f"https://itunes.apple.com/search?entity=song&limit={sys.argv[2]}&term={sys.argv[1]}")

o = response.json()  # the whole json text
for result in o["results"]:   # "results" is a list with one dict inside, so this retreives the dict
    print(result["trackName"]) # this fids the key "trackName inside the dict and returns its value


# prints json with better formatting
# print(json.dumps(response.json(), indent = 2))
