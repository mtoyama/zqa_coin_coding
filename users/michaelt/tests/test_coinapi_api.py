import sys
from coinapi_rest_v1.restapi import CoinAPIv1
import datetime

test_key = sys.argv[1]
api = CoinAPIv1(test_key)

quotes_today_data_btc_usd = api.quotes_historical_data(
    'BITSTAMP_SPOT_BTC_USD',
    {'time_start': datetime.datetime.now().strftime('%Y-%m-%d')}
)

for quote in quotes_today_data_btc_usd:
    print('Symbol ID: %s' % quote['symbol_id'])
    print('Time Exchange: %s' % quote['time_exchange'])
    print('Time CoinAPI: %s' % quote['time_coinapi'])
    print('Ask Price: %s' % quote['ask_price'])
    print('Ask Size: %s' % quote['ask_size'])
    print('Bid Price: %s' % quote['bid_price'])
    print('Bid Size: %s' % quote['bid_size'])