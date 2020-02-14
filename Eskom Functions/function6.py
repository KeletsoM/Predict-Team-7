def word_splitter(df):
# your code

# importing tokenizer wrapper function to split words
from nltk.tokenize import TreebankWordTokenizer

# importing pandas to work with data frames
import pandas as pd

# initializing tokenizer function
tokenizer = TreebankWordTokenizer() 

# calling function to split words in the data frame passed to it
tokenizer.tokenize(df) 

# using .apply function to create a Split Tweets column within data frame
  df['tweets'] = df.apply(lambda row: row, axis = 'Split Tweets')

# makes the string passed to 'Split Tweets' lowercase 
  df['Split Tweets'] = df['tweets'].str.lower()

# splits string passed to 'Split Tweets' in the data frame
  df['Split Tweets'] = tokenizer.tokenize(df)

# Prints the data frame after adding + splitting 'Split Tweets' column 
  print(df) 
