import requests
import random
random.seed()
import secrets

MODES = ['analogic-complement', 'quad', 'analogic']
MIN_COLORS = 3
MAX_COLORS = 9
ENDPOINT = 'https://www.thecolorapi.com/scheme'

params = {
    'hex': secrets.token_bytes(3).hex(),
    'mode': random.choice(MODES),
    'count': random.randint(MIN_COLORS, MAX_COLORS),
    'format': 'json'
}
print(params)

try:
    tries = 5
    while tries >= 0:
        try:
            data = requests.get(ENDPOINT, params).json()
            for color in data['colors']:
                print(f"Got color {color['hex']['value']}")

            break
        except requests.exceptions.HTTPError as err:
            tries = tries - 1
            if tries > 0:
                print(f'HTTP ERROR, trying {tries} more times...')
except ConnectionError as err:
    print('CONNECTION ERROR, exiting... (more output below)')
    print(str(err))
    exit(1)
