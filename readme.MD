# Explore Data Science Academy team 3 
We have built a package consisting of 7 python functions that compute and analyse structured and unstructured data



# Function Word_Splitter

''' This function splits sentences in a dataframe's column by whitespaces into a list
    of seperate words and returns the dataframe with a new column
    named 'Split Tweets' that holds a the list of words. The function also converts the the words in the new column 
    into lower case words. The process this function does is known as Tokenization

    args:
        df(Dataframe): The function takes in a pandas dataframe with a column named 'Tweets' as input, this column should holds
        sentences.

    return:
        df(dataframe): A  modified pandas dataframe with a new column named 'Split tweets'
        that holds a list of lower case seperate words.
        
    # Notes
           Pandas and Numpy should be imported to used this function
           
    
# Function : Number of Tweets per Day
    This function takes in a pandas dataframe as input. It returns a new dataframe that is grouped by day and uses the index to count the number of tweets for that day. The new dataframe index is named 'Date' and the new column 'Tweets', and they correspond to the Date and the number of tweets for that day, respectively. 

    args:
        pandas.index.name(): naming of the index on the new added data frame.
        Index.value_counts(): returns object containing counts of unique values.
        pd.DataFrame(): new data frame.
        DataFrame.sort_index. Sort object by labels
        
    return:
        df(index.name, dataframe): A new dataframe with a new index column
        containing the dates sorted and a column of tweets counted per day.
 
    # Notes

    Pandas should be imported to use this function.    
    
