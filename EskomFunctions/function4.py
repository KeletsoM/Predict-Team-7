def extract_municipality_hashtags(df):


    """ This function takes a twitter dataframe as an input then the output is the dataframe with 2 new columns namely a hashtag 
    column and a municipality column.

    Example
    ------ 
    if the tweet contains the @mention '@CityPowerJhb' then the coresponding output in the municipality column should be 
    Johannesburg. 

    The function also extracts hashtags and saves them under the hastags column as a list in the dataframe.
    
    """

    import pandas as pd
    import numpy as np

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
