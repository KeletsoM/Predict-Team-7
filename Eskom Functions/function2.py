def five_num_summary(items):
    
    import numpy as np
    items = np.array(items)
    
    h = {'max': round(np.max(items),2), 'median': round(np.median(items),2), 'min': round(np.min(items),2), 'q1': round(np.quantile(items,0.25),2), 'q3': round(np.quantile(items,0.75),2)}
    
    return h
    
    
