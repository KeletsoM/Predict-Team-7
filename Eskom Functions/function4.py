#Function 4


def extract_municipality_hashtags(df):
    # your code here

    g = df['Tweets'].str.findall(r'@.*?(?=\s|$)')
    df['municipality'] = g.apply(lambda x: [mun_dict[g] for g in mun_dict.keys() if g in x])
    df["municipality"]= df['municipality'].apply(lambda x: ''.join(x) if len(x) > 0 else np.nan)
    df['hashtags'] = df['Tweets'].str.findall(r'#.*?(?=\s|$)')
    df["hashtags"]= df['hashtags'].apply(lambda x: ','.join(x).lower().split(',') if len(x) > 0 else np.nan)
    
    return df
