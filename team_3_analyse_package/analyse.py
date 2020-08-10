import numpy as np
import pandas as pd

# dictionary mapping official municipality twitter handles to the municipality name
mun_dict = {
    '@CityofCTAlerts' : 'Cape Town',
    '@CityPowerJhb' : 'Johannesburg',
    '@eThekwiniM' : 'eThekwini' ,
    '@EMMInfo' : 'Ekurhuleni',
    '@centlecutility' : 'Mangaung',
    '@NMBmunicipality' : 'Nelson Mandela Bay',
    '@CityTshwane' : 'Tshwane'
}

# dictionary of english stopwords
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


def dictionary_of_metrics(items):
    """
    a function that calculates the mean, median, variance,
    standard deviation, minimum and maximum of of list of items.

    Args:
        items(list[int]) a list of intergers.

    Returns:
         a dict with keys 'mean', 'median', 'std', 'var', 'min',
         and 'max', corresponding to the mean, median, standard deviation,
         variance, minimum and maximum of the input list, respectively.
    """
    metrics = {}
    # Mean
    mean = round(np.mean(items), 2)
    metrics['mean'] = mean

    # median
    median = round(np.median(items), 2)
    metrics['median'] = median

    # variance
    var = round(np.var(items, ddof=1), 2)
    metrics['var'] = var

    # std
    std = round(np.std(items, ddof=1), 2)
    metrics['std'] = std

    # min
    mini = round(min(items), 2)
    metrics['min'] = mini

    # max
    maxi = round(max(items), 2)
    metrics['max'] = maxi

    return metrics

def five_num_summary(items):
    """
    function which takes in a list of integers and returns
    a dictionary of the five number summary.

    Args:
        items(list[int]) a list of intergers

    Returns:
        dict: a dict with keys 'max', 'median', 'min', 'q1',
        and 'q3' corresponding to the maximum, median, minimum,
        first quartile and third quartile, respectively rounded
        to two decimal places.
    """
   
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


def date_parser(dates):
    ''' This function takes in a string consisting of a date and time
    in the form 'yyyy-mm-dd hh:mm:ss and returns just the date in
    the form 'yyy-mm-dd'

    args:
        dates: A list consisting of strings in the format 'yyyy-mm-dd hh:mm:ss'
        newList: A list consisting of dates only in the form 'yyyy-mm-dd'
        from the dates variable.

    return:
        returns a list that consists only of the first 10 words/characters in
        each string, thus outputting only the date in the form 'yyyy-mm-dd'
    '''
    newList = []  # creating an empty list
    for i in dates:  # for loop
        newList.append(i[:10])  # choosing the first 10 letters in 'dates'
    return newList


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

def stop_words_remover(df):

    ''' This function removes all english stop words from a tokenised list
    in a dataframe's column and returns the modified dataframe with a new
    column named 'tweets_without_stopwords' that holds a tokenised list
    without english stop words.
    args:
        df(Dataframe): A pandas dataframe with a column named 'Tweets'.
    return:
        df(dataframe): A modified pandas dataframe consisting of a new
        column named 'tweets_without_stopwords' that holds a list of
        tweets that have no stop words.
    '''
    tweets = df['Tweets'].copy()

    # Tokenizing
    for i in range(len(tweets)):
        tweets[i] = tweets[i].lower().split()

        # Stop words removal
        tweets_without_stopwords = []
        for word in tweets[i]:
            if word not in stop_words_dict['stopwords']:
                tweets_without_stopwords.append(word)
        tweets[i] = tweets_without_stopwords
    df['Without Stop Words'] = tweets

    return df

def extract_municipality_hashtags(df):

    """" Returns a DataFrame with two additional column with data 'Municipality'
         and 'Hashtags'
         Args:
             DataFrame: DateFrame with Data,Index and Colums
        Return:
             DataFrame: A DataFrame with additional columns with data
        Egs:
             df['new colum'] = col_name
    """
    tweets = df['Tweets']
    tweets.map(lambda x: (i[1:] for i in x.split() if i.startswith('@')))
    df['municipality'] = tweets
    df['municipality'] = df.index.to_series().map(mun_dict)
    df['hashtags'] = df.Tweets. str.lower().str.findall(r'#.*?(?=\s|$)')
    htags = df['hashtags']
    df['hashtags'] = htags.apply(lambda x: np.nan if len(x) == 0 else x)
    return df

def number_of_tweets_per_day(df):
    '''
    This function calculates the number of tweets per day by accouting for
    a data frame that takes intweets posted at different times of the day.
    Args:
        df.index.name(): naming of the index on the new added data frame.
        value_counts(): A dataframe consists of a date (yyyy-mm-dd) and time
    with counted tweets per single day.
        pd.DataFrame(): new data frame.
    Return:
        df(index.name, dataframe): A new dataframe with a new index column
    containing the dates sortedand a column of tweets counted per day.
    '''
    df.Date = twitter_df.Date.apply(pd.to_datetime)
    df['Day'] = [d.date() for d in df['Date']]
    df['Time'] = [d.time() for d in df['Date']]
    df = (df.Day.value_counts()).sort_index()
    df = pd.DataFrame({'Tweets': df})
    df.index.name = 'Date'
    return df

