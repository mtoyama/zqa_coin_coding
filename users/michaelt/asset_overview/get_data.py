import sys
import json
import os
import time
from operator import itemgetter
from datetime import datetime, timedelta
import urllib

from api_patches.coinapi_patch import CoinAPIv1Patched

from users.michaelt.asset_overview import config

api = CoinAPIv1Patched(os.environ['COINAPI_API_KEY'])

def coinapi_get_active_crypto_assets():
    assets = api.metadata_list_assets()
    assets_filtered = []
    for asset in assets:
        if asset['type_is_crypto'] and asset['volume_1mth_usd'] > 0:
            assets_filtered.append(asset)

    with open(config.ASSETS, "w+") as f:
        json.dump(assets_filtered, f, indent=4)
    return config.ASSETS

def coinapi_get_historical_data_days(asset_base_quote_list, days):
    time_end = datetime.now().date()
    time_start = time_end - timedelta(days=days)

    historical_data = {}
    historical_data['metadata'] = {
        'time_start' : time_start.isoformat(),
        'time_end' : time_end.isoformat()
    }
    for asset_base, asset_quote in asset_base_quote_list:
        time.sleep(1)
        print(asset_base, asset_quote)
        try:
            data = api.ohlcv_historical_data_by_asset(
                asset_base,
                asset_quote,
                {'period_id': '1DAY', 'time_start': time_start.isoformat()}
            )
            print(data)
            historical_data[asset_base + "_" + asset_quote] = data
        except urllib.error.HTTPError as e:
            print(e.read().decode())
            continue
    with open(config.TOP_10_HISTORICAL, 'w') as f:
        json.dump(historical_data, f, indent=4)
    return config.TOP_10_HISTORICAL

def local_get_top_assets_volume_1d(num_assets):
    with open(config.ASSETS, "r") as f:
        assets_json = json.load(f)
    sorted_list = sorted(
        assets_json,
        key=itemgetter('volume_1day_usd'),
        reverse=True
    )
    return sorted_list[:num_assets-1]
