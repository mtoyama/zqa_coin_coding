import sys
import json
from nomics import Nomics

api_key = sys.argv[1]
nomics = Nomics(api_key)

btc_etc = nomics.Currencies.get_currencies(ids = "BTC, ETC")
print(json.dumps(btc_etc, indent=4))