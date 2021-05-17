#from api_patches.coinapi_patch import CoinAPIv1Patched
from coinapi_rest_v1.restapi import CoinAPIv1
import datetime, os
import pandas as pd
import matplotlib.pyplot as plt

test_key = os.environ.get("COIN_API_KEY")
#api = CoinAPIv1(os.environ['COIN_API_KEY'])

api = CoinAPIv1(test_key)
exchanges_btc = api.exchange_rates_get_all_current_rates("BTC")
# print(type(exchanges_btc))
df_btc = pd.DataFrame(exchanges_btc)

# print(df_btc.info())
# print((exchanges_btc['asset_id_base']))
# print(exchanges_btc['rates'])
df_test = pd.DataFrame(exchanges_btc['rates'])
df_test.to_csv('list_rates.csv',index=False)
df_test['asset_id_quote'] == 'USD'

AB = df_test['asset_id_quote'] == 'USD'
BC = df_test['asset_id_quote'] == 'DOGE'
CD = df_test['asset_id_quote'] == 'GOLD'
DE = df_test['asset_id_quote'] == 'ETH'
EF = df_test['asset_id_quote'] == 'XRP'
print (df_test[AB|BC|CD|DE|EF])

plt.bar(df_test['asset_id_quote'], df_test['rate'])
plt.show()


# print (type)
# print (type(df_test['asset_id_quote']))
# print (df_test)
# exchanges = api.metadata_list_exchanges()


# print('Exchanges')
# for exchange in exchanges:
#     print('Exchange ID: %s' % exchange['exchange_id'])
#     print('Exchange website: %s' % exchange['website'])
#     print('Exchange name: %s' % exchange['name'])


# exchange_rate = api.exchange_rates_get_specific_rate('BTC', 'USD')
# print('Time: %s' % exchange_rate['time'])
# print('Base: %s' % exchange_rate['asset_id_base'])
# print('Quote: %s' % exchange_rate['asset_id_quote'])
# print('Rate: %s' % exchange_rate['rate'])
# last_week = datetime.date(2017, 5, 16).isoformat()

# exchange_rate_last_week = api.exchange_rates_get_specific_rate('BTC', 'USD', {'time': last_week})
# print('Time: %s' % exchange_rate_last_week['time'])
# print('Base: %s' % exchange_rate_last_week['asset_id_base'])
# print('Quote: %s' % exchange_rate_last_week['asset_id_quote'])
# print('Rate: %s' % exchange_rate_last_week['rate'])
