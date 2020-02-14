def stop_words_remover(df):
    stopwords = stop_words_dict['stopwords']
    Tweets_split = df['Tweets'].apply(lambda x: x.lower().split()) # Tokeising the sentences are according to the definition in function 6
    no_stopwords = []  # Creating  a list to place the setences without the stopwords
    for item in Tweets_split:
        for stopword in stopwords:
            if stopword in item:
                item.remove(stopword)  # Creating  a list to place the setences without the stopwords
        no_stopwords.append(item) # Adding the setences to the created list
    df.insert(loc=2, column='Without Stop Words', value=no_stopwords)
    return df