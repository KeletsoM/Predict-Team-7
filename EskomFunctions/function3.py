def date_parser(dates):
    """ return a list of strings where each element in the returned list contains only the date"""
    c = []  # initialize an empty list
    for i in dates: 
        i = i[:10]  # the date from the datetime string is only made up of 9 characters
        c.append(i)  # Adds items to the list c
    return c        #return list c
