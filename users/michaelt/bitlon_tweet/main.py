import os
import argparse
from datetime import datetime, timedelta
from dateutil.parser import parse
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


utc = pytz.UTC

tweet_data = pickle.load(open(TWEET_DATA, 'rb'))
last_stored_tweet_date = tweet_data[-1].created_at
new_tweet_data = get_data.get_user_latest_tweets(
    twitter_api,
    'elonmusk',
    utc.localize(datetime.now()) - timedelta(days=20)
)
for tweet in new_tweet_data:
    if tweet.created_at > last_stored_tweet_date:
        tweet_data.append(tweet)
pickle.dump(tweet_data, open(TWEET_DATA, 'wb'))

bitcoin_data = pickle.load(open(BITCOIN_DATA, 'rb'))
last_stored_bitcoin_data = parse(bitcoin_data[-1]['time_period_start'])
coinapi = CoinAPIv1Patched(os.environ['COINAPI_API_KEY'])
new_bitcoin_data = get_data.get_latest_btc_prices(coinapi, '30MIN', 960)
for btc_price in new_bitcoin_data:
    if parse(btc_price['time_period_start']) > last_stored_bitcoin_data:
        bitcoin_data.append(btc_price)
pickle.dump(bitcoin_data, open(BITCOIN_DATA, 'wb'))
