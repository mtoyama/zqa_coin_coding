import os
import pytest
import datetime
import pytz

import twitter

from users.michaelt.bitlon_tweet import get_data, api_patch

@pytest.fixture
def twitter_api():
    api = twitter.Api(consumer_key=os.environ['TWITTER_API_KEY'],
                      consumer_secret=os.environ['TWITTER_API_SECRET'],
                      access_token_key=os.environ['TWITTER_ACCESS_TOKEN'],
                      access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET']
    )
    return api

@pytest.fixture
def coinapi_api():
    api = api_patch.CoinAPIv1Patched(os.environ['COINAPI_API_KEY'])
    return api

def test_get_user_latest_tweets(twitter_api):
    utc = pytz.UTC
    tweet = get_data.get_user_latest_tweets(
        twitter_api, 'elonmusk', utc.localize(datetime.datetime(2021, 1, 1))
    )
    assert tweet[0].user.screen_name == 'elonmusk'

def test_get_btc_price_latest(coinapi_api):
    data = get_data.get_latest_btc_prices(coinapi_api, '1SEC', 5)
    assert len(data) == 5
