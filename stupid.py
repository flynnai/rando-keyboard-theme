import requests
import json
random_hex='f901d1'
request_string = 'https://www.thecolorapi.com/scheme?hex={}&mode=analogic&count=9&format=json'.format(random_hex)
resp = requests.get(request_string)
resp_json = resp.json()
print(resp_json)


