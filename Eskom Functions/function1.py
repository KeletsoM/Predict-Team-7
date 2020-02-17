def dictionary_of_metrics(items):
    import numpy as np
    
    items = np.array(items)
    h={'mean': round(np.mean(items),2),'median': round(np.median(items),2), 'var': round(np.var(items, ddof = 1),2),'std': round(np.std(items, ddof = 1),2), 'min': round(np.min(items),2), 'max': round(np.max(items),2)}

    return h
    pass