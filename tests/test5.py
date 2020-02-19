""" Test for function 5"""

from EskomFunctions.function5 import number_of_tweets_per_day
import pandas as pd
twitter_url = 'https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Data/twitter_nov_2019.csv'
twitter_df = pd.read_csv(twitter_url)
twitter_df.head()

assert number_of_tweets_per_day(twitter_df.copy()).iloc[0,0] == 18