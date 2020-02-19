""" Test for function 6"""

import pandas as pd
import numpy as np 

from EskomFunctions import function6
twitter_url = 'https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Data/twitter_nov_2019.csv'
twitter_df = pd.read_csv(twitter_url)
twitter_df.head()

assert word_splitter(twitter_df.copy()).loc[0, "Without Stop Words"] == ['@bongadlulane', 'Please', 'send', 'an', 'email', 'to', 'mediadesk@eskom.co.za']