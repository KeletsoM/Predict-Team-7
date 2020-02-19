### START FUNCTION

def word_splitter(df):
    """ This function takes pandas dataframe as input, split the sentence into a list of separate words and returns a modified dataframe

Example 
    Input:

    Tweets                                                  Date
    @IamGladstone @CityPowerJhb @HermanMashaba The...       2019-11-29 11:28:40
    #ESKOMFREESTATE #MEDIASTATEMENT : ESKOM SUSPEN... 	    2019-11-29 12:17:43

    Output:
    Tweets                                                  Date                        Split Tweets   
    @IamGladstone @CityPowerJhb @HermanMashaba The...       2019-11-29 11:28:40         [@bongadlulane, please, send, an, email, to, m...
    #ESKOMFREESTATE #MEDIASTATEMENT : ESKOM SUSPEN... 	    2019-11-29 12:17:40         [#eskomfreestate, #mediastatement, :, eskom, s...

"""

    # your code here
    # initializing char to increment through the data frame with
    char = 0
    
    # each char (word) encountered has the .lower and .split methods applied to it 
    # in the data frame as in increments
    df['Split Tweets'] = [char.lower().split() for char in df['Tweets']]
    
    # the returned result should be displayed 
    # in the following columns and rows using the .head function
    df[['Tweets','Date', 'Split Tweets']].head()
    
    #return result
    return (df)

### END FUNCTION
