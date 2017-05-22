'''
May 2017
@author: Burkhard
'''

import numpy as np
import matplotlib.pyplot as plt
from pylab import show

x = np.arange(0, 5, 0.1);
y = np.sin(x)
plt.plot(x, y)

show()              # call show() 
