import json
import pandas as pd
import datetime as dt
import requests
import urllib
import os

from coinapi_rest_v1.restapi import CoinAPIv1


API_KEY = os.environ.get('COIN_API_KEY')

api = CoinAPIv1(API_KEY)

headers = {"X-CoinAPI-Key" : API_KEY}

url = 'https://rest.coinapi.io/v1/assets'

resp = requests.get(url, headers = headers)


assets = resp.json()

print(f"There are {len(assets)} assets")
assets[:3]