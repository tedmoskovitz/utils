import matplotlib.pyplot as plt
import numpy as np
import time
import sys 

def plt_dynamic(x, y, fig, ax, colors=['b']):
    """
    written by Sam Greydanus

    call in a loop to dynamically plot (e.g., a loss fn)
    example:
        fig,ax = plt.subplots(1,1)
        ax.set_xlabel('X') ; ax.set_ylabel('Y')
        ax.set_xlim(0,360) ; ax.set_ylim(-1,1)
        xs, ys = [], []

        # this is any loop for which you want to plot dynamic updates.
        # in my case, I'm plotting loss functions for neural nets
        for x in range(360):
            y = np.sin(x*np.pi/180)
            xs.append(x)
            ys.append(y)
            if x % 30 == 0:
                plt_dynamic(xs, ys, ax)
                time.sleep(.2)
        plt_dynamic(xs, ys, ax)
    note: if using in a jupyter notebook, make sure to set 
    %matplotlib notebook 
    """
    for color in colors:
        ax.plot(x, y, color)
    fig.canvas.draw()


def flush_print(s):
    """
    print updates in a loop that refresh rather than stack 
    """
    print("\r" + s, end="")
    sys.stdout.flush()
