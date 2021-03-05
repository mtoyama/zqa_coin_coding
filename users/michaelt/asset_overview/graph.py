import sys
import json
import argparse

from coinapi_rest_v1.restapi import CoinAPIv1

import config


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--API_KEY", required=True)
    parser.add_argument("--refresh_assets", action='store_true')
    parser.add_argument("--refresh_history", action='store_true')
    return parser.parse_args()

def main(args):
    config.API_KEY = args.API_KEY
    import get_data

    if args.refresh_assets:
        coinapi_get_active_crypto_assets()
    if args.refresh_history:
        top_assets = get_data.local_get_top_assets_volume_1d(10)
        symbol_list = []
        for asset in top_assets:
            symbol_list.append("_".join(
                    [
                    config.EXCHANGE_ID,
                    config.SYMBOL,
                    asset['asset_id'],
                    config.QUOTE_ASSET
                    ]
                )
            )
        get_data.coinapi_get_historical_data_days(symbol_list, 30)
    


if __name__ == "__main__":
    main(parse_args())