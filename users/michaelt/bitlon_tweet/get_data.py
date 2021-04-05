import os
from dateutil.parser import parse
import datetime

def get_user_latest_tweets(api, user, since_date):
    """
    GetUserTimeline returns Status objects: 
    https://python-twitter.readthedocs.io/en/latest/_modules/twitter/models.html#Status
    """
    tweets = api.GetUserTimeline(
        screen_name=user,
        include_rts=False,
        exclude_replies=True,
        count=100)

    tweets_out = []
    for tweet in tweets:
        created_at = parse(tweet.created_at)
        if created_at >= since_date:
            tweets_out.append(tweet)
        else:
            break
    return tweets_out

def get_latest_btc_prices(api, period, limit):
    """
    Period syntax: 1SEC, 1MIN, 1HRS, etc
    https://docs.coinapi.io/#list-all-periods
    
    Data format:
    {
        "time_period_start": "2017-08-09T14:31:00.0000000Z",
        "time_period_end": "2017-08-09T14:32:00.0000000Z",
        "time_open": "2017-08-09T14:31:01.0000000Z",
        "time_close": "2017-08-09T14:31:46.0000000Z",
        "price_open": 3255.590000000,
        "price_high": 3255.590000000,
        "price_low": 3244.740000000,
        "price_close": 3244.740000000,
        "volume_traded": 16.903274550,
        "trades_count": 31
    }
    """
 
    data = api.ohlcv_latest_data_by_asset(
        'BTC', 
        'USD',
        {'period_id': period,
         'limit': limit}
    )
    return data
