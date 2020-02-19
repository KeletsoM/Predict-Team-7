"""" Test for function 7 """

import pandas as pd
twitter_url = 'https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Data/twitter_nov_2019.csv'
twitter_df = pd.read_csv(twitter_url)
from EskomFunctions.function7 import stop_words_remover
# Calling this function like so: stop_words_remover(twitter_df.copy()), returns the whole dataFrame 
assert stop_words_remover(twitter_df.copy()).loc[100, "Without Stop Words"] == ['#eskomnorthwest', '#mediastatement', ':', 'notice', 'supply', 'interruption', 'lichtenburg', 'area', 'https://t.co/7hfwvxllit'] 'incorrect'