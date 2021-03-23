from datetime import timedelta, datetime
from dateutil.parser import parse
import statistics

from bokeh.plotting import figure, show
from bokeh.palettes import Dark2_5 as palette
from bokeh.io import curdoc
from bokeh.models import Span, HoverTool, ColumnDataSource, LinearAxis, Range1d

from utils import parse_and_localize_utc

def graph(bitcoin_data, tweet_data):
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