import os
from datetime import datetime, timedelta

import twitter
import pytz

from users.michaelt.bitlon_tweet import scheduler, report, get_data
from api_patches.coinapi_patch import CoinAPIv1Patched

def main():
    twitter_api = twitter.Api(consumer_key=os.environ['TWITTER_API_KEY'],
                          consumer_secret=os.environ['TWITTER_API_SECRET'],
                          access_token_key=os.environ['TWITTER_ACCESS_TOKEN'],
                          access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET']
    )

    coinapi = CoinAPIv1Patched(os.environ['COINAPI_API_KEY'])
    utc = pytz.UTC

    tweets = get_data.get_user_latest_tweets(
        twitter_api, 
        'elonmusk',
        utc.localize(datetime.now() - timedelta(days=1))
    )
    
    bitcoin_data = get_data.get_latest_btc_prices(coinapi, "10MIN", 144)

    report.graph(bitcoin_data, tweets)

if __name__ == "__main__":
    main()
