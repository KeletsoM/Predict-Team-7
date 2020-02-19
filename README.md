# EskomFunctions
This library was created to house a package of python functions to analyse and calculate data from Eskom, through processing numeric and text data as Eskom requires certain metrics to be calculated for their analytical team.
The package consists of list manipulation, dictionaries, basic stats and aggregations  as well as data clean up, all of which were implemented under the PEP8 coding style guidelines.

# Developed by
Keletso Maleka
Hlamulo Mavasa
Noxolo Kheswa
Ntokozo Nkanyane
Thuthukile Ngema

## installing the package from GitHub
`pip install git+https://github.com/KeletsoM/Predict-Team-7.git`

## updating the package from GitHub
`pip install --upgrade git+https://github.com/KeletsoM/Predict-Team-7.git`

## License
MIT License

Copyright (c) 2020 KeletsoM in colLaboration with Team 7

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Listed Functions
# Function 1
 Function 1 receives a list of values as and input then calculated the mean, median, variance,standard deviation, min, and the maximum value in the list this fuction then returs a dictionary.
 Example
     --------

        Input: dictionary_of_metrics([39660.0, 36024.0, 32127.0, 39488.0,
                                        18422.0, 23532.0, 8842.0, 37416.0, 16156.0, 18730.0, 19261.0, 25275.0])

        Output: dictionary_of_metrics(gauteng) == {'mean': 26244.42, 'median': 24403.5, 'var': 108160153.17, 'std': 10400.01, 
                                                   'min': 8842.0 , 'max': 39660.0}
                                    


# Function 2
The function takes a list as input and return a dict with keys 'max', 'median', 'min', 'q1', and 'q3' 
    corresponding to the maximum, median, minimum, first quartile and third quartile, respectively.

    Example
    -------
         
           Input: gauteng = [39660.0,36024.0, 32127.0, 39488.0, 18422.0, 23532.0, 8842.0, 37416.0, 16156.0, 18730.0, 19261.0, 25275.0]

           Output: five_num_summ(gauteng) == {'max': 39660.0, 'median': 24403.5, 'min': 8842.0, 'q1': 18422.5, 'q3': 36024.5}


# Function 3
The function return a list of strings where each element in the returned list contains only the date
    
    Example
    -------

        Input: ['2019-11-29 12:50:54',
                '2019-11-29 12:46:53',
                '2019-11-29 12:46:10']

        Output: ['2019-11-29', '2019-11-29', '2019-11-29']


# Function 4
The function takes a twitter dataframe as an input then the output is the dataframe with 2 new columns namely a hashtag column and a municipality column.
 
    Example
    ------- 
    if the tweet contains the @mention '@CityPowerJhb' then the coresponding output in the municipality column should be 
    Johannesburg. 

    The function also extracts hashtags and saves them under the hastags column as a list in the dataframe.


# Function 5
The function takes a pandas dataframe of twitter data and returns the number of tweets per day on a given day.

    Example 
    ---------

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
        


# Function 6
The function takes pandas dataframe as input, split the sentence into a list of separate words and returns a modified dataframe

    Example 
    -------

    words_splitter(twitter_df.copy()).loc[0, "Split Tweets"] == ['@bongadlulane', 'please', 'send', 'an', 'email', 'to', 'mediadesk@eskom.co.za']


# Function 7 
 This function which removes english stop words from a tweet.
  
    Example:
    --------
    
    stop_words_remover(twitter_df.copy()).loc[100, "Without Stop Words"] == ['#eskomnorthwest', '#mediastatement', ':', 'notice', 'supply', 'interruption', 'lichtenburg', 'area', 'https://t.co/7hfwvxllit']

