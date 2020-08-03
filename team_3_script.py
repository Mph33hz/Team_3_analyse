import numpy
import pandas


def word_splitter(df):


    ''' This function splits sentences in a dataframe's column into a list
    of lower case seperate words and returns the dataframe with a new column
    named 'Split Tweets' that holds a list of lower case seperate words.

    args:
        df(Dataframe): A dataframe with a column named 'Tweets' which holds
        sentences.

    return:
        df(dataframe): A dataframe with a new column named 'Split tweets'
        that holds a list of lower case seperate words.
    '''
    tweets = df['Tweets'].copy()

    for i in range(len(tweets)):
        tweets[i] = tweets[i].lower().split()

    df['Split Tweets'] = tweets

    return df



def date_parser(dates):

    ''' This function takes in a string consisting of a date and time
    in the form 'yyyy-mm-dd hh:mm:ss and returns just the date in
    the form 'yyy-mm-dd'.
    '''

    newList = []  # creating an empty list
    for i in dates:  # for loop
        newList.append(i[:10])  # choosing the first 10 letters in 'dates'
    return newList




