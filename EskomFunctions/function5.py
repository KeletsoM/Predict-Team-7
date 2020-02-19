def number_of_tweets_per_day(df):

    """This function takes a pandas dataframe of twitter data and returns the number of tweets 
    per day on a given day.

    Example 
    ----------

    Input: twitter_df
        Tweets                                                      Date
        @BongaDlulane Please send an email to mediades...           2019-11-29 12:50:54
        @saucy_mamiie Pls log a call on 0860037566                  2019-11-29 12:46:53
        @BongaDlulane Query escalated to media desk. 	            2019-11-29 12:46:10
        #ESKOMFREESTATE #MEDIASTATEMENT : ESKOM SUSPEN              2019-11-29 12:17:43


    Output: 
        Date            Tweets
        2019-04-5       18
        2019-08-20      70
        2019-11-29      56
        

     """

    
    d = df['Date'].str.split(' ', expand = True) # splits the date datapoints into date & time
    df['Date'] = d.iloc[:,0]  # takes the date coloumn
    c = df.groupby('Date').count() # this line groups the data by the date and counts the number of tweets in a given day

    return c