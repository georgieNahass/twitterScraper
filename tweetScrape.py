import GetOldTweets3 as got
import pandas as pd


class Scrape ():
    def __init__(self, args):
  
        self.text_query = args.Q
        self.since_date = args.I
        self.until_date = args.F
        self.place = args.P
        self.distance = args.D
        self.count = args.X
        self.top = args.T

        # Creation of query object
        tweetCriteria = got.manager.TweetCriteria().setQuerySearch(self.text_query)\
                                                    .setMaxTweets(self.count)\
                                                    .setSince(self.since_date)\
                                                    .setUntil(self.until_date)\
                                                    .setNear(self.place)\
                                                    .setWithin(self.distance)\
                                                    .setTopTweets(self.top) 

        # Creation of list that contains all tweets
        tweets = got.manager.TweetManager.getTweets(tweetCriteria)

        # Creating list of chosen tweet data
        text_tweets = [[tweet.date, tweet.text, tweet.username, tweet.favorites, tweet.retweets, tweet.mentions, tweet.hashtags ] for tweet in tweets]

        # Creation of dataframe from tweets list
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)
        pd.set_option('display.max_colwidth', None)        
        tweets_df = pd.DataFrame(text_tweets, columns = ['date','tweet', 'Username', 'Favorites', 'Retweets', 'Mentions', 'HashTags'])
        print (self.top)
        tweets_df.to_html('scrapeOutput!.html')