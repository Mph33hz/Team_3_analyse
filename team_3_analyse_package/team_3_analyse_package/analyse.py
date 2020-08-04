import numpy as np
import pandas as pd

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
    return_dict = {}

    # changing items list to sorted numpy array
    np_items = np.array(items)
    np_items = np.sort(np_items)

    # assigning minimum & maximum value
    return_dict['min'] = round(np_items[0], 2)
    return_dict['max'] = round(np_items[-1], 2)

    # assigning median value
    return_dict['median'] = round(np.median(np_items), 2)

    # assigning q1 value
    return_dict['q1'] = round(np.percentile(np_items, 25), 2)

    # assigning q2 value
    return_dict['q2'] = round(np.percentile(np_items, 75), 2)

    return return_dict

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
    mean = {'mean': mean}
    metrics.update(mean)

    # median
    median = round(np.median(items), 2)
    median = {'median': median}
    metrics.update(median)

    # variance
    var = round(np.var(items, ddof=1), 2)
    var = {'var': var}
    metrics.update(var)

    # std
    std = round(np.std(items, ddof=1), 2)
    std = {'std': std}
    metrics.update(std)

    # min
    mini = round(min(items), 2)
    min_d = {'min': mini}
    metrics.update(min_d)

    # max
    maxi = round(max(items), 2)
    max_d = {'max': maxi}
    metrics.update(max_d)

    return metrics


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
