from coinapi_rest_v1.restapi import CoinAPIv1
import datetime, os

test_key = os.environ.get("COIN_API")


api = CoinAPIv1(test_key)
exchanges = api.metadata_list_exchanges()

print('Exchanges')
for exchange in exchanges:
    print('Exchange ID: %s' % exchange['exchange_id'])
    print('Exchange website: %s' % exchange['website'])
    print('Exchange name: %s' % exchange['name'])