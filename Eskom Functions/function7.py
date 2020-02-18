def stop_words_remover(df):
''' This function which removes english stop words from a tweet.'''
    stopwords = stop_words_dict['stopwords']        # Extracting the stopwords from the stopwords dict
    Tweets_split = df['Tweets'].apply(lambda x: x.lower().split())          # Tokeising the sentences are according to the definition in function 6
    no_stopwords = Tweets_split.apply(lambda x: [item for item in x if item not in stopwords])          # Removing stopwords from each tweet list using the lambda function, then assinging this to a 'no_stopwords' variable
    df.insert(loc=2, column='Without Stop Words', value=no_stopwords)           # Adding the tweets withouth stopwords as a column to the DataFrame
    
    # return the dataframe to check if the new column is added.
    return df