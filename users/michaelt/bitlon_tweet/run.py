import os
import argparse
from datetime import datetime, timedelta
import pickle

import twitter
import pytz

from bokeh.plotting import curdoc
import scheduler, report, get_data
from coinapi_patch import CoinAPIv1Patched


from bokeh.plotting import figure, show
from bokeh.palettes import Dark2_5 as palette
from bokeh.io import curdoc
from bokeh.models import Span, HoverTool, ColumnDataSource, LinearAxis, Range1d

from utils import parse_and_localize_utc

TWEET_DATA = "./data/tweets.p"
BITCOIN_DATA = "./data/bitcoin_data.p"

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--use_pickle", action='store_true', default=True)
    parser.add_argument("--pickle_data", action='store_true',default=False)
    return parser.parse_args()

def main(args):
    twitter_api = twitter.Api(consumer_key=os.environ['TWITTER_API_KEY'],
                          consumer_secret=os.environ['TWITTER_API_SECRET'],
                          access_token_key=os.environ['TWITTER_ACCESS_TOKEN'],
                          access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET']
    )

    if not args.use_pickle:
        coinapi = CoinAPIv1Patched(os.environ['COINAPI_API_KEY'])
        utc = pytz.UTC
        tweets = get_data.get_user_latest_tweets(
            twitter_api, 
            'elonmusk',
            utc.localize(datetime.now() - timedelta(days=1))
        )
        bitcoin_data = get_data.get_latest_btc_prices(coinapi, "10MIN", 144)
        if args.pickle_data:
            pickle.dump(tweets, open(TWEET_DATA, 'wb'))
            pickle.dump(bitcoin_data, open(BITCOIN_DATA, 'wb'))
    else:
        tweets = pickle.load(open(TWEET_DATA, 'rb'))
        bitcoin_data = pickle.load(open(BITCOIN_DATA, 'rb'))

    graph(bitcoin_data, tweets)

def graph(bitcoin_data, tweets):
    bitcoin_time_array = [parse_and_localize_utc(x["time_period_start"]) for x in bitcoin_data]
    bitcoin_price_array = [y["price_close"] for y in bitcoin_data]
    bitcoin_min = min(bitcoin_price_array)
    bitcoin_max = max(bitcoin_price_array)
    curdoc().theme = 'dark_minimal'
    p = figure(
        title='BitCoin x Elon Musk',
        x_axis_label='date',
        x_axis_type='datetime',
        y_axis_label='Price (USD)',
        y_range=(round(bitcoin_min, -4), round(bitcoin_max, -4))
    )

    p.line(
        bitcoin_time_array,
        bitcoin_price_array,
        legend_label = "BitCoin Price",
        line_width=2,
        line_color='gray'
    )

    trades_count_array = [x['trades_count'] for x in bitcoin_data]
    trades_count_min = min(trades_count_array)
    trades_count_max = max(trades_count_array)
    p.extra_y_ranges = {"trades_count": Range1d(
        start=round(trades_count_min,-3), end=round(trades_count_max, -3)
        )}
    p.add_layout(LinearAxis(
        y_range_name="trades_count", axis_label="Trades Count"), 'right')
    p.vbar(x=bitcoin_time_array, top=trades_count_array, width=0.4, bottom=0, 
           y_range_name="trades_count", line_color='purple', line_alpha = 0.8,
           legend_label="BitCoin Trades Count", fill_color='purple')

    x_tweet = []
    bitcoin_average = statistics.mean(bitcoin_price_array)
    y_tweet = [bitcoin_average for x in range(0, len(tweet_data))]
    desc_tweet = []
    for tweet in tweet_data:
        created_at_parsed = parse_and_localize_utc(tweet.created_at)
        x_tweet.append(created_at_parsed)
        desc_tweet.append(tweet.text)
        tweet_line = Span(location=created_at_parsed,
                          dimension='height', line_color = 'deepskyblue',
                          line_dash='dashed', line_width=0.8)
        p.add_layout(tweet_line)
    
    source = ColumnDataSource(data=dict(
        x=x_tweet,
        y=y_tweet,
        desc=desc_tweet,
    ))
    circle = p.circle(source=source, size=1, alpha=1)
    tweet_hovertool = HoverTool(
        renderers = [circle],
        mode = 'vline',
        tooltips = [("@elonmusk:", "@desc")],
    )
    p.tools.append(tweet_hovertool)
    curdoc().add_root(p)


if __name__ == "__main__":
    main(parse_args())
