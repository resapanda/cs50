import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])

o = response.json()
for result in o["results"]:
    print(result["trackName"])

# break vs sys.exit()
# break -> is used to break out of things like loop
# sys.exit() -> is used to break out of whole program itself

