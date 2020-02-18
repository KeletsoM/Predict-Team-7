def word_splitter(df):
# your code

import pandas as pd
def word_splitter(df):
    df['tweets'] = df.apply(lambda row: row, axis = 'Split_Tweets')
    df['Split_Tweets'] = df['tweets'].str.lower()
    for i in list:
        Split_Tweets.append(i.split(' '))
        print(df)