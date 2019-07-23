from textblob import TextBlob
import tweepy
import twkeys

def twminer(keyword, twcount):
    """Search Tweets with a keyword and determine their sentiments"""

    # Authentication with Twitter using API keys stored in twkeys.py file
    auth = tweepy.OAuthHandler(twkeys.C_KEY, twkeys.C_SECRET)
    auth.set_access_token(twkeys.A_TOKEN, twkeys.A_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    # Create dictionary to store tweet number, tweet sentiment and tweet text
    twdata = {'twt_number': [],
              'twt_polarity': [],
              'twt_text': []
              }
    # Create object that stores found tweets
    twobject = tweepy.Cursor(api.search,
                               keyword,
                               lang = "en").items(twcount)
    # A loop to iterate over all found tweets
    for cnt, tw in enumerate(twobject):
        # Error handling in case siomething went wrong with Twitter API
        try:
            twdata['twt_number'].append(cnt)
            # Sentiment analysis with TextBlob
            textanalysis = TextBlob(tw.text)
            twdata['twt_polarity'].append(textanalysis.sentiment.polarity)
            # Text for each tweet is also stored
            twdata['twt_text'].append(tw.text)
        except tweepy.TweepError as twerror:
            print(twerror.reason)
    return twdata
