def date_parser(dates):
    """ returns a list of strings containing only dates"""
    c = []  # initialize an empty list
    for i in dates: 
        i = i[:10]  # the date from the datetime string is only made up of 9 characters
        c.append(i)  # Adds items to the list c
    return c        #return list c
