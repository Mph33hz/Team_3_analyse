import numpy
import pandas

def five_num_summary(items):
    
    return_dict={}
    
    #changing items list to sorted numpy array
    np_items = np.array(items)
    np_items = np.sort(np_items)
    
    #assigning minimum & maximum value
    return_dict['min'] = round(np_items[0], 2)
    return_dict['max'] = round(np_items[-1], 2)
    
    #assigning median value
    return_dict['median'] = round(np.median(np_items), 2)
    
    #assigning q1 value
    return_dict['q1'] = round(np.percentile(np_items, 25), 2)
    
    #assigning q2 value
    return_dict['q3'] = round(np.percentile(np_items, 75), 2)
    
    return return_dict

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



