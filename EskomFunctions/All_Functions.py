import numpy as np
def dictionary_of_metrics(items):
    items = np.array(items)
    metric_dict = {'mean': round(np.mean(items),2),'median': round(np.median(items),2), 
                    'var': round(np.var(items, ddof = 1),2),'std': round(np.std(items, ddof = 1),2), 
                    'min': round(np.min(items),2), 'max': round(np.max(items),2)}

    return metric_dict # returning the the metrics dictionary

def five_num_summary(items):
    items = np.array(items)
    num_summary = {'max': round(np.max(items),2), 'median': round(np.median(items),2), 
    'min': round(np.min(items),2), 'q1': round(np.quantile(items,0.25),2), 
    'q3': round(np.quantile(items,0.75),2)} #Assigning the required data to 'num_summary'
    
    return num_summary # returning the the summary

def date_parser(dates):
    c = []  # initialize an empty list
    for i in dates: 
        i = i[:10]  # the date from the datetime string is only made up of 9 characters
        c.append(i)  # Adds items to the list c
    return c        #return list c

def extract_municipality_hashtags(df):
    mun_dict = {
    '@CityofCTAlerts' : 'Cape Town',
    '@CityPowerJhb' : 'Johannesburg',
    '@eThekwiniM' : 'eThekwini' ,
    '@EMMInfo' : 'Ekurhuleni',
    '@centlecutility' : 'Mangaung',
    '@NMBmunicipality' : 'Nelson Mandela Bay',
    '@CityTshwane' : 'Tshwane'
        }

    g = df['Tweets'].str.findall(r'@.*?(?=\s|$)') # finds all @mentions 
    df['municipality'] = g.apply(lambda x: [mun_dict[g] for g in mun_dict.keys() if g in x]) # produces the values for the keys found in the tweets
    df["municipality"]= df['municipality'].apply(lambda x: ''.join(x) if len(x) > 0 else np.nan) # removes the list format to string format
    df['hashtags'] = df['Tweets'].str.findall(r'#.*?(?=\s|$)') # finds all the hashtags and stores them in the newly created hashtags column 
    df["hashtags"]= df['hashtags'].apply(lambda x: ','.join(x).lower().split(',') if len(x) > 0 else np.nan) # makes all the hashtags lowercase 
    
    return df

def number_of_tweets_per_day(df):
    d = df['Date'].str.split(' ', expand = True) # splits the date datapoints into date & time
    df['Date'] = d.iloc[:,0]  # takes the date coloumn
    c = df.groupby('Date').count() # this line groups the data by the date and counts the number of tweets in a given day

    return c  # returning the df with counted number of tweets

def word_splitter(df):
    # initializing char to increment through the data frame with
    char = 0
    
    # each char (word) encountered has the .lower and .split methods applied to it 
    # in the data frame as in increments
    df['Split Tweets'] = [char.lower().split() for char in df['Tweets']]
    
    # the returned result should be displayed 
    # in the following columns and rows using the .head function
    df[['Tweets','Date', 'Split Tweets']].head()
    
    #return result
    return df

def stop_words_remover(df):
     stop_words_dict = {
    'stopwords':[
        'where', 'done', 'if', 'before', 'll', 'very', 'keep', 'something', 'nothing', 'thereupon', 
        'may', 'why', 'â€™s', 'therefore', 'you', 'with', 'towards', 'make', 'really', 'few', 'former', 
        'during', 'mine', 'do', 'would', 'of', 'off', 'six', 'yourself', 'becoming', 'through', 
        'seeming', 'hence', 'us', 'anywhere', 'regarding', 'whole', 'down', 'seem', 'whereas', 'to', 
        'their', 'various', 'thereafter', 'â€˜d', 'above', 'put', 'sometime', 'moreover', 'whoever', 'although', 
        'at', 'four', 'each', 'among', 'whatever', 'any', 'anyhow', 'herein', 'become', 'last', 'between', 'still', 
        'was', 'almost', 'twelve', 'used', 'who', 'go', 'not', 'enough', 'well', 'â€™ve', 'might', 'see', 'whose', 
        'everywhere', 'yourselves', 'across', 'myself', 'further', 'did', 'then', 'is', 'except', 'up', 'take', 
        'became', 'however', 'many', 'thence', 'onto', 'â€˜m', 'my', 'own', 'must', 'wherein', 'elsewhere', 'behind', 
        'becomes', 'alone', 'due', 'being', 'neither', 'a', 'over', 'beside', 'fifteen', 'meanwhile', 'upon', 'next', 
        'forty', 'what', 'less', 'and', 'please', 'toward', 'about', 'below', 'hereafter', 'whether', 'yet', 'nor', 
        'against', 'whereupon', 'top', 'first', 'three', 'show', 'per', 'five', 'two', 'ourselves', 'whenever', 
        'get', 'thereby', 'noone', 'had', 'now', 'everyone', 'everything', 'nowhere', 'ca', 'though', 'least', 
        'so', 'both', 'otherwise', 'whereby', 'unless', 'somewhere', 'give', 'formerly', 'â€™d', 'under', 
        'while', 'empty', 'doing', 'besides', 'thus', 'this', 'anyone', 'its', 'after', 'bottom', 'call', 
        'nâ€™t', 'name', 'even', 'eleven', 'by', 'from', 'when', 'or', 'anyway', 'how', 'the', 'all', 
        'much', 'another', 'since', 'hundred', 'serious', 'â€˜ve', 'ever', 'out', 'full', 'themselves', 
        'been', 'in', "'d", 'wherever', 'part', 'someone', 'therein', 'can', 'seemed', 'hereby', 'others', 
        "'s", "'re", 'most', 'one', "n't", 'into', 'some', 'will', 'these', 'twenty', 'here', 'as', 'nobody', 
        'also', 'along', 'than', 'anything', 'he', 'there', 'does', 'we', 'â€™ll', 'latterly', 'are', 'ten', 
        'hers', 'should', 'they', 'â€˜s', 'either', 'am', 'be', 'perhaps', 'â€™re', 'only', 'namely', 'sixty', 
        'made', "'m", 'always', 'those', 'have', 'again', 'her', 'once', 'ours', 'herself', 'else', 'has', 'nine', 
        'more', 'sometimes', 'your', 'yours', 'that', 'around', 'his', 'indeed', 'mostly', 'cannot', 'â€˜ll', 'too', 
        'seems', 'â€™m', 'himself', 'latter', 'whither', 'amount', 'other', 'nevertheless', 'whom', 'for', 'somehow', 
        'beforehand', 'just', 'an', 'beyond', 'amongst', 'none', "'ve", 'say', 'via', 'but', 'often', 're', 'our', 
        'because', 'rather', 'using', 'without', 'throughout', 'on', 'she', 'never', 'eight', 'no', 'hereupon', 
        'them', 'whereafter', 'quite', 'which', 'move', 'thru', 'until', 'afterwards', 'fifty', 'i', 'itself', 'nâ€˜t',
        'him', 'could', 'front', 'within', 'â€˜re', 'back', 'such', 'already', 'several', 'side', 'whence', 'me', 
        'same', 'were', 'it', 'every', 'third', 'together'
    ]
}
    stopwords = stop_words_dict['stopwords'] # Extracting the stopwords from the stopwords dict
    Tweets_split = df['Tweets'].apply(lambda x: x.lower().split()) # Tokeising the sentences are according to the definition in function 6
    no_stopwords = Tweets_split.apply(lambda x: [item for item in x if item not in stopwords]) # Removing stopwords from each tweet list using the lambda function, then assinging this to a 'no_stopwords' variable
    df.insert(loc=2, column='Without Stop Words', value=no_stopwords) # Adding the tweets withouth stopwords as a column to the DataFrame
    
    # returning the df with the no_stop_words tweets
    return df
