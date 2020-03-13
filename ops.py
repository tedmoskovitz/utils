import numpy as np 

def running_mean(x, N):
    """
    compute the running mean with a window size of N
    """ 
    cumsum = np.cumsum(np.insert(x, 0, 0)) 
    return (cumsum[N:] - cumsum[:-N]) / float(N)