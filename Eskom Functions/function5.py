def number_of_tweets_per_day(df):

    '''This function takes a pandas dataframe of twitter data and returns the number of tweets 
    per day on a given day. '''

    
    d = df['Date'].str.split(' ', expand = True) # splits the date datapoints into date & time
    df['Date'] = d.iloc[:,0]  # takes the date coloumn
    c = df.groupby('Date').count() # this line groups the data by the date and counts the number of tweets in a given day

    return c