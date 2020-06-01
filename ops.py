import numpy as np 

def running_mean(x, N):
    """
    compute the running mean 
    args:
        x: 1D series of scalar data 
        N: smoothing window size 
    """ 
    cumsum = np.cumsum(np.insert(x, 0, 0)) 
    return (cumsum[N:] - cumsum[:-N]) / float(N)

def smooth(scalars, weight=0.75):  
    """
    perform exponential smoothing of a series
    args:
        scalars: 1D list of scalars 
        weight: smoothing factor, between 0 and 1 (higher = greater smoothing)
    """
    last = scalars[0]  # First value in the plot (first timestep)
    smoothed = list()
    for point in scalars:
        smoothed_val = last * weight + (1 - weight) * point  # Calculate smoothed value
        smoothed.append(smoothed_val)                        # Save it
        last = smoothed_val                                  # Anchor the last smoothed value

    return smoothed