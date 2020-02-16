def date_parser(dates):
    """ initialize an empty list"""
    c = [] 
    for i in dates:
        i = i[:10] 
        c.append(i) 
    return c
