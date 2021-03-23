import os
import argparse
from datetime import datetime, timedelta
import pickle

import twitter
import pytz

from bokeh.plotting import curdoc
import scheduler, report, get_data
from coinapi_patch import CoinAPIv1Patched

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

    report.graph(bitcoin_data, tweets)

if __name__ == "__main__":
    main(parse_args())
