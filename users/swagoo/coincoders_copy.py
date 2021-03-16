import sys
import json
from nomics import Nomics

api_key = sys.argv[1]
nomics = Nomics(api_key)

btc = nomics.Currencies.get_currencies(ids = "BTC")
print(json.dumps(btc, indent=4))
results=json.dumps(btc, indent=4)
data_dict = json.loads(results)
# the result is a JSON string:
price=data_dict[0]["price"]
print(price)