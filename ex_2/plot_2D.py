import numpy as np
import matplotlib.pyplot as plt

def Show_data_2D(x,L,s="data"):
    plt.plot(np.arange(L),x[0,:,0], color = 'red')
    plt.plot(np.arange(L),x[0,:,1], color = 'blue')
    plt.plot(np.arange(L,2*L),x[1,:,0], color = 'red')
    plt.plot(np.arange(L,2*L),x[1,:,1], color = 'blue')
    plt.plot(np.arange(2*L,3*L),x[2,:,0], color = 'red')
    plt.plot(np.arange(2*L,3*L),x[2,:,1], color = 'blue')
    plt.title(s)
    plt.xlabel("time")
    plt.show()