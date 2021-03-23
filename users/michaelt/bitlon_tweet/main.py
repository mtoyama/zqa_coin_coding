import os
import argparse
from datetime import datetime, timedelta
import pickle
import statistics
from random import random
import pytz

from users.michaelt.bitlon_tweet import scheduler, report, get_data

from api_patches.coinapi_patch import CoinAPIv1Patched
import twitter

TWEET_DATA = "users/michaelt/bitlon_tweet/data/tweets.p"
BITCOIN_DATA = "users/michaelt/bitlon_tweet/data/bitcoin_data.p"

twitter_api = twitter.Api(consumer_key=os.environ['TWITTER_API_KEY'],
                        consumer_secret=os.environ['TWITTER_API_SECRET'],
                        access_token_key=os.environ['TWITTER_ACCESS_TOKEN'],
                        access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET']
)

coinapi = CoinAPIv1Patched(os.environ['COINAPI_API_KEY'])
utc = pytz.UTC

tweet_data = get_data.get_user_latest_tweets(
    twitter_api,
    'elonmusk',
    utc.localize(datetime.now()) - timedelta(days=20)
)
bitcoin_data = get_data.get_latest_btc_prices(coinapi, '30MIN', 480)
pickle.dump(tweet_data, open(TWEET_DATA, 'wb'))
pickle.dump(bitcoin_data, open(BITCOIN_DATA, 'wb'))
