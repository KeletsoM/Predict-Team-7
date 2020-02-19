def date_parser(dates):
    """ This function returns a list of strings where each element in the returned list contains only the date
    
    Example
    -------

        Input: ['2019-11-29 12:50:54',
                '2019-11-29 12:46:53',
                '2019-11-29 12:46:10']

        Output: ['2019-11-29', '2019-11-29', '2019-11-29']
        
    """

    c = []  # initialize an empty list
    for i in dates: 
        i = i[:10]  # the date from the datetime string is only made up of 9 characters
        c.append(i)  # Adds items to the list c
    return c        #return list c
