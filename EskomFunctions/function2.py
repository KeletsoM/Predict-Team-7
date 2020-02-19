def five_num_summary(items):

    """The function takes a list as input and return a dict with keys 'max', 'median', 'min', 'q1', and 'q3' 
    corresponding to the maximum, median, minimum, first quartile and third quartile, respectively.

    Example
    -------
         
           Input: gauteng = [39660.0,36024.0, 32127.0, 39488.0, 18422.0, 23532.0, 8842.0, 37416.0, 16156.0, 18730.0, 19261.0, 25275.0]

           Output: five_num_summ(gauteng) == {'max': 39660.0, 'median': 24403.5, 'min': 8842.0, 'q1': 18422.5, 'q3': 36024.5}

    """

    
    import numpy as np
    items = np.array(items)
    
    num_summary = {'max': round(np.max(items),2), 'median': round(np.median(items),2), 'min': round(np.min(items),2), 'q1': round(np.quantile(items,0.25),2), 'q3': round(np.quantile(items,0.75),2)}
    
    return num_summary
    
    
