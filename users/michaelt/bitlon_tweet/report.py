from datetime import timedelta, datetime
from dateutil.parser import parse

from bokeh.plotting import figure, show
from bokeh.palettes import Dark2_5 as palette
from bokeh.io import curdoc
from bokeh.models import Span, HoverTool, ColumnDataSource

def graph(bitcoin_data, tweet_data):
    curdoc().theme = 'dark_minimal'
    p = figure(
        title='BitCoin x Elon Musk',
        x_axis_label='date',
        y_axis_label='Bitcoin Price'
    )

    p.line(
        [parse(x["time_period_start"]) for x in bitcoin_data],
        [y["price_close"] for y in bitcoin_data],
        legend_label = "BitCoin Price",
        line_width=2,
        line_color='gray'
    )

    x_tweet = []
    y_tweet = [1 for x in range(0, len(tweet_data))]
    desc_tweet = []
    for tweet in tweet_data:
        x_tweet.append(tweet.created_at)
        desc_tweet.append(tweet.text)
        tweet_line = Span(location=tweet.created_at,
                          dimension='height', line_color = 'deepskyblue',
                          line_dash='dashed', line_width=1)
        p.add_layout(tweet_line)
    
    source = ColumnDataSource(data=dict(
        x=x_tweet,
        y=y_tweet,
        desc=desc_tweet,
    ))
    circle = p.circle(source=source, size=2, alpha=0)
    tweet_hovertool = HoverTool(
        renderers = [circle],
        mode = 'vline',
        tooltips = [("@elonmusk:", "@desc")],
    )
    p.tools.append(tweet_hovertool)

    show(p)