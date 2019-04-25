import numpy as np
import matplotlib.pyplot as plt

def some_function(x):
    return(x-5.45)**2+7.7

x = np.arange(-1.0, 12.0, 0.01)
y = some_function(x)

plt.plot(x, y, marker='', color='r')
plt.grid(True)
plt.show()