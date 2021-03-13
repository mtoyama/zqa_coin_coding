import os

def get_user_latest_tweet(api, user):
    tweets = api.GetUserTimeline(
        screen_name=user,
        include_rts=False,
        exclude_replies=True,
        count=1)
    return tweets[0]

def get_latest_btc_prices(api, period, limit):
    """Period syntax: 1SEC, 1MIN, 1HRS, etc
    https://docs.coinapi.io/#list-all-periods"""
    data = api.ohlcv_latest_data_by_asset(
        'BTC', 
        'USD',
        {'period': period,
         'limit': limit}
    )
    return data
