import sys
import json
import argparse
import itertools

from datetime import datetime, timedelta

from coinapi_rest_v1.restapi import CoinAPIv1
from bokeh.plotting import figure, show
from bokeh.palettes import Dark2_5 as palette
from bokeh.io import curdoc

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
        get_data.coinapi_get_active_crypto_assets()
    if args.refresh_history:
        top_assets = get_data.local_get_top_assets_volume_1d(10)
        symbol_list = []
        for asset in top_assets:
            symbol_list.append((asset['asset_id'], config.QUOTE_ASSET))
        get_data.coinapi_get_historical_data_days(symbol_list, 30)
    
    with open(config.TOP_10_HISTORICAL, 'r') as f:
        data = json.load(f)
    
    start_date = datetime.fromisoformat(data['metadata']['time_start'])
    end_date = datetime.fromisoformat(data['metadata']['time_end'])
    date_range = end_date - start_date

    colors = itertools.cycle(palette)
    curdoc().theme = 'dark_minimal'
    p = figure(
        title='Percent Change from Open for Top Assets by Volume',
        x_axis_label='date',
        y_axis_label='Percent Change From Open'
    )

    x = []
    for i in range(date_range.days - 1):
        x.append(start_date + timedelta(days=i))
    
    for key in data.keys():
        if key == "metadata":
            continue
        if len(data[key]) > 0:
            y = []
            title = key
            print(title)
            for asset_data in data[key]:
                y.append(
                    (asset_data['price_open'] - asset_data['price_close']) \
                        / asset_data['price_open']
                )
            p.line(x, y, legend_label = title, line_width=2, color=next(colors))
    
    show(p)

if __name__ == "__main__":
    main(parse_args())
