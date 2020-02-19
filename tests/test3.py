""" Test for function 3"""

import pandas as pd
from EskomFunctions.function3 import date_parser
twitter_url = 'https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Data/twitter_nov_2019.csv'
twitter_df = pd.read_csv(twitter_url)
dates = twitter_df['Date'].to_list()
assert date_parser(dates[:3]) == ['2019-11-29', '2019-11-29', '2019-11-29']
assert date_parser(dates[-3:]) == ['2019-11-20', '2019-11-20', '2019-11-20']