Explore Data Science Academy team 3 
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
           
    
    
