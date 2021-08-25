# Bokeh Web Server for Bitlon Tweets

## Pushing to Heroku
1. Push git changes to main
2. Login to Heroku: `heroku login -i`
2. Set up heroku remote git: `heroku git:remote -a cryptic-wildwood-73826`
3. Push files from r: `git subtree push --prefix users/michaelt/bitlon_tweet/bokeh_web heroku master`