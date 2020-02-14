def number_of_tweets_per_day(df):
    '''This function takes a dataframe of twitter data and returns the number of tweets 
    per day on a given day. '''

    
    d = df['Date'].str.split(' ', expand = True) # splits the date datapoints into date & time